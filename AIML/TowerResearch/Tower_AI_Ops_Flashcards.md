# Flashcards — LLM Pricing, Concepts & Numbers to Memorize

> Drill these until they're automatic. Cover the right column, recall, uncover, repeat.
> Pricing is directional and changes frequently — verify on official pricing pages the day before your interview. Numbers below reflect publicly listed pricing as of mid-2026; ratios and structure matter more than exact cents.

---

## Section 1 — Per-Million-Token Prices (USD)

### OpenAI

| Model | Input $/1M | Cached Input $/1M | Output $/1M |
|---|---|---|---|
| GPT-4o | $2.50 | $1.25 | $10.00 |
| GPT-4o-mini | $0.15 | $0.075 | $0.60 |
| GPT-4.1 | $2.00 | $0.50 | $8.00 |
| GPT-4.1-mini | $0.40 | $0.10 | $1.60 |
| GPT-4.1-nano | $0.10 | $0.025 | $0.40 |
| o3 | $2.00 | $0.50 | $8.00 |
| o3-mini | $1.10 | $0.55 | $4.40 |
| o4-mini | $1.10 | $0.275 | $4.40 |
| text-embedding-3-small | $0.02 | — | — |
| text-embedding-3-large | $0.13 | — | — |

**Key ratios to memorize:**
- Output is roughly **4x input** on flagship models.
- Cached input is **50% off** (OpenAI auto-cache) up to **75% off** on some tiers.
- Batch API: **50% off** input AND output, 24h SLA.

### Anthropic (Claude)

| Model | Input $/1M | Cache Write $/1M | Cache Read $/1M | Output $/1M |
|---|---|---|---|---|
| Claude Opus 4 | $15 | $18.75 | $1.50 | $75 |
| Claude Sonnet 4 | $3 | $3.75 | $0.30 | $15 |
| Claude Haiku 4 | $0.80 | $1.00 | $0.08 | $4 |

**Key ratios:**
- Output is **5x input**.
- Cache write costs **25% more** than input (one-time penalty).
- Cache read costs **10% of input** (90% discount on hits).
- Batch API: **50% off**.
- Cache TTL: **5 min default**, **1 hour extended** (extra cost on write).

### Google (Gemini via API)

| Model | Input $/1M | Output $/1M |
|---|---|---|
| Gemini 2.5 Pro | $1.25 (≤200K) / $2.50 (>200K) | $10 / $15 |
| Gemini 2.5 Flash | $0.30 | $2.50 |
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 |

**Note:** Context-window-dependent pricing — bigger context = higher rate.

### AWS Bedrock (relative — same models, AWS markup is typically near-parity)

- Claude models on Bedrock: **same price** as Anthropic direct in most regions; check region-specific pricing.
- Amazon Nova Pro / Lite / Micro: cheaper than Claude equivalents (Nova Micro ~$0.035 input).
- Llama 3.x via Bedrock: variable; usually competitive.
- **Provisioned Throughput**: hourly rate per model unit; 1-month and 6-month commitments offer ~20–40% effective discount IF saturated.

---

## Section 2 — Cost Math (memorize the formula)

### Standard inference cost
```
cost = (input_tokens / 1,000,000) × input_price
     + (output_tokens / 1,000,000) × output_price
```

### With prompt caching (Anthropic)
```
cost = (cache_write_tokens / 1M) × cache_write_price        ← first call only
     + (cache_read_tokens / 1M) × cache_read_price          ← subsequent calls
     + (non_cached_input_tokens / 1M) × input_price
     + (output_tokens / 1M) × output_price
```

### Break-even for prompt caching (Anthropic)
Cache write = 1.25× input; cache read = 0.10× input.
Net savings per hit = `input - cache_read` = 0.90× input.
Break-even: `0.25× input (extra write cost) / 0.90× input (savings per hit)` ≈ **0.28 hits**.
Translation: **you only need 1 cache hit to be net positive**. With 2+ hits per TTL, caching is a no-brainer.

### Worked example (do this in your head)
> 50,000 calls/day. 6K input + 800 output. Claude Sonnet 4.
> Input cost: 50,000 × 6,000 / 1M × $3 = 50,000 × 0.006 × $3 = **$900**
> Output cost: 50,000 × 800 / 1M × $15 = 50,000 × 0.0008 × $15 = **$600**
> Daily total: **$1,500** → annual ≈ **$550K**

> Now add caching on a 5K stable system prompt, 80% cache-hit rate:
> Cached portion savings: 0.80 × 50,000 × 5,000 / 1M × ($3 − $0.30) = **$540/day**
> Annual savings: **~$197K** (-36%)

---

## Section 3 — Concept Flashcards

| Term | One-line definition |
|---|---|
| **Token** | The atomic billing unit. ~4 chars / ~0.75 words English. Different tokenizers per provider. |
| **Context window** | Max tokens in a single request (input + output). 200K (Claude), 128K-1M (GPT-4 family), 1M-2M (Gemini). |
| **TTFT** | Time To First Token — latency until streaming starts. |
| **TPOT / TPS** | Tokens Per Output Token / Tokens Per Second — generation throughput. |
| **Prompt caching** | Provider stores KV-cache of prompt prefix; cache reads ~10% of input price. |
| **Batch API** | Async batch processing, 50% discount, 24h SLA. |
| **Provisioned Throughput (PT)** | Reserved capacity, $/hour, no per-token charge within capacity. |
| **PTU (Azure)** | Azure's name for provisioned throughput on OpenAI models. |
| **Model unit** | Bedrock's unit of provisioned capacity. |
| **Fine-tuning** | Train a model on your data; cheaper inference, narrower scope. |
| **Distillation** | Train a small model on a large model's outputs. |
| **RAG** | Retrieval-Augmented Generation — retrieve relevant docs, inject into prompt. |
| **Embeddings** | Vector representation of text used for semantic search/retrieval. |
| **Function calling / tool use** | Model returns structured calls to your code; reduces output tokens. |
| **Structured output** | JSON-schema-constrained output; tighter, no parse errors, fewer retries. |
| **Guardrails** | Pre/post filters on prompts and outputs (Bedrock Guardrails, NeMo Guardrails). |
| **Inference profile** | Bedrock construct that tags every call for cost attribution. |
| **Application Inference Profile** | Custom Bedrock profile with your own tags, surfaces in CUR. |
| **Cost Allocation Tags** | AWS tags that activate in CUR for chargeback. |
| **CUR** | AWS Cost and Usage Report — granular billing in S3. |
| **AWS Budgets** | AWS service for budget alerts and actions. |
| **Cost Anomaly Detection** | AWS ML-based spike detection on spend. |
| **Showback** | Visibility into team-level costs without internal billing. |
| **Chargeback** | Actual internal billing of consumed resources. |
| **Unit economics** | $/successful-task, $/active-user, $/business-outcome. |
| **Model routing** | Send each request to the cheapest model that can handle it. |
| **Semantic caching** | Cache LLM responses keyed by embedding similarity, not exact match. |
| **Token-level streaming** | Stream tokens as generated — same total cost, better UX. |

---

## Section 4 — FinOps Lifecycle Flashcards

| Phase | Activities | Tower-specific examples |
|---|---|---|
| **Inform** | Visibility, allocation, budgeting, forecasting, benchmarking | Tag every API call; per-desk and per-project dashboards; weekly variance report |
| **Optimize** | Rightsizing, commitments, eliminate waste, automation | Model routing; prompt caching; batch API; PT for predictable loads; kill orphan keys |
| **Operate** | Define policies, automate enforcement, continuous improvement | Governance docs; budget gates in CI; auto-throttle on overage; quarterly vendor reviews |

---

## Section 5 — Vendor / Contract Flashcards

| Term | One-line |
|---|---|
| **EDP (Enterprise Discount Program)** | AWS multi-year committed spend for blended discounts. |
| **Committed spend** | Promise X annual $ for Y% discount. |
| **Rate card** | Negotiated per-unit prices replacing list price. |
| **Burst pricing** | Higher rate above committed capacity. |
| **Price protection clause** | Your rate auto-adjusts if list price drops. |
| **MFN clause** | "Most Favored Nation" — you get the best price offered to similar customers. |
| **Zero data retention (ZDR)** | Provider doesn't store prompts/outputs; required for sensitive data. |
| **No training on inputs** | Provider can't use your data to train models. |
| **IP indemnification** | Provider covers you legally if model output infringes copyright. |
| **Sub-processor list** | Third parties the vendor uses; must be approved. |
| **Audit rights** | Your right to audit vendor controls (SOC2, ISO 27001). |
| **SLA** | Uptime, latency, support response time commitments. |
| **Service credits** | Money back when SLA missed. |

---

## Section 6 — Tower-Specific Flashcards

| Topic | Key point |
|---|---|
| **Firm type** | Proprietary quantitative trading firm — trades own capital. |
| **Founded** | 1998 by Mark Gorton. |
| **HQ** | Equitable Building, NYC Financial District. |
| **Trading style** | High-frequency / low-latency systematic. |
| **Tech edge** | FPGA, hardware acceleration, low-latency C++, ML. |
| **Org structure** | Pod model — independent PMs + central platform teams. |
| **Your group** | Core AI & ML — central platform for AI tooling across the firm. |
| **Your boss** | Global Head of Core AI & ML. |
| **Your peers** | Eng, Procurement, Finance, Trading PMs, Compliance. |
| **Why this role now** | LLM spend has scaled from $0 to material in 18 months and needs governance. |
| **Cultural code** | "Smart, driven, no ego, no unnecessary hierarchy." |

---

## Quick-recall drill (run this in 5 minutes)

1. Claude Sonnet 4 input/output per million? → **$3 / $15**
2. GPT-4o input/output per million? → **$2.50 / $10**
3. Anthropic cache read discount? → **90% off input** (~10% of input price)
4. Anthropic cache write penalty? → **+25% over input** (one-time per write)
5. Batch API discount (both OpenAI and Anthropic)? → **50%**
6. Batch API SLA? → **24 hours**
7. Bedrock attribution mechanism? → **Application Inference Profiles + Cost Allocation Tags → CUR**
8. FinOps lifecycle? → **Inform → Optimize → Operate**
9. Showback vs Chargeback? → **Visibility vs Real billing**
10. Best signal for "is caching worth it"? → **2+ hits per cache TTL**
11. Best signal for "is PT worth it"? → **~60%+ sustained utilization**
12. Tower's trading model? → **Prop, systematic, low-latency, pod-based**
13. Output tokens cost ratio? → **3–5x input**
14. Tower founder & year? → **Mark Gorton, 1998**
15. Top 3 vendor levers? → **Committed spend, multi-vendor leverage, price-protection clause**

If you can answer all 15 in under 3 minutes, you're ready.
