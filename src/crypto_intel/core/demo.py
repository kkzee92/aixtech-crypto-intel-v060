"""Simple paper-only demo. Research only."""
from crypto_intel.strategies.asset_class import score_signal
from crypto_intel.security.redact import redact

def run_demo():
    print("AIxTech crypto intel v0.60 — paper-only research demo")
    factors = {
        "strength": 0.72,
        "vol_tier": 0.4,
        "vol_forecast": 0.45,
        "anomaly": 0.2,
        "isolation": 0.1,
        "correlation": 0.3,
        "confidence": 0.68,
        "liquidity": 0.75,
        "fib_align": 0.8,
        "elliott_phase": "impulse",
        "mvrv": 1.8,
        "residual": 0.3,
        "beta": 1.1,
    }
    score = score_signal("major", "trend", factors)
    print(f"Sample major score: {score}")
    sample = "API key: binance_api_key=abc123 and mnemonic word1 word2 ... word12"
    print("Redacted:", redact(sample))
    print("Done. No live trading performed.")

if __name__ == "__main__":
    run_demo()
