# AIxTech crypto intel v0.60: paper-only trading information system

Research harness for automated cryptocurrency **information** and paper strategy evaluation. Does not place live orders, does not store exchange secrets, and is not financial advice.

Builds on [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) secure AI-agent practices and prior kkzee92 versions (up to v0.59).

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.60.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.60

- Refined multi-factor strategies per asset class: adaptive EMA/ATR/Supertrend/Ichimoku/BB/Keltner/VWAP/MACD/Stochastic/Heikin-Ashi/Parabolic SAR/Donchian/GARCH-style + EWMA + realized vol forecast proxies, Fibonacci, Elliott wave proxy, options skew/gamma/vanna/volga, funding-rate dynamics + basis, expanded on-chain (volume-flow, active-address, whale, smart-money, exchange inflow/outflow, netflow, OI change, liquidation heat, order-flow imbalance, liquidity depth, MVRV, SOPR, realized-cap, exchange reserve change, NVTS proxy, Puell Multiple proxy), DEX LP depth + IL + fee yield, volatility clustering + ATR percentile + realized vol forecast + term structure, multi-horizon consistency, RSI/MACD/Stoch/Heikin/CCI/Williams %R/MFI divergence, regime clustering simulation (k-means + HMM-style + GMM proxy + transition probability + LOF + DBSCAN proxy), volume profile/delta/POC, relative strength z-score, adaptive Kelly-like + risk-parity + CVaR + max-drawdown research sizing, synthetic social volume + sentiment proxy.
- Portfolio-level adaptive correlation matrix + isolation risk gate with dynamic vol-scaled, forecast-adjusted, risk-parity, CVaR, and Kelly proxy sizing under high vol/anomaly/correlation/isolation/cluster regimes. Added multi-asset beta and residual risk filters.
- Strengthened zero-trust cyber/data security architecture: expanded redaction (BIP39, WIF, PEM, AWS, GitHub PATs, high-entropy, Solana, session tokens, hardware wallet exports, partial seeds, quantum mentions, exchange API key patterns including Binance/Bybit/OKX/KuCoin/Gate/MEXC formats, JWT, private key hex, Telegram/Discord bot tokens, more base58/hex variants, seed checksums, exchange-specific key formats, hardware serials, API secret fragments, ChaCha20 key mentions, SSH private keys, mnemonic phrases with checksum, encrypted wallet JSON fragments), sealed multi-hash lineage (SHA-256 + SHA3-256 + BLAKE2b + SHA512 + SHA3-512 + BLAKE3 proxy + SHA3-384 + SHAKE128 proxy + SHAKE256 proxy), entropy scoring, isolation forest-style + LOF + autoencoder residual + one-class SVM proxy + DBSCAN anomaly, residency stamps, consecutive-action counters, source attestation, continuous verification proxies, PDPA-style tripwire, feed integrity checks, Merkle-style subtree seals with monotonic counter, quantum-safe hash mentions, continuous attestation, and data residency compliance stamps.
- Nine asset classes with refined playbooks, risk caps, class-specific cost models, confidence floors, and adaptive horizon. Added explicit beta and residual risk overlays.
- Research only; synthetic fixtures recommended. AI-agent harness friendly with CI gates (lint, tests, secret scan style).

See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) and [docs/security-architecture.md](docs/security-architecture.md).

## What it does

- Classifies into nine asset classes with enhanced multi-factor research rules.
- Labels regime (trend/range/stress) + volatility tier + forecast + anomaly score + correlation regime + cluster + isolation + relative strength + risk parity + CVaR proxy + fib/elliott/options/on-chain advanced + beta/residual.
- Scores signal then multi-gate risk (class caps, confidence, correlation, anomaly, isolation, drawdown, kill switch, vol scaling + forecast + risk-parity + CVaR + beta).
- Paper fills with class costs; hash-chained audit with multi-hash sealed lineage.
- No live execution, no secret storage.

| Asset class | Enhanced research rule | Risk cap | Cost |
|---|---|---|---|
| Major | Adaptive multi-factor EMA + Supertrend + Ichimoku + BB + Keltner + VWAP + MACD + Heikin-Ashi + SAR + Donchian + GARCH/EWMA/realized vol + Fib/Elliott + options skew/gamma + funding/basis/on-chain/OI/order-flow/liquidity/MVRV/SOPR/reserve/NVTS/Puell proxies + correlation/beta-adjusted outside stress | 8% | 8 bps |
| Large-cap alt | Volume-profile/POC breakout + VWAP + MACD + multi-TF + relative strength z-score vs major + correlation/beta filter + regime cluster + volume delta + netflow + OI + order-flow + Fib + DEX LP + CCI + residual | 4% | 14 bps |
| Stablecoin | Adaptive peg deviation (15-50 bps) with volume confirmation + netflow + liquidity depth + SOPR proxy + residual | 0% | n/a |
| DeFi | Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity/smart-money proxy + isolation check + risk-parity + CVaR + LP depth/IL/fee + Williams %R + residual | 2% | 22 bps |
| Meme | Qualified burst + StochRSI + consistency + hard horizon + volume-flow decay + anomaly filter + residual + liq heat + order-flow + social synthetic + Fib + CCI + beta | 0.5% | 45 bps |
| L2 | Relative strength + MACD vs benchmark + adaptive MTF + correlation confirmation + cluster + vol forecast + transition + Elliott proxy + residual | 3% | 16 bps |
| RWA | Slow multi-scale + gap/anomaly halt + volume filter + isolation + forecast + CVaR + realized-cap + NVTS + residual | 2% | 12 bps |
| Perpetual | Negative funding carry + contained drift + low anomaly + funding flip alert + correlation + residual + OI + order-flow + gamma/vanna proxy + reserve change + basis | 2% | 10 bps |
| AI-token | Hybrid burst + activity proxy + divergence + low isolation; strict horizon + smart-money + OI + transition + options vanna + social + residual | 1% | 30 bps |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m crypto_intel.demo
PYTHONPATH=src pytest tests/ -q
```

## Controls

Paper-only mode guard. No trade keys. Class caps, confidence floors, kill switch, drawdown, correlation, anomaly, isolation, beta gates. Hash-chained audit + sealed multi-hash lineage. Expanded redaction. PDPA-style tripwire. gitleaks and lint in CI recommended.

## Honesty

No live connector included. Strategy scores describe synthetic data. Not financial, legal, or compliance advice. Research only.
