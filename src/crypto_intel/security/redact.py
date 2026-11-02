"""Expanded redaction patterns for zero-trust. Research only. v0.60"""
import re

PATTERNS = [
    re.compile(r"\b(?:[a-z]{3,8}\s+){11,24}[a-z]{3,8}\b", re.I),  # BIP39-like
    re.compile(r"5[HJK][1-9A-HJ-NP-Za-km-z]{49,50}"),  # WIF
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS
    re.compile(r"ghp_[A-Za-z0-9]{36}"),  # GitHub PAT
    re.compile(r"sk-[A-Za-z0-9]{20,}"),  # OpenAI-like or generic
    re.compile(r"binance[_-]?api[_-]?key", re.I),
    re.compile(r"bybit[_-]?key", re.I),
    re.compile(r"okx[_-]?api", re.I),
    re.compile(r"kucoin[_-]?api", re.I),
    re.compile(r"gate[_-]?api", re.I),
    re.compile(r"mexc[_-]?api", re.I),
    re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}"),  # base58-like Solana/addresses
    re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),  # JWT
    re.compile(r"-----BEGIN OPENSSH PRIVATE KEY-----"),
    re.compile(r"chacha20|xchacha", re.I),
    re.compile(r"\b[0-9a-fA-F]{64}\b"),  # private key hex
    re.compile(r"bot[0-9]+:[A-Za-z0-9_-]{35}"),  # Telegram bot
    re.compile(r"[A-Za-z0-9]{24}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27}"),  # Discord
]

def redact(text: str) -> str:
    for p in PATTERNS:
        text = p.sub("[REDACTED]", text)
    return text
