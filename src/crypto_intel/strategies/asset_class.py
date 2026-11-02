"""Asset-class specific research strategies (paper-only). v0.60 refinements."""

ASSET_CLASSES = {
    "major": {"risk_cap": 0.08, "cost_bps": 8, "confidence_floor": 0.55},
    "large_alt": {"risk_cap": 0.04, "cost_bps": 14, "confidence_floor": 0.60},
    "stable": {"risk_cap": 0.0, "cost_bps": 0, "confidence_floor": 0.0},
    "defi": {"risk_cap": 0.02, "cost_bps": 22, "confidence_floor": 0.65},
    "meme": {"risk_cap": 0.005, "cost_bps": 45, "confidence_floor": 0.70},
    "l2": {"risk_cap": 0.03, "cost_bps": 16, "confidence_floor": 0.58},
    "rwa": {"risk_cap": 0.02, "cost_bps": 12, "confidence_floor": 0.60},
    "perp": {"risk_cap": 0.02, "cost_bps": 10, "confidence_floor": 0.55},
    "ai_token": {"risk_cap": 0.01, "cost_bps": 30, "confidence_floor": 0.68},
}

def score_signal(asset_class: str, regime: str, factors: dict) -> float:
    """Multi-factor score with vol/anomaly/correlation/isolation/forecast/risk-parity/CVaR/order-flow/fib/elliott/options/on-chain/CCI/Williams/beta/residual adjustments. Research only."""
    if regime == "stress" or factors.get("anomaly", 0) > 0.75 or factors.get("isolation", 0) > 0.8:
        return 0.0
    base = factors.get("strength", 0.5)
    # Volatility scaling + forecast (GARCH/EWMA/realized proxy)
    vol = factors.get("vol_tier", 0.5)
    vol_forecast = factors.get("vol_forecast", vol)
    if max(vol, vol_forecast) > 0.7:
        base *= 0.55
    # Correlation and beta penalty for alts/meme
    if asset_class in ("large_alt", "meme", "ai_token") and (factors.get("correlation", 0) > 0.6 or factors.get("beta", 1.0) > 1.5):
        base *= 0.65
    # Isolation forest-style + LOF + residual + liq heat + order-flow + CCI/Williams extremes + DBSCAN
    if (factors.get("isolation", 0) > 0.5 or factors.get("lof", 0) > 0.6 or factors.get("residual", 0) > 0.6 or
        factors.get("liq_heat", 0) > 0.7 or factors.get("order_flow", 0) > 0.8 or factors.get("cci", 0) > 200 or
        factors.get("williams", -50) < -80 or factors.get("dbscan", 0) > 0.7):
        base *= 0.7
    # OI change proxy
    if factors.get("oi_change", 0) > 0.8 and asset_class in ("perp", "ai_token"):
        base *= 0.75
    # Adaptive sizing proxy (Kelly-like + risk-parity + CVaR + maxDD research)
    if (factors.get("confidence", base) < 0.5 or factors.get("risk_parity", 1.0) < 0.6 or
        factors.get("cvar", 1.0) < 0.5 or factors.get("max_dd", 0) > 0.15):
        base *= 0.8
    # Liquidity depth boost for majors
    if asset_class == "major" and factors.get("liquidity", 0) > 0.6:
        base *= 1.05
    # Fib / Elliott / options proxies
    if factors.get("fib_align", 0) > 0.7:
        base *= 1.03
    if factors.get("elliott_phase", "") == "impulse" and asset_class in ("major", "l2"):
        base *= 1.04
    if factors.get("options_skew", 0) > 0.6 and asset_class == "perp":
        base *= 0.9
    if factors.get("options_vanna", 0) > 0.5 and asset_class == "ai_token":
        base *= 0.95
    # Advanced on-chain including reserve change, NVTS, Puell
    if (factors.get("mvrv", 1.0) > 2.5 or factors.get("sopr", 1.0) > 1.1 or factors.get("reserve_change", 0) > 0.5 or
        factors.get("nvts", 100) > 150 or factors.get("puell", 1.0) > 2.0):
        base *= 0.85
    # Residual risk filter
    if factors.get("residual", 0) > 0.65:
        base *= 0.75
    cfg = ASSET_CLASSES.get(asset_class, {})
    score = min(base, cfg.get("risk_cap", 0.0))
    if score < cfg.get("confidence_floor", 0.0):
        return 0.0
    return round(score, 4)
