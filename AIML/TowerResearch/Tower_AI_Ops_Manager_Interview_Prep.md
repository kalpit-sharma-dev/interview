# Tower Research Capital — AI Operations Manager
## End-to-End Interview Preparation Guide

> **Role:** AI Operations Manager, Core AI & Machine Learning Group
> **Reports to:** Global Head of Core AI & ML
> **Location:** Gurgaon (with global stakeholders)
> **Candidate:** Kalpit

---

## Table of Contents

1. [Understand the Company (Tower Research Capital)](#1-understand-the-company)
2. [Decoding the Job Description](#2-decoding-the-jd)
3. [Core Knowledge Domains You MUST Master](#3-core-knowledge-domains)
   - 3.1 FinOps for AI / AI Cost Management
   - 3.2 LLM Pricing & Token Economics
   - 3.3 AI Platforms & Providers (OpenAI, Anthropic, Bedrock, Cursor)
   - 3.4 Orchestration Frameworks (LangChain, LangGraph)
   - 3.5 Observability & Inventory (LangSmith, Langfuse, Helicone)
   - 3.6 Cloud Billing (AWS Cost Explorer, CUR, Bedrock pricing)
   - 3.7 Vendor Contracting & Procurement Levers
   - 3.8 Governance, Controls & Chargeback
   - 3.9 Hedge Fund / Prop Trading Context
4. [Frameworks to Speak Fluently](#4-frameworks)
5. [Likely Interview Questions + Model Answers](#5-questions-and-answers)
6. [Behavioral / Leadership Prep (STAR)](#6-behavioral)
7. [Case Studies / Whiteboard Exercises](#7-case-studies)
8. [Questions YOU Should Ask the Interviewers](#8-questions-to-ask)
9. [7-Day Study Plan](#9-study-plan)
10. [Final Checklist & Day-of Tips](#10-final-checklist)

---

## 1. Understand the Company

### Tower Research Capital — Snapshot
- **Founded:** 1998 by Mark Gorton.
- **Type:** Proprietary (prop) quantitative trading firm — trades the firm's own capital, not client money.
- **HQ:** Equitable Building, NYC Financial District. Global footprint with 10+ offices (Gurgaon, London, Singapore, Amsterdam, Chicago, etc.).
- **Strategy:** High-frequency / low-latency systematic trading across asset classes (equities, futures, FX, options).
- **Tech edge:** FPGA, hardware acceleration, low-latency C++, ML, co-located infrastructure.
- **Structure:** "Pod" model — independent portfolio managers / trading teams supported by central infrastructure (Core AI/ML, Engineering, Business Support).
- **Affiliates:** Latour Trading (US market-making affiliate).

### Why this matters for the interview
- This is a **buy-side prop firm**, not a sell-side bank or vendor. They eat their own P&L.
- Every dollar of cost — including AI/LLM spend — is a direct hit to firm profitability. So cost discipline is religion.
- They value **engineers and quants who think like owners**. Your role exists because LLM spend has become material and unmanaged.
- Culture: "smart, driven, no ego, no unnecessary hierarchy" — be confident but humble; collaborative; direct.

### Core AI & ML Group context
- A central platform team that provides LLM access, AI tooling, and ML infrastructure to trading desks, quant research, engineering, compliance, ops, etc.
- They likely run a mix of:
  - **External LLM APIs** (OpenAI, Anthropic, Google, etc.)
  - **AWS Bedrock** (managed multi-model gateway)
  - **Internal / self-hosted models** (likely on GPU clusters for sensitive workloads)
  - **Developer tools** (Cursor, GitHub Copilot, etc.)
  - **Orchestration** (LangChain / LangGraph / custom)

---

## 2. Decoding the JD

Map each JD bullet to a concrete capability you can talk about:

| JD Phrase | What they actually want |
|---|---|
| "Token management, cost attribution, chargeback" | Build a system that tags every API call (team/project/user/model) and bills internal teams back. Like AWS chargeback but for LLM tokens. |
| "Implementing robust tracking and tagging" | Metadata standards (OpenAI `user`/`metadata`, Anthropic `metadata.user_id`, custom proxy headers, LangSmith tags). |
| "AI cost strategies and governance policies" | Budgets, quotas, rate limits, model-tier policies (don't use GPT-4o for grep). |
| "Token-based pricing trends" | You track price drops (Anthropic Haiku, GPT-4o-mini, Gemini Flash, prompt caching, batch API discounts) and re-optimize. |
| "Comprehensive financial reports" | Dashboards: $/team, $/project, $/use-case, $/token, $/successful-request, $/developer. |
| "Drive cost-efficiency use cases" | Embed with trading/eng teams; redesign prompts, switch models, add caching, batch where latency allows. |
| "Negotiate contracts, commercials, committed-use discounts" | Enterprise agreements, PTUs (Provisioned Throughput Units), volume discounts, Bedrock commitments. |
| "Model routing and prompt optimization" | Route cheap queries to cheap models; semantic caching; prompt compression. |
| "L1 escalation point" | You own AI ops incidents — outages, rate-limit breaches, runaway agents, prompt-injection cost attacks. |
| "Buy-side institutions background" | They want someone who has worked at a hedge fund / prop shop / bank trading floor and understands urgency, confidentiality, P&L culture. |

---

## 3. Core Knowledge Domains

### 3.1 FinOps for AI / AI Cost Management

**FinOps** = cultural + operational practice of running cloud (and now AI) with financial accountability.

- **FinOps Foundation framework:** *Inform → Optimize → Operate* (the lifecycle).
  - **Inform:** visibility, allocation, budgeting, forecasting.
  - **Optimize:** rightsizing, commitments, eliminate waste.
  - **Operate:** continuous improvement, policy, automation.
- **FinOps for AI specifics:**
  - Unit economics: cost per inference, cost per successful task, cost per developer per day, cost per trade signal generated.
  - "Unit cost" thinking — not just absolute $, but $/output.
  - Allocation: tag every call with team / project / cost-center / environment.
  - Showback (visibility only) vs **Chargeback** (real internal billing).

**Be ready to say:** *"I'd run AI FinOps on the same Inform → Optimize → Operate loop, but with token-aware unit economics — cost per successful task, cost per developer, cost per generated trade idea — not just raw $/month."*

### 3.2 LLM Pricing & Token Economics

**Tokens:**
- ~4 characters / ~0.75 words per token (English).
- Two prices per model: **input tokens** (cheaper) and **output tokens** (typically 3–5x input).
- Some providers add: cached input tokens (much cheaper), thinking/reasoning tokens (sometimes billed separately).

**Pricing levers you must know:**

| Lever | What it is | When to use |
|---|---|---|
| **Model tier** | GPT-4o vs GPT-4o-mini, Claude Opus vs Haiku, Gemini Pro vs Flash | Route by complexity |
| **Prompt caching** | Anthropic/OpenAI/Bedrock cache reusable prompt prefixes; 75–90% cheaper on cache hits | Long system prompts, RAG context, agent loops |
| **Batch API** | 50% discount, async (24h SLA) on OpenAI/Anthropic | Backfills, evals, non-realtime jobs |
| **Provisioned Throughput (PTU / Bedrock PT)** | Pay for reserved capacity by the hour, unlimited tokens within capacity | Predictable high-volume workloads |
| **Committed spend discounts** | Enterprise agreements with OpenAI/Anthropic, AWS EDP | High annual spend |
| **Context window weighting** | Bigger context windows cost more per call AND can be priced at premium tiers | Don't dump entire codebase if 5% is needed |
| **Fine-tuning vs prompting** | Fine-tuned smaller model can beat prompted larger model on cost+quality | Repetitive narrow tasks |
| **Distillation** | Train small model on big model's outputs | Production replacement |
| **Embeddings + RAG** | Replace giant context with retrieval | Knowledge-heavy queries |
| **Structured output / function calling** | Fewer retries, shorter responses | Anywhere parseable output is needed |

**Worked example to memorize:**
> A trading team is running 100K agent calls/day, average 8K input + 1K output tokens on Claude Sonnet (≈ $3/M input, $15/M output).
> Daily cost = 100,000 × (8,000/1M × $3 + 1,000/1M × $15) = 100,000 × ($0.024 + $0.015) = **$3,900/day ≈ $1.4M/year**.
> If 80% of those calls have a reusable 7K-token system prompt and we enable prompt caching at ~10% of input cost on cache hits:
> Savings ≈ 80% × 100,000 × 7,000/1M × $3 × 90% = **~$1,500/day ≈ $550K/year**.
> Add batch API for the 30% that's non-realtime (50% off) → another ~$300K/year.

You should be able to do this math live on a whiteboard.

### 3.3 AI Platforms & Providers

**OpenAI**
- Models: GPT-4o, GPT-4o-mini, o1/o3 (reasoning), GPT-4.1, embeddings (text-embedding-3-*), Whisper.
- Cost controls: usage tiers, project-level API keys, **usage dashboards by project/user**, monthly budgets, hard/soft limits, the `user` field for end-user attribution, Batch API, prompt caching (automatic with stable prefixes).
- Enterprise: ChatGPT Enterprise, Enterprise API agreements with committed spend, SOC2, zero data retention.

**Anthropic (Claude)**
- Models: Claude Opus, Sonnet, Haiku (tiered by capability/price).
- Features: 200K context, **prompt caching** (explicit `cache_control` markers, 5-min or 1-hour TTL), Message Batches API (50% off), tool use.
- Enterprise: Claude for Enterprise, AWS Bedrock and GCP Vertex availability.

**AWS Bedrock**
- Single API for multiple model providers (Anthropic, Meta, Cohere, Amazon Titan/Nova, AI21, Mistral).
- Pricing modes: **on-demand**, **Provisioned Throughput (PT)** — buy "model units" by hour/month/6-month.
- Cost attribution via **Application Inference Profiles** + AWS resource tags → flows into AWS Cost Explorer and CUR.
- Bedrock Guardrails, Knowledge Bases, Agents — each has its own cost line.

**Cursor (the IDE)**
- Tower likely deploys Cursor org-wide for engineers.
- Pricing: per-seat (Pro/Business) + usage-based for "MAX/Advanced" model calls.
- Cost levers: seat audits (inactive users), model selection policy (default to cheaper model), context size limits, "auto" vs "max" mode, business plan admin controls and usage dashboards, SSO + SCIM for lifecycle management.

**Other tools you may encounter:** GitHub Copilot (Business/Enterprise), Perplexity Enterprise, Glean, internal RAG platforms, vector DBs (Pinecone, Weaviate, pgvector), Hugging Face / vLLM / TGI for self-hosted.

### 3.4 Orchestration Frameworks

**LangChain**
- Python/JS framework for chaining LLM calls, tools, retrievers, memory.
- Cost relevance: each "chain step" is potentially another LLM call → cost compounds. Poorly designed chains hide cost.
- Common waste: redundant tool descriptions in every step, unbounded ReAct loops, no early exit.

**LangGraph**
- Graph-based agent orchestration from LangChain team. State machine for agents (nodes = steps, edges = transitions).
- Cost relevance: explicit graph means you can **measure cost per node** and enforce max-step limits.
- Supports human-in-the-loop, checkpointing, parallel branches.

**Talking point:** *"LangGraph's explicit state model is great for cost governance — you can attach budgets per node, hard-cap recursion, and trace per-node token usage in LangSmith. LangChain's free-form agents are flexible but prone to runaway loops."*

Other orchestration to namedrop: **LlamaIndex, Haystack, DSPy, CrewAI, Microsoft AutoGen, OpenAI Agents SDK, Anthropic's Claude Agent SDK**.

### 3.5 Observability & Inventory

| Tool | What it does | Pricing model | Notable strength |
|---|---|---|---|
| **LangSmith** | LangChain-native tracing, evals, datasets, monitoring | SaaS, per-seat + per-trace | Deep LangChain/LangGraph integration |
| **Langfuse** | Open-source LLM observability, traces, prompt mgmt, evals | OSS / self-hosted free; cloud paid | Self-hosting (data stays on-prem — important for prop firms) |
| **Helicone** | Proxy-based LLM observability, caching, rate limits | OSS + cloud | Easy drop-in proxy, built-in caching |
| **Datadog LLM Observability / New Relic AI Monitoring** | Enterprise APM extended to LLMs | Enterprise | Fits into existing infra monitoring |
| **OpenLLMetry** | OpenTelemetry standard for LLMs | OSS | Vendor-neutral |

**For Tower (a prop trading firm), self-hosting is likely preferred** for sensitive prompts → Langfuse self-hosted + an internal proxy. Be ready to discuss this trade-off.

### 3.6 Cloud Billing

**AWS Cost Explorer / CUR (Cost and Usage Report)**
- CUR = the raw, hourly, granular billing data in S3/Athena.
- Tag-based allocation: every resource gets `CostCenter`, `Team`, `Project`, `Environment`.
- Bedrock costs show up under `AWS Bedrock` service with `usage type` (input/output tokens, PT hours).
- **Application Inference Profiles** in Bedrock let you tag every inference request → flows to CUR.
- Savings Plans / Reserved Instances don't apply to Bedrock; **Bedrock Provisioned Throughput commitments do** (1-month / 6-month).
- AWS Budgets + Anomaly Detection for proactive alerts.

**Equivalent tools to name:** Azure Cost Management, GCP Billing + BigQuery export, **CloudZero, Vantage, Cloudability, Apptio** for multi-cloud + SaaS cost.

### 3.7 Vendor Contracting & Procurement Levers

You will help negotiate. Be fluent in:

- **Committed spend agreements**: annual minimum spend in exchange for X% discount.
- **Volume tiers**: price drops at $250K, $1M, $5M annual.
- **Rate cards** vs **list price** — enterprise gets discounted rate cards.
- **PTUs / Provisioned Throughput**: lower $/token but pay-for-capacity-not-usage; only wins above a utilization threshold.
- **Burst capacity / overage pricing**.
- **MSA terms that matter for AI**: data retention, training opt-out (zero data retention / no training), IP indemnification (Anthropic, OpenAI, Google now offer this), SLAs, audit rights, sub-processor list.
- **Renewal leverage**: bring a competitor quote (Anthropic vs OpenAI vs Bedrock-routed Claude), threaten to shift workload.
- **Multi-year vs annual**: multi-year = more discount but less flexibility as prices drop fast.

### 3.8 Governance, Controls & Chargeback

**Tagging standard (propose this):**
```
team: <quant-research | execution | infra | compliance | ...>
project: <project-code>
cost_center: <CC code>
environment: <prod | staging | dev>
use_case: <code-assist | research-summarization | trade-signal | ...>
user: <employee-id>
```
Enforced via: API gateway / proxy that rejects untagged calls.

**Controls hierarchy:**
1. **Preventive:** SSO, per-key budgets, model allow-lists per team, rate limits, prompt-injection guardrails.
2. **Detective:** real-time dashboards, anomaly detection (spend spike alerts), weekly variance vs budget.
3. **Corrective:** auto-throttle on overage, escalation runbooks, post-incident reviews.

**Chargeback model options:**
- **Direct passthrough** (actual usage × actual price + small ops overhead).
- **Tiered allocation** (each team gets a base allocation, overage charged back).
- **Showback only** in year 1 to build trust, then chargeback in year 2.

### 3.9 Hedge Fund / Prop Trading Context

Be ready to discuss why AI ops in a trading firm is **different from a tech company**:
- **Latency-sensitive**: many trading workloads can't use cloud LLMs at all — only batch research/back-office.
- **Confidentiality**: alpha-generating prompts and outputs are crown jewels. No data egress to public APIs without legal/compliance sign-off.
- **Regulatory**: SEC/FINRA/CFTC + global equivalents. Model risk management (SR 11-7-style). Records retention.
- **Highly skewed users**: a handful of quant researchers may drive 80% of spend.
- **Volatility**: spend can 10x during a research push or new strategy launch.
- **Information barriers**: pod-level separation; one PM's data must not leak to another's prompts.

---

## 4. Frameworks to Speak Fluently

Memorize these — they're your "vocabulary upgrade":

1. **FinOps Lifecycle**: Inform → Optimize → Operate.
2. **Unit Economics**: $/successful-task, $/user-day, $/trade-idea, $/PR-merged (for Copilot).
3. **5-Why for cost spikes**: drill from $ → tokens → calls → user → use-case → root cause.
4. **Model Routing Decision Tree**:
   - Is the task deterministic / parseable? → smaller model + structured output.
   - Does it require reasoning / multi-step? → reasoning model, but cap thinking tokens.
   - Is latency tolerant? → batch API.
   - Is the prompt prefix stable? → enable prompt caching.
   - Is volume predictable & high? → consider PTU/Bedrock PT.
5. **Build vs Buy vs Route**: self-host (capex), enterprise API (opex + leverage), multi-vendor router (flexibility + complexity).
6. **RACI for AI Ops**: who is Responsible, Accountable, Consulted, Informed for spend, incidents, contracts.
7. **TCO**: total cost of ownership — don't forget observability, proxy infra, eng time, vendor mgmt overhead.

---

## 5. Questions and Answers

### A. Role & Strategy

**Q1. Walk me through your first 90 days in this role.**

*Model answer (Situation–Plan–Outcome):*
> "Days 1–30 — **Inform**. I'd inventory every AI tool, vendor, contract, API key, and self-hosted model in use across the firm. Pull billing data from OpenAI, Anthropic, AWS (Bedrock + EC2/GPU), Cursor, Copilot, and any internal proxies. Interview the top 10 consumers and the Head of each desk to understand workloads, criticality, and pain points. Output: a single consolidated spend baseline, top 20 use cases by cost, and a risk register.
>
> Days 31–60 — **Optimize**. Pick the 3 highest-ROI levers: typically (1) standardize tagging via a central proxy so 100% of calls are attributable; (2) deploy a model-routing policy — cheap models for cheap tasks; (3) turn on prompt caching and batch API on the obvious workloads. Stand up a weekly FinOps review with Eng and Procurement.
>
> Days 61–90 — **Operate**. Roll out chargeback in showback mode, publish the first monthly AI Spend Report to the Head of Core AI & ML and to desk heads, define governance policy (budgets, model allow-lists, escalation runbooks), and start the first vendor renegotiation cycle with Anthropic/OpenAI/AWS based on now-clean usage data."

**Q2. How do you think about cost vs capability trade-offs when a quant team wants to use the most expensive model?**

> "I treat the decision as a unit-economics problem, not a $/token problem. If Claude Opus on a research summarization task produces an idea that's worth even a fraction of a basis point on a strategy, the $ are irrelevant. So the conversation isn't 'use a cheaper model' — it's 'let's measure what the workload actually needs.' I'd run an A/B: same 500-sample task on Opus vs Sonnet vs Haiku, score outputs with the team's own eval rubric, and compare cost-per-acceptable-output. Often the answer is route by complexity — 70% of calls work fine on Sonnet, the hard 30% go to Opus. That preserves quality and cuts spend 40–60%."

**Q3. How would you build a chargeback system from scratch here?**

> "Three layers.
> **Layer 1 — Capture.** A thin internal LLM proxy in front of every external API. Every request carries mandatory metadata: team, project, cost_center, use_case, user. Requests without tags are rejected after a 30-day grace period. The proxy also logs tokens-in, tokens-out, model, cached_tokens, latency, and outcome.
> **Layer 2 — Allocate.** Nightly job rolls usage into a warehouse table joined with the price book (per model, per token type, including PT amortization). Bedrock costs come from CUR + Application Inference Profiles. Cursor/Copilot come from their admin APIs.
> **Layer 3 — Bill.** Monthly chargeback statements per cost center, with drilldowns to project and user. First 2–3 months are showback (no real $) to build trust and let teams correct misallocations. Then we flip to true chargeback with a clear dispute process."

**Q4. What's the difference between showback and chargeback, and which would you start with?**

> "Showback shows teams what they consumed and what it cost — visibility only, no internal money moves. Chargeback actually debits their P&L or budget. I always start with showback for 2–3 months because (a) the data is never clean on day one, (b) it builds trust with desk heads who otherwise see chargeback as a tax, and (c) showback alone usually drives a 15–25% cost reduction through behavior change. Then I flip to chargeback once the allocation is defensible and the policy is published."

### B. Technical / FinOps Depth

**Q5. What's the difference between input and output tokens, and why does it matter?**

> "Output tokens are typically 3–5x the price of input tokens — for Claude Sonnet it's $3 vs $15 per million, for GPT-4o it's $2.50 vs $10. So the same call with a 10K input and 200 output costs $0.033, but if you let the model ramble to 2K output it's $0.055 — output tokens dominate cost. Three implications: (1) use `max_tokens` aggressively, (2) ask for structured/JSON output to keep responses tight, (3) when summarizing or extracting, design the prompt to force concise output. On the input side, prompt caching changes the math — cached input can be 90% cheaper, so consolidating stable system prompts is high-leverage."

**Q6. Explain prompt caching and when it pays off.**

> "Prompt caching lets the provider store the KV-cache of a stable prompt prefix on their side. Subsequent calls that reuse the prefix pay a fraction — Anthropic charges ~10% of input price on cache hits, OpenAI auto-caches at 50% off after a 1K-token threshold. It pays off when (a) you have a long stable prefix — system prompt, tool definitions, retrieved context, or a long document being asked multiple questions; (b) you make repeated calls within the cache TTL (5 min standard / 1 hr extended on Anthropic); (c) the cache write cost — Anthropic charges 25% extra on the first call — is amortized over enough hits. Rule of thumb: at 2+ hits within TTL, you're net positive."

**Q7. When does Bedrock Provisioned Throughput make sense vs on-demand?**

> "On-demand is pay-per-token, unlimited scale, no commitment — perfect for spiky or unknown workloads. PT reserves capacity ('model units') by the hour with a 1-month or 6-month commitment — you get predictable latency and a lower effective $/token if you saturate it. The math: take your on-demand cost for a given workload, compare to (model_units × hourly_PT_rate × hours). PT wins when (a) sustained utilization is roughly 60%+, (b) you need throughput guarantees, or (c) latency consistency matters. The trap is buying PT for 'forecasted' demand that never materializes — I'd require 30 days of on-demand baseline before any PT commitment."

**Q8. How would you detect and respond to a runaway agent that's burning tokens?**

> "Three layers.
> **Prevent:** every agent has a hard token budget per session (e.g., 200K tokens), max recursion depth, and a per-user/minute rate limit at the proxy.
> **Detect:** real-time anomaly detection on $/hour per project — a 3-sigma spike triggers an alert. LangSmith/Langfuse traces let me see step-by-step where tokens are going.
> **Respond:** runbook escalates to me as L2; I can kill the project's key, throttle the team, and we do a post-mortem within 24h. The first time this happens you learn the failure mode — usually an unbounded ReAct loop, a tool that returns huge JSON blobs back into context, or a malformed prompt that triggers repeated retries."

**Q9. How do you attribute cost when multiple teams share the same fine-tuned model or PTU?**

> "Two-step allocation. First, the fixed cost of the PTU or fine-tuning job is a 'pool.' Second, allocate the pool to teams by a fair driver — usually tokens consumed against that resource, weighted by priority if needed. I publish the allocation method up front so it's not a black box. For fine-tunes, I also charge the originating team the training cost as a one-time, then amortize inference normally."

**Q10. What metrics would you put on a CFO-ready monthly AI dashboard?**

> "Top of dashboard — three numbers: total AI spend MTD vs budget, forecast vs annual plan, and $/active-user.
> Then breakdowns: spend by team, by provider, by model, by use case.
> Unit economics: $/successful-task for the top 5 workloads.
> Efficiency: % cached tokens, % batch tokens, % calls on cheapest-acceptable model.
> Risk: top 5 cost centers vs their budget, count of untagged calls, vendor concentration (% of spend on single provider).
> Trend: 13-week rolling spend, with annotations for launches and price changes."

### C. Vendor & Negotiation

**Q11. Anthropic gives you a 15% committed-spend discount for $5M annual. Walk me through your decision.**

> "I'd anchor on three questions.
> (1) **Forecast confidence** — do I have 3+ months of clean usage data showing $5M is realistic? If forecast is $3M, I'm overcommitting; if $8M, I should push for a bigger commitment and bigger discount.
> (2) **Lock-in risk** — Anthropic prices have dropped meaningfully over 18 months; multi-year locks me into yesterday's price. I'd push for annual with a price-protection clause: if their public list drops, my rate drops proportionally.
> (3) **Leverage** — what's the counter-offer from OpenAI, and what's Bedrock's Anthropic pricing? If Bedrock-routed Claude is within 5% and gives me AWS billing consolidation, that's worth more than the 15%.
> Final move: I'd accept a 12-month commit at, say, $4M (below my forecast for safety) for 12% discount, plus negotiate prompt-caching uplift, batch API access, dedicated capacity, and a price-protection clause. Then put the remaining workload on Bedrock for optionality."

**Q12. Procurement asks you to pick a single LLM vendor for the firm. What do you say?**

> "I'd push back. Single-vendor is operationally simpler but strategically fragile in a market where capability and price change quarterly. My recommendation is **strategic dual-source** — Anthropic + OpenAI as primaries, with Bedrock as an aggregation layer for model optionality and AWS billing integration. The premium for multi-vendor is 5–10% in eng overhead, but it (a) gives me real renegotiation leverage every year, (b) protects against outages — both have had multi-hour incidents this year, (c) lets each team use the best model for their workload, and (d) hedges against capability divergence. The exception is if a vendor offers an unbeatable enterprise package with deep co-development — then a primary-with-fallback model can work."

### D. Org & Stakeholder

**Q13. A senior PM says your cost controls are slowing his team down. How do you handle it?**

> "First, I listen — they're a customer, not an adversary. Concretely: I'd sit with their lead engineer for an hour, walk through which control is biting (rate limit? budget cap? model restriction?), and ask what they're trying to achieve. Often the fix is local — raise their team's budget, whitelist a model for their use case, or pre-approve a workflow. Sometimes the control is wrong and I change it. Sometimes the workload is genuinely wasteful and I help them optimize — that wins trust faster than any policy. The principle: governance exists to enable the firm to use AI more, not less. If a control isn't earning its cost in waste prevented, it should go."

**Q14. How do you operate as L1 escalation across global time zones?**

> "I'd structure a follow-the-sun L1 with regional points-of-contact — APAC, EMEA, NYC — each owning their working-hours triage with a clear playbook. I sit on top as the global owner: incident commander for major events, owner of the post-mortem template, owner of the runbook library. PagerDuty (or equivalent) routes by service + region + severity. Major incidents — say, a provider outage affecting trading-adjacent workloads — get a Slack war-room within 5 minutes, status page updates every 15 minutes, and a written PIR within 48 hours. The goal is never to be the bottleneck while still being the accountable owner."

---

## 6. Behavioral

Tower's culture line: *"smart, driven people, no ego."* Prepare 6–8 STAR stories. Suggested themes:

1. **Drove a measurable cost-reduction** (any cloud/SaaS/AI) — quantify the $ and the %.
2. **Built something cross-functional** (eng + finance + procurement).
3. **Owned an incident / outage** end-to-end including the post-mortem.
4. **Negotiated a vendor contract** — what you asked for, what you got, what you walked away from.
5. **Pushed back on a senior stakeholder** with data, and the outcome.
6. **Learned a new technical domain fast** (relevant if you're newer to LLMs specifically).
7. **Built a dashboard / reporting system** that changed a decision.
8. **Managed competing priorities** under time pressure.

**STAR format reminder:**
- **S**ituation — 1–2 sentences of context
- **T**ask — what you specifically owned
- **A**ction — what *you* did (use "I," not "we" where possible)
- **R**esult — quantified outcome + what you learned

### Sample STAR (template you adapt to your real experience)

> **S:** "At [prior firm], our quant research org's OpenAI spend grew from $40K to $380K per month in 5 months with no attribution — nobody could tell me which team or use case was driving it."
> **T:** "I was asked by the CTO to get it under control without slowing research."
> **A:** "I built a lightweight proxy in front of the OpenAI SDK that enforced tagging, capped token budgets per project key, and shipped logs to BigQuery. I then ran a 2-week deep-dive on the top 5 cost drivers — three of them were running GPT-4 on tasks that worked equivalently on GPT-3.5, one was an unbounded agent retry loop, and one was a legitimately expensive but high-ROI strategy backtest. I rolled out a model-tier policy, fixed the retry loop with the eng team, and presented showback dashboards weekly."
> **R:** "Monthly spend dropped to $190K within 6 weeks (-50%) while call volume grew 30%. The CTO adopted the proxy + showback model as the firm-wide pattern."

---

## 7. Case Studies

Be prepared for one or more of these on a whiteboard or in conversation.

### Case A — Design a token attribution system
*"Walk me through the architecture you'd build to attribute every LLM call at Tower to a team, project, and user."*

**Sketch this:**
```
Developer / Service
        │
        ▼  (SDK or HTTP)
┌──────────────────────┐
│  Internal LLM Proxy  │  ← enforces auth, tags, budgets, rate limits
│  (FastAPI / Envoy)   │
└──────────┬───────────┘
           │
           ├──► OpenAI API
           ├──► Anthropic API
           ├──► AWS Bedrock
           └──► Self-hosted (vLLM/TGI)
           │
           ▼
   Async log stream (Kafka / Kinesis)
           │
           ▼
   Warehouse (Snowflake / BigQuery / Redshift)
           │
           ▼
   ┌─────────────┬──────────────┬──────────────┐
   │  Dashboards │  Chargeback  │  Anomaly Det │
   │  (Looker)   │  (monthly)   │  (real-time) │
   └─────────────┴──────────────┴──────────────┘
```
Key design points: mandatory tags on auth, fail-closed (no tag = no call), shadow-mode for 30 days, async logging so the proxy never adds latency, separate hot/cold storage, integrate with Langfuse/LangSmith for trace-level drilldown.

### Case B — Cost optimization scenario
*"Team X is spending $2M/year on Claude Opus for a daily research-summarization workflow. Reduce their cost by 50% without quality regression."*

Walk through:
1. **Measure baseline** — capture 1 week of representative calls (prompts + outputs).
2. **Define quality** — work with team on an eval rubric (factual accuracy, coverage, conciseness).
3. **Test alternatives** — Sonnet, Haiku, GPT-4o-mini, fine-tuned smaller model, all scored on the same eval set.
4. **Layer optimizations** — prompt caching on the stable instruction + research-corpus prefix; batch API since it runs overnight; structured output to cap response length.
5. **Routing policy** — easy summaries on Sonnet, hard / multi-doc on Opus.
6. **Projected savings** — show the math, validate with a 2-week shadow run, then cut over.

### Case C — Vendor negotiation roleplay
The interviewer plays Anthropic AE; you negotiate the renewal. Practice this with a friend.

### Case D — Build the monthly report
Sketch the actual dashboard layout (sections, charts, KPIs) for the Head of Core AI & ML.

---

## 8. Questions to Ask

Have 8–10 ready; ask 3–5 per round, tailored to the interviewer.

**Strategic:**
- "What's the firm's current annual run-rate on external LLM spend, and what's the growth trajectory?"
- "Is the mandate primarily cost control, or also enabling more AI adoption across the firm?"
- "How is AI ROI currently measured — at the firm, desk, or use-case level?"

**Operational:**
- "How is AI infrastructure split today between internal (self-hosted) and external providers?"
- "Do you already have an internal LLM proxy / gateway, or would I build that?"
- "What does the current tagging / attribution look like?"
- "Who are the top 3 LLM consumers internally, and what are their workloads?"

**Org & stakeholders:**
- "Who would my closest partners be in Procurement, Finance, and Engineering?"
- "How does the Core AI & ML group interact with the trading pods — central platform, embedded, or hybrid?"
- "What does success look like in this role at 6 months and 12 months from the Global Head's perspective?"

**Culture:**
- "What separates someone who's great in this role from someone who's just good?"
- "What's the biggest open problem on the AI ops side today?"

---

## 9. Study Plan

A 7-day plan assuming the interview is next week. Compress as needed.

### Day 1 — Company & Role
- Tower Research website (Careers, About, Technology pages).
- LinkedIn deep-dive: Global Head of Core AI & ML, your interviewers, current employees in similar roles.
- Read 2–3 articles on Tower's history and HFT model.
- Re-read the JD; write your own 1-pager mapping each bullet to a concrete example you can give.

### Day 2 — LLM Pricing & Token Economics
- Memorize current per-million-token rates for: GPT-4o, GPT-4o-mini, o3, Claude Opus/Sonnet/Haiku 4.x, Gemini 1.5/2.0 Pro/Flash, Bedrock equivalents.
- Read OpenAI's prompt-caching docs and Anthropic's prompt-caching docs end-to-end.
- Read OpenAI's Batch API and Anthropic Message Batches docs.
- Do the worked-example math (Section 3.2) on paper from memory.

### Day 3 — AWS Bedrock & Cloud Billing
- AWS Bedrock pricing page (on-demand vs Provisioned Throughput, model units).
- AWS Bedrock Application Inference Profiles documentation.
- AWS Cost Explorer + CUR + Cost Allocation Tags overview.
- AWS Budgets + Cost Anomaly Detection.

### Day 4 — Orchestration & Observability
- LangChain quickstart + LangGraph concepts (state, nodes, edges, checkpointing).
- LangSmith vs Langfuse vs Helicone comparison (read each tool's "why us" page).
- Skim a Langfuse self-host setup — be able to talk about it.

### Day 5 — FinOps & Governance
- FinOps Foundation: Inform/Optimize/Operate framework (one-pager exists on their site).
- Read 1–2 industry write-ups on "AI FinOps" or "LLMOps cost management" (CloudZero, Vantage, Anyscale blogs).
- Sketch your own chargeback policy doc — tagging standard, allocation method, dispute process.

### Day 6 — Mock interviews
- Out-loud practice with a friend or alone with a recorder.
- Run Section 5 questions in random order; time yourself to 2–3 min per answer.
- Practice the whiteboard architecture (Case A) on paper or Miro.
- Refine your STAR stories.

### Day 7 — Light review + rest
- Re-read this document.
- Re-read the JD.
- Read your STAR stories aloud.
- Don't cram new material — rest is more valuable than one more concept.
- Lay out clothes, test video setup if remote, plan commute if in-person.

---

## 10. Final Checklist

### 24 hours before
- [ ] Re-read JD and this doc once.
- [ ] Confirm interview time, format, panel names.
- [ ] LinkedIn-stalk each interviewer (read their last 3 posts; note shared background).
- [ ] Print 2 copies of your resume.
- [ ] Test video/audio if remote; pick a quiet space with good lighting.
- [ ] Prepare 8–10 questions to ask (Section 8).
- [ ] Sleep 7+ hours.

### Day-of
- [ ] Arrive 10 min early (or join 2 min early if remote).
- [ ] Water + a snack 30 min before.
- [ ] Open: a confident, friendly intro (60–90 seconds about who you are and why this role).
- [ ] Listen more than you talk; clarify before answering.
- [ ] Quantify everything — $, %, headcount, time.
- [ ] Use the language: tokens, attribution, chargeback, PT, prompt caching, FinOps lifecycle, model routing, batch, observability.
- [ ] When you don't know something: say "I haven't worked with X directly, but my mental model is Y — is that close?" Honesty + structured thinking > bluffing.
- [ ] Close: reiterate interest, ask about next steps, thank each interviewer by name.

### Within 24 hours after
- [ ] Send a short thank-you email to each interviewer (or to the recruiter to forward).
- [ ] Reference one specific topic from each conversation.
- [ ] Note your own debrief: what went well, what to sharpen for next round.

---

## One-Page Cheat Sheet (memorize this)

> **Role in one sentence:** Run AI FinOps for Tower — attribute every LLM dollar, optimize spend, govern usage, and negotiate vendors, so trading and engineering can use AI more, not less.
>
> **Three pillars:** Attribution (tag everything via a proxy). Optimization (model routing + caching + batch + PT). Governance (budgets, policies, controls, chargeback).
>
> **Three frameworks I always use:** FinOps Lifecycle (Inform → Optimize → Operate). Unit economics ($/successful-task). Strategic dual-source vendor strategy.
>
> **Three tools I'll evaluate Day 1:** internal LLM proxy + tagging, Langfuse (self-hosted) for observability, AWS Cost Explorer + Bedrock Application Inference Profiles for cloud-side attribution.
>
> **Three numbers I'll deliver in 90 days:** a clean firm-wide AI spend baseline; the first chargeback statement (showback mode); a 20–30% in-flight cost reduction from quick wins (caching, routing, batch).

---

*Good luck, Kalpit. You've got this — go in calm, structured, and concrete.*
