# Security architecture (v0.60)

Zero-trust research design for paper-only crypto information system. No live keys, no order execution.

## Controls
- Expanded redaction patterns covering BIP39, WIF, PEM, AWS, GitHub PATs, exchange keys (Binance/Bybit/OKX/KuCoin/Gate/MEXC), JWT, private key hex, Telegram/Discord tokens, SSH keys, ChaCha20, high-entropy strings, hardware wallet exports, partial seeds, quantum mentions.
- Sealed multi-hash lineage: SHA-256, SHA3-256, BLAKE2b, SHA512, SHA3-512, BLAKE3 proxy, SHA3-384, SHAKE128/256 proxies, with monotonic counters and Merkle-style subtree seals.
- Anomaly detection proxies: isolation forest-style, LOF, autoencoder residual, one-class SVM, DBSCAN.
- Continuous attestation, source attestation, residency stamps, consecutive-action counters, PDPA-style tripwire, feed integrity checks, data residency compliance stamps.
- Entropy scoring, kill switches, confidence floors, class risk caps, correlation/beta/isolation/anomaly gates.

## Principles
- No secret storage. All sensitive patterns redacted before any logging or processing.
- Paper-only mode enforced. Synthetic data recommended.
- Audit trail with hash-chained multi-hash seals.
- AI-agent harness friendly: CI gates for lint, tests, secret scanning.

Research only. Not production security advice.
