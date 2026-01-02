# Import from existing modules (these should always be available)
from .googlenews_utils import getNewsData
from .reddit_utils import fetch_top_from_category
from .rss_utils import (
    fetch_rss_feed,
    parse_rss_entries,
    filter_articles_by_asset,
    filter_articles_by_date,
    fetch_dlnews_rss,
    fetch_article_content
)

# Import from interface if available (with error handling for missing dependencies)
# Note: interface.py may import from modules that don't exist (finnhub_utils, yfin_utils, etc.)
# So we need to handle ImportError gracefully
try:
    from .interface import (
        # News and sentiment functions
        get_finnhub_news,
        get_finnhub_company_insider_sentiment,
        get_finnhub_company_insider_transactions,
        get_google_news,
        get_reddit_global_news,
        get_reddit_company_news,
        # Financial statements functions
        get_simfin_balance_sheet,
        get_simfin_cashflow,
        get_simfin_income_statements,
        # Technical analysis functions
        get_stock_stats_indicators_window,
        get_stockstats_indicator,
        # Market data functions
        get_YFin_data_window,
        get_YFin_data,
    )
except (ImportError, ModuleNotFoundError) as e:
    # If interface imports fail due to missing dependencies, 
    # we'll just skip those imports - RSS utils should still work
    import warnings
    warnings.warn(f"Some dataflows imports failed (missing dependencies): {e}. RSS utils are still available.")
    # Define None for missing functions so __all__ doesn't break
    get_finnhub_news = None
    get_finnhub_company_insider_sentiment = None
    get_finnhub_company_insider_transactions = None
    get_google_news = None
    get_reddit_global_news = None
    get_reddit_company_news = None
    get_simfin_balance_sheet = None
    get_simfin_cashflow = None
    get_simfin_income_statements = None
    get_stock_stats_indicators_window = None
    get_stockstats_indicator = None
    get_YFin_data_window = None
    get_YFin_data = None

# Build __all__ list dynamically, only including what's available
__all__ = [
    # RSS feed functions (always available)
    "fetch_rss_feed",
    "parse_rss_entries",
    "filter_articles_by_asset",
    "filter_articles_by_date",
    "fetch_dlnews_rss",
    "fetch_article_content",
    "getNewsData",
    "fetch_top_from_category",
]

# Add interface functions only if they were successfully imported
if get_finnhub_news is not None:
    __all__.extend([
        # News and sentiment functions
        "get_finnhub_news",
        "get_finnhub_company_insider_sentiment",
        "get_finnhub_company_insider_transactions",
        "get_google_news",
        "get_reddit_global_news",
        "get_reddit_company_news",
        # Financial statements functions
        "get_simfin_balance_sheet",
        "get_simfin_cashflow",
        "get_simfin_income_statements",
        # Technical analysis functions
        "get_stock_stats_indicators_window",
        "get_stockstats_indicator",
        # Market data functions
        "get_YFin_data_window",
        "get_YFin_data",
    ])
