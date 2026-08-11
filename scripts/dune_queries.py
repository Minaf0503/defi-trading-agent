#!/usr/bin/env python
"""
Defines and (re-)creates this project's two Dune Analytics queries used by
the On-Chain Analyst (holder concentration, DEX volume) -- see
tradingagents/dataflows/onchain/dune_api.py.

These were originally created ad hoc via direct API calls while debugging;
this script makes that reproducible. Run with --update to push the current
SQL below to existing query IDs (e.g. after fixing a bug in the SQL), or
with no flags to print the SQL for reference.

Both queries were hand-verified live against real Ethereum mainnet data on
2026-06-22 (see writing/papers/PROGRESS_LOG.md). Key gotcha: Dune substitutes
{{param}} into the SQL text with no added quoting, so a hex address param
must be wrapped in single quotes in the SQL (from_hex('{{token_address}}'))
and the Python caller must pass the address without its "0x" prefix --
getting either of those wrong produces a confusing SQL-level error, not an
auth/config error.

Usage:
    python scripts/dune_queries.py                 # print SQL
    python scripts/dune_queries.py --update IDS     # push SQL to existing query IDs, e.g.:
        python scripts/dune_queries.py --update --holder-id 7774547 --volume-id 7774491
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

HOLDER_QUERY_SQL = """with transfers as (
    select "from" as address, -value as amount
    from erc20_ethereum.evt_Transfer
    where contract_address = from_hex('{{token_address}}')
    union all
    select "to" as address, value as amount
    from erc20_ethereum.evt_Transfer
    where contract_address = from_hex('{{token_address}}')
)
select address, sum(amount) as balance_raw
from transfers
where address != 0x0000000000000000000000000000000000000000
group by address
having sum(amount) > 0
order by balance_raw desc
limit 50"""

VOLUME_QUERY_SQL = """select
  date_trunc('day', block_time) as day,
  sum(amount_usd) as volume_usd,
  count(*) as trade_count
from dex.trades
where (token_bought_address = from_hex('{{token_address}}')
    or token_sold_address = from_hex('{{token_address}}'))
  and block_time >= now() - interval '{{days_back}}' day
group by 1
order by 1 desc"""


def _headers():
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("DUNE_API_KEY")
    if not api_key:
        raise SystemExit("DUNE_API_KEY not set in .env")
    return {"X-DUNE-API-KEY": api_key, "Content-Type": "application/json"}


def create_query(name: str, sql: str, parameters: list) -> int:
    import requests

    r = requests.post(
        "https://api.dune.com/api/v1/query",
        headers=_headers(),
        json={"name": name, "query_sql": sql, "parameters": parameters, "is_private": False},
    )
    r.raise_for_status()
    return r.json()["query_id"]


def update_query(query_id: int, sql: str) -> None:
    import requests

    r = requests.patch(
        f"https://api.dune.com/api/v1/query/{query_id}",
        headers=_headers(),
        json={"query_sql": sql},
    )
    r.raise_for_status()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update", action="store_true", help="push current SQL to existing query IDs")
    parser.add_argument("--holder-id", type=int, default=None)
    parser.add_argument("--volume-id", type=int, default=None)
    args = parser.parse_args()

    if not args.update:
        print("-- Holder query SQL (DUNE_HOLDER_QUERY_ID) --")
        print(HOLDER_QUERY_SQL)
        print("\n-- Volume query SQL (DUNE_VOLUME_QUERY_ID) --")
        print(VOLUME_QUERY_SQL)
        return

    if args.holder_id:
        update_query(args.holder_id, HOLDER_QUERY_SQL)
        print(f"Updated holder query {args.holder_id}")
    if args.volume_id:
        update_query(args.volume_id, VOLUME_QUERY_SQL)
        print(f"Updated volume query {args.volume_id}")
    if not args.holder_id and not args.volume_id:
        print("No --holder-id/--volume-id given; nothing to update.")


if __name__ == "__main__":
    main()
