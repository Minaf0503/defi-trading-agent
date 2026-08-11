"""
Deterministic technical indicator computation for DeFi trading agents.

ALL arithmetic is computed here in Python. The LLM receives a pre-computed
structured snapshot and is responsible ONLY for interpretation, never calculation.

Addresses gaps in the Technical Analyst agent:
  Gap 1 - Deterministic computation (replaces LLM arithmetic)
  Gap 2 - Expanded indicator set (ADX, StochRSI, OBV, VWAP, ATR, BB squeeze, ROC)
  Gap 3 - Weekly HTF bias via daily → weekly resample
  Gap 4 - Market structure (S/R levels, pivot points, swing HH/HL detection)
  Gap 5 - Signal conflict resolution scoring with pre-defined hierarchy
  Gap 6 - Adaptive parameters based on 30-day realised volatility
  Gap 7 - Regime detection (trending/ranging/high-vol/squeeze/bb-squeeze)
  Gap 8 - Relative strength vs BTC (30-day return differential)
  Gap 9 - Candle pattern recognition (doji, hammer, engulfing, pin bar)
"""

from __future__ import annotations

import warnings
from typing import Optional

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=RuntimeWarning)


# ─────────────────────────────────────────────────────────────────────────────
# GAP 6: ADAPTIVE PARAMETER SELECTION
# ─────────────────────────────────────────────────────────────────────────────

def _select_params(hist_vol_30d: float) -> dict:
    """Scale indicator periods to the token's 30-day realised volatility.

    Equity-default parameters (RSI-14, MACD 12/26/9) are poorly calibrated for
    high-volatility DeFi tokens. A 14-period RSI on daily AAVE data oscillates
    between extremes almost continuously, destroying signal quality.
    """
    if hist_vol_30d > 200:
        return dict(rsi=21, macd_fast=19, macd_slow=39, macd_sig=9, bb=30, atr=14, vol_label="extreme")
    elif hist_vol_30d > 100:
        return dict(rsi=18, macd_fast=15, macd_slow=30, macd_sig=9, bb=25, atr=14, vol_label="high")
    elif hist_vol_30d > 60:
        return dict(rsi=14, macd_fast=12, macd_slow=26, macd_sig=9, bb=20, atr=14, vol_label="medium")
    else:
        return dict(rsi=10, macd_fast=8, macd_slow=21, macd_sig=9, bb=20, atr=14, vol_label="low")


# ─────────────────────────────────────────────────────────────────────────────
# PRIMITIVE INDICATOR FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def _ema(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, adjust=False).mean()


def _rsi(close: pd.Series, period: int) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(span=period, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(span=period, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift()).abs(),
        (low - close.shift()).abs(),
    ], axis=1).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


def _adx(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> tuple:
    atr_s = _atr(high, low, close, period)
    up = high.diff()
    dn = -low.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    plus_di = (
        100
        * pd.Series(plus_dm, index=close.index).ewm(span=period, adjust=False).mean()
        / atr_s.replace(0, np.nan)
    )
    minus_di = (
        100
        * pd.Series(minus_dm, index=close.index).ewm(span=period, adjust=False).mean()
        / atr_s.replace(0, np.nan)
    )
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx_s = dx.ewm(span=period, adjust=False).mean()
    return adx_s, plus_di, minus_di


def _stoch_rsi(rsi_series: pd.Series, period: int = 14, k_smooth: int = 3, d_smooth: int = 3) -> tuple:
    lo = rsi_series.rolling(period).min()
    hi = rsi_series.rolling(period).max()
    stoch = (rsi_series - lo) / (hi - lo).replace(0, np.nan)
    k = stoch.rolling(k_smooth).mean() * 100
    d = k.rolling(d_smooth).mean()
    return k, d


def _macd(close: pd.Series, fast: int, slow: int, signal: int) -> tuple:
    line = _ema(close, fast) - _ema(close, slow)
    sig = _ema(line, signal)
    return line, sig, line - sig


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (np.sign(close.diff()).fillna(0) * volume).cumsum()


def _vwap(close: pd.Series, volume: pd.Series, period: int = 20) -> pd.Series:
    return (close * volume).rolling(period).sum() / volume.rolling(period).sum()


def _bollinger(close: pd.Series, period: int, std_dev: float = 2.0) -> tuple:
    mid = close.rolling(period).mean()
    std = close.rolling(period).std()
    upper = mid + std_dev * std
    lower = mid - std_dev * std
    width = (upper - lower) / mid.replace(0, np.nan)
    pct_b = (close - lower) / (upper - lower).replace(0, np.nan)
    return upper, mid, lower, width, pct_b


def _hist_vol(close: pd.Series, period: int = 30) -> pd.Series:
    return np.log(close / close.shift()).rolling(period).std() * np.sqrt(365) * 100


# ─────────────────────────────────────────────────────────────────────────────
# GAP 4: MARKET STRUCTURE
# ─────────────────────────────────────────────────────────────────────────────

def _swing_structure(high: pd.Series, low: pd.Series, lookback: int = 20) -> str:
    if len(high) < lookback * 2:
        return "insufficient_data"
    h1 = high.iloc[-lookback * 2 : -lookback].max()
    h2 = high.iloc[-lookback:].max()
    l1 = low.iloc[-lookback * 2 : -lookback].min()
    l2 = low.iloc[-lookback:].min()
    hh, hl = h2 > h1, l2 > l1
    lh, ll = h2 < h1, l2 < l1
    if hh and hl:
        return "uptrend_HH_HL"
    if lh and ll:
        return "downtrend_LH_LL"
    if hh and ll:
        return "expanding_range"
    if lh and hl:
        return "contracting_range"
    return "consolidating"


def _pivot_points(prev_high: float, prev_low: float, prev_close: float) -> dict:
    p = (prev_high + prev_low + prev_close) / 3
    r1 = 2 * p - prev_low
    r2 = p + (prev_high - prev_low)
    s1 = 2 * p - prev_high
    s2 = p - (prev_high - prev_low)
    return dict(pivot=p, r1=r1, r2=r2, s1=s1, s2=s2)


# ─────────────────────────────────────────────────────────────────────────────
# GAP 9: CANDLE PATTERN RECOGNITION
# ─────────────────────────────────────────────────────────────────────────────

def _candle_patterns(df: pd.DataFrame) -> dict:
    o, h, l, c = df["open"], df["high"], df["low"], df["close"]
    body = (c - o).abs()
    upper_wick = h - pd.concat([c, o], axis=1).max(axis=1)
    lower_wick = pd.concat([c, o], axis=1).min(axis=1) - l
    rng = h - l

    doji = bool(body.iloc[-1] < rng.iloc[-1] * 0.1 and rng.iloc[-1] > 0)
    hammer = bool(
        rng.iloc[-1] > 0
        and lower_wick.iloc[-1] > body.iloc[-1] * 2
        and upper_wick.iloc[-1] < body.iloc[-1] * 0.5
    )
    bullish_engulfing = bool(
        len(df) >= 2
        and c.iloc[-2] < o.iloc[-2]
        and c.iloc[-1] > o.iloc[-1]
        and o.iloc[-1] <= c.iloc[-2]
        and c.iloc[-1] >= o.iloc[-2]
    )
    bearish_engulfing = bool(
        len(df) >= 2
        and c.iloc[-2] > o.iloc[-2]
        and c.iloc[-1] < o.iloc[-1]
        and o.iloc[-1] >= c.iloc[-2]
        and c.iloc[-1] <= o.iloc[-2]
    )
    bullish_pin = bool(
        rng.iloc[-1] > 0
        and lower_wick.iloc[-1] > rng.iloc[-1] * 0.6
        and body.iloc[-1] < rng.iloc[-1] * 0.25
    )
    bearish_pin = bool(
        rng.iloc[-1] > 0
        and upper_wick.iloc[-1] > rng.iloc[-1] * 0.6
        and body.iloc[-1] < rng.iloc[-1] * 0.25
    )

    flags = {
        "doji": doji,
        "hammer": hammer,
        "bullish_engulfing": bullish_engulfing,
        "bearish_engulfing": bearish_engulfing,
        "bullish_pin_bar": bullish_pin,
        "bearish_pin_bar": bearish_pin,
    }
    detected = [k for k, v in flags.items() if v]
    return {**flags, "detected": detected or ["none"]}


# ─────────────────────────────────────────────────────────────────────────────
# GAP 5: SIGNAL CONFLICT RESOLUTION SCORING
# ─────────────────────────────────────────────────────────────────────────────

def _score_signals(r: dict) -> tuple:
    """
    Pre-defined weighted signal hierarchy. LLM receives the pre-computed bias
    and conviction and is instructed to explain WHY, not to recompute the score.

    Hierarchy (descending weight):
      1. Macro trend (price vs 200 EMA) — weight 3
      2. EMA ribbon alignment — weight 2
      3. MACD crossover — weight 2
      4. Weekly HTF bias — weight 1
      5. RSI zone — weight ±1
      6. Volume confirmation — weight ±1
      7. BTC relative strength — weight ±0.5
    Regime gates (Gap 7):
      ADX < 20 → halve all signals (ranging market)
      vol_regime high/spike → reduce by 30%
    """
    score = 0.0
    conflicts: list[str] = []

    # 1. Macro trend
    if r["price_vs_200ema"] == "above":
        score += 3
    else:
        score -= 3

    # 2. EMA ribbon
    if r["ema_aligned_bull"]:
        score += 2
    elif r["ema_aligned_bear"]:
        score -= 2

    # 3. MACD
    if r["macd_crossover"] == "bullish":
        score += 2
    elif r["macd_crossover"] == "bearish":
        score -= 2

    # Detect MACD vs macro conflict
    if r["macd_histogram"] > 0 and r["price_vs_200ema"] == "below":
        conflicts.append("MACD histogram positive (short-term bullish) but price below 200 EMA (macro bearish)")
    if r["macd_histogram"] < 0 and r["price_vs_200ema"] == "above":
        conflicts.append("MACD histogram negative (short-term bearish) but price above 200 EMA (macro bullish)")

    # 4. Weekly HTF bias
    if r.get("weekly_bias") == "bull":
        score += 1
    elif r.get("weekly_bias") == "bear":
        score -= 1

    # 5. RSI zone
    rsi = r["rsi"]
    if 40 < rsi < 65:
        score += 1
    elif rsi > 70:
        score -= 1
        if r["price_vs_200ema"] == "above":
            conflicts.append(f"RSI overbought ({rsi:.1f}) vs price above 200 EMA (macro bullish)")
    elif rsi < 30:
        score += 1
        if r["price_vs_200ema"] == "below":
            conflicts.append(f"RSI oversold ({rsi:.1f}) vs price below 200 EMA (macro bearish)")

    # 6. Volume confirmation
    if r["volume_ratio"] > 1.5:
        if r["macd_crossover"] == "bullish":
            score += 1
        elif r["macd_crossover"] == "bearish":
            score -= 1
    if r["obv_trend"] == "rising" and r["price_vs_200ema"] == "below":
        conflicts.append("OBV rising (accumulation) but price below 200 EMA (bearish structure)")

    # 7. BTC relative strength
    rs = r.get("rs_vs_btc_30d")
    if rs is not None:
        if rs > 0.10:
            score += 0.5
        elif rs < -0.10:
            score -= 0.5

    # Regime gates (Gap 7) — applied after scoring
    adx = r["adx"]
    if adx < 20:
        score *= 0.5
        conflicts.append(f"ADX={adx:.1f} (<20): ranging market — all momentum signals have reduced reliability")
    if r["vol_regime"] in ("high_vol", "vol_spike"):
        score *= 0.7
        conflicts.append(f"vol_regime={r['vol_regime']}: elevated volatility — conviction reduced")

    if score >= 6:
        bias = "STRONG_BULL"
    elif score >= 3:
        bias = "BULL"
    elif score <= -6:
        bias = "STRONG_BEAR"
    elif score <= -3:
        bias = "BEAR"
    else:
        bias = "NEUTRAL"

    conviction = round(min(abs(score) / 8.0, 1.0), 3)
    return round(score, 2), bias, conviction, conflicts


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

def compute_technical_snapshot(
    df: pd.DataFrame,
    token: str,
    btc_df: Optional[pd.DataFrame] = None,
) -> dict:
    """
    Compute a complete deterministic technical snapshot from daily OHLCV data.

    Args:
        df:      Daily OHLCV DataFrame with columns [timestamp, open, high, low, close, volume].
                 Needs ≥ 60 rows; EMA-200 becomes reliable at ≥ 250 rows.
        token:   Token symbol, for labelling only.
        btc_df:  Optional BTC daily OHLCV for Gap 8 relative-strength computation.

    Returns:
        Flat dict (all values JSON-serialisable) — passed directly to the LLM.
    """
    min_bars = 60
    if len(df) < min_bars:
        raise ValueError(f"Need ≥ {min_bars} daily bars, got {len(df)}")

    # Normalise column names and set timestamp as index where needed
    df = df.copy()
    close = df["close"]
    high = df["high"]
    low = df["low"]
    volume = df["volume"]
    open_ = df["open"]
    price = float(close.iloc[-1])

    # ── Step 0: hist vol first (drives adaptive params) ─────────────
    hv_series = _hist_vol(close, 30)
    hv30 = float(hv_series.iloc[-1]) if not np.isnan(hv_series.iloc[-1]) else 80.0
    p = _select_params(hv30)

    # ── Step 1: Trend indicators ────────────────────────────────────
    ema8 = _ema(close, 8)
    ema21 = _ema(close, 21)
    ema50 = _ema(close, 50)
    ema200 = _ema(close, 200)
    adx_s, plus_di_s, minus_di_s = _adx(high, low, close, 14)

    ema8_v = float(ema8.iloc[-1])
    ema21_v = float(ema21.iloc[-1])
    ema50_v = float(ema50.iloc[-1])
    ema200_v = float(ema200.iloc[-1])
    adx_v = float(adx_s.iloc[-1]) if not np.isnan(adx_s.iloc[-1]) else 20.0
    plus_di_v = float(plus_di_s.iloc[-1]) if not np.isnan(plus_di_s.iloc[-1]) else 20.0
    minus_di_v = float(minus_di_s.iloc[-1]) if not np.isnan(minus_di_s.iloc[-1]) else 20.0

    ema_bull = ema8_v > ema21_v > ema50_v
    ema_bear = ema8_v < ema21_v < ema50_v
    vs_200 = "above" if price > ema200_v else "below"

    if adx_v > 25:
        trend_regime = "strong_trend_up" if plus_di_v > minus_di_v else "strong_trend_down"
    elif adx_v > 18:
        trend_regime = "weak_trend_up" if plus_di_v > minus_di_v else "weak_trend_down"
    else:
        trend_regime = "ranging"

    # ── Step 2: Momentum ────────────────────────────────────────────
    rsi14 = _rsi(close, p["rsi"])
    rsi7 = _rsi(close, 7)
    stoch_k, stoch_d = _stoch_rsi(rsi14, 14)
    macd_line, macd_sig, macd_hist = _macd(close, p["macd_fast"], p["macd_slow"], p["macd_sig"])
    roc14 = close.pct_change(14) * 100

    rsi_v = float(rsi14.iloc[-1]) if not np.isnan(rsi14.iloc[-1]) else 50.0
    rsi7_v = float(rsi7.iloc[-1]) if not np.isnan(rsi7.iloc[-1]) else 50.0
    stoch_k_v = float(stoch_k.iloc[-1]) if not np.isnan(stoch_k.iloc[-1]) else 50.0
    stoch_d_v = float(stoch_d.iloc[-1]) if not np.isnan(stoch_d.iloc[-1]) else 50.0
    macd_v = float(macd_line.iloc[-1])
    macd_sig_v = float(macd_sig.iloc[-1])
    macd_hist_v = float(macd_hist.iloc[-1])
    roc14_v = float(roc14.iloc[-1]) if not np.isnan(roc14.iloc[-1]) else 0.0

    crossover = "none"
    if len(macd_hist) >= 2 and not np.isnan(macd_hist.iloc[-2]):
        if macd_hist.iloc[-1] > 0 and macd_hist.iloc[-2] <= 0:
            crossover = "bullish"
        elif macd_hist.iloc[-1] < 0 and macd_hist.iloc[-2] >= 0:
            crossover = "bearish"

    if rsi_v > 70:
        mom_regime = "overbought"
    elif rsi_v < 30:
        mom_regime = "oversold"
    elif rsi_v >= 50 and macd_hist_v > 0:
        mom_regime = "healthy_bull"
    elif rsi_v < 50 and macd_hist_v < 0:
        mom_regime = "healthy_bear"
    else:
        mom_regime = "neutral"

    # ── Step 3: Volatility ──────────────────────────────────────────
    atr_s = _atr(high, low, close, p["atr"])
    bb_up, bb_mid, bb_lo, bb_w, bb_pct = _bollinger(close, p["bb"])

    atr_v = float(atr_s.iloc[-1])
    atr_pct_v = round(atr_v / price * 100, 3) if price else 0.0
    bb_up_v = float(bb_up.iloc[-1])
    bb_mid_v = float(bb_mid.iloc[-1])
    bb_lo_v = float(bb_lo.iloc[-1])
    bb_w_v = float(bb_w.iloc[-1]) if not np.isnan(bb_w.iloc[-1]) else 0.0
    bb_pct_v = float(bb_pct.iloc[-1]) if not np.isnan(bb_pct.iloc[-1]) else 0.5

    bb_w_clean = bb_w.dropna()
    squeeze = False
    if len(bb_w_clean) >= 20:
        roll_size = min(100, len(bb_w_clean))
        q20 = float(bb_w_clean.rolling(roll_size).quantile(0.2).iloc[-1])
        squeeze = bool(bb_w_v < q20)

    atr_clean = atr_s.dropna()
    vol_regime = "normal_vol"
    if len(atr_clean) >= 20:
        roll_size = min(100, len(atr_clean))
        q25 = float(atr_clean.rolling(roll_size).quantile(0.25).iloc[-1])
        q75 = float(atr_clean.rolling(roll_size).quantile(0.75).iloc[-1])
        q90 = float(atr_clean.rolling(roll_size).quantile(0.90).iloc[-1])
        if atr_v > q90:
            vol_regime = "vol_spike"
        elif atr_v > q75:
            vol_regime = "high_vol"
        elif atr_v < q25:
            vol_regime = "low_vol"

    # ── Step 4: Volume ──────────────────────────────────────────────
    obv_s = _obv(close, volume)
    vwap_s = _vwap(close, volume, 20)

    obv_mean = obv_s.rolling(14).mean()
    obv_last = float(obv_s.iloc[-1])
    obv_mean_last = float(obv_mean.iloc[-1]) if not np.isnan(obv_mean.iloc[-1]) else obv_last
    obv_chg = (obv_last - obv_mean_last) / (abs(obv_mean_last) + 1e-10)
    obv_trend = "rising" if obv_chg > 0.02 else "falling" if obv_chg < -0.02 else "flat"

    vol20_mean = float(volume.rolling(20).mean().iloc[-1])
    vol_ratio = float(volume.iloc[-1] / vol20_mean) if vol20_mean > 0 else 1.0
    vol_spike = vol_ratio > 2.0
    vwap_v = float(vwap_s.iloc[-1]) if not np.isnan(vwap_s.iloc[-1]) else price
    price_vs_vwap = "above" if price > vwap_v else "below"

    # ── Step 5: Market structure ────────────────────────────────────
    res20 = float(high.rolling(20).max().iloc[-1])
    sup20 = float(low.rolling(20).min().iloc[-1])
    res50 = float(high.rolling(min(50, len(high))).max().iloc[-1])
    sup50 = float(low.rolling(min(50, len(low))).min().iloc[-1])
    dist_res = round((res20 - price) / price * 100, 3) if price else 0.0
    dist_sup = round((price - sup20) / price * 100, 3) if price else 0.0
    swing = _swing_structure(high, low, 20)
    pivots = _pivot_points(float(high.iloc[-2]), float(low.iloc[-2]), float(close.iloc[-2]))

    # ── Step 6: Candle patterns ─────────────────────────────────────
    patterns = _candle_patterns(df)

    # ── Step 7: Weekly HTF bias (Gap 3 partial) ─────────────────────
    weekly_bias = None
    try:
        df_indexed = df.copy()
        if not isinstance(df_indexed.index, pd.DatetimeIndex):
            df_indexed = df_indexed.set_index("timestamp")
        weekly_close = df_indexed["close"].resample("W").last().dropna()
        if len(weekly_close) >= 10:
            w_ema21 = _ema(weekly_close, min(21, len(weekly_close)))
            w_rsi = _rsi(weekly_close, min(10, len(weekly_close) - 1))
            w_price = float(weekly_close.iloc[-1])
            w_ema21_v = float(w_ema21.iloc[-1])
            w_rsi_v = float(w_rsi.iloc[-1]) if not np.isnan(w_rsi.iloc[-1]) else 50.0
            if w_price > w_ema21_v and w_rsi_v > 50:
                weekly_bias = "bull"
            elif w_price < w_ema21_v and w_rsi_v < 50:
                weekly_bias = "bear"
            else:
                weekly_bias = "neutral"
    except Exception:
        pass

    # ── Step 8: BTC relative strength (Gap 8) ───────────────────────
    rs_vs_btc = None
    if btc_df is not None and token.upper() not in ("BTC", "WBTC") and len(btc_df) >= 30:
        try:
            token_ret = float(close.iloc[-1] / close.iloc[-30]) - 1
            btc_ret = float(btc_df["close"].iloc[-1] / btc_df["close"].iloc[-30]) - 1
            rs_vs_btc = round(token_ret - btc_ret, 4)
        except Exception:
            pass

    # ── Step 9: Signal scoring (Gap 5) ──────────────────────────────
    scoring_inputs = dict(
        price_vs_200ema=vs_200,
        ema_aligned_bull=ema_bull,
        ema_aligned_bear=ema_bear,
        rsi=rsi_v,
        macd_crossover=crossover,
        macd_histogram=macd_hist_v,
        volume_ratio=vol_ratio,
        obv_trend=obv_trend,
        adx=adx_v,
        vol_regime=vol_regime,
        weekly_bias=weekly_bias,
        rs_vs_btc_30d=rs_vs_btc,
    )
    signal_score, bias, conviction, conflicts = _score_signals(scoring_inputs)

    # Regime warning for LLM prompt
    if trend_regime == "ranging":
        regime_warning = "Ranging market (ADX<20) — apply mean-reversion logic, not trend-following"
    elif vol_regime == "vol_spike":
        regime_warning = "Volatility spike detected — reduce conviction and position sizing on all signals"
    elif squeeze:
        regime_warning = "Bollinger Band squeeze — breakout imminent, direction undetermined; wait for expansion"
    else:
        regime_warning = None

    # ── Assemble output ──────────────────────────────────────────────
    result = dict(
        token=token,
        price=round(price, 6),
        adaptive_params=dict(p),

        # Trend
        ema_8=round(ema8_v, 6),
        ema_21=round(ema21_v, 6),
        ema_50=round(ema50_v, 6),
        ema_200=round(ema200_v, 6),
        ema_aligned_bull=ema_bull,
        ema_aligned_bear=ema_bear,
        price_vs_200ema=vs_200,
        adx=round(adx_v, 2),
        plus_di=round(plus_di_v, 2),
        minus_di=round(minus_di_v, 2),
        trend_regime=trend_regime,
        swing_structure=swing,

        # Momentum
        rsi_14=round(rsi_v, 2),
        rsi_7=round(rsi7_v, 2),
        stoch_rsi_k=round(stoch_k_v, 2),
        stoch_rsi_d=round(stoch_d_v, 2),
        macd_line=round(macd_v, 6),
        macd_signal=round(macd_sig_v, 6),
        macd_histogram=round(macd_hist_v, 6),
        macd_crossover=crossover,
        roc_14=round(roc14_v, 2),
        momentum_regime=mom_regime,

        # Volatility
        atr_14=round(atr_v, 6),
        atr_pct=atr_pct_v,
        hist_vol_30d=round(hv30, 2),
        bb_upper=round(bb_up_v, 6),
        bb_mid=round(bb_mid_v, 6),
        bb_lower=round(bb_lo_v, 6),
        bb_width=round(bb_w_v, 4),
        bb_pct_b=round(bb_pct_v, 4),
        bb_squeeze=squeeze,
        vol_regime=vol_regime,

        # Volume
        volume_ratio=round(vol_ratio, 3),
        volume_spike=vol_spike,
        obv_trend=obv_trend,
        vwap_20d=round(vwap_v, 6),
        price_vs_vwap=price_vs_vwap,

        # Market structure
        support_20=round(sup20, 6),
        resistance_20=round(res20, 6),
        support_50=round(sup50, 6),
        resistance_50=round(res50, 6),
        dist_to_resistance_pct=dist_res,
        dist_to_support_pct=dist_sup,
        pivot_point=round(pivots["pivot"], 6),
        pivot_r1=round(pivots["r1"], 6),
        pivot_r2=round(pivots["r2"], 6),
        pivot_s1=round(pivots["s1"], 6),
        pivot_s2=round(pivots["s2"], 6),

        # Candle patterns
        candle_patterns=patterns,

        # Multi-timeframe (Gap 3)
        weekly_bias=weekly_bias,

        # BTC relative strength (Gap 8)
        rs_vs_btc_30d=rs_vs_btc,

        # Pre-computed signal resolution (Gap 5)
        signal_score=signal_score,
        signal_bias=bias,
        conviction=conviction,
        conflicting_signals=conflicts,
        regime_warning=regime_warning,

        data_bars_used=len(df),
        ema200_reliable=len(df) >= 250,
    )
    return result
