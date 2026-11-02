from crypto_intel.strategies.asset_class import score_signal

def test_score_stress():
    assert score_signal("major", "stress", {"strength": 0.9}) == 0.0

def test_score_basic():
    factors = {"strength": 0.7, "vol_tier": 0.3, "anomaly": 0.1, "confidence": 0.6}
    s = score_signal("major", "trend", factors)
    assert 0 < s <= 0.08
