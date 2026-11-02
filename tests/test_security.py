from crypto_intel.security.redact import redact

def test_redact_key():
    text = "secret binance_api_key=xyz123"
    assert "[REDACTED]" in redact(text)
