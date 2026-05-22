# Deep Dives — Bedrock Cost Mechanics & Vendor Negotiation Roleplay

> Two long-form deep dives, each designed to take you from "I've heard of this" to "I can hold a 20-minute technical conversation about it."

---

# Part 1: AWS Bedrock Cost Deep Dive

## Why this matters for Tower

Bedrock is the most likely **AWS-native LLM aggregation layer** at Tower because:
- Tower already runs heavily on AWS (their trading and research infra is AWS-anchored).
- Bedrock gives access to Anthropic, Meta, Cohere, Mistral, Amazon's own models through one API.
- AWS billing consolidation means Bedrock spend flows into the same CUR/Cost Explorer the firm already uses for everything else.
- Enterprise procurement leverage — Bedrock spend counts toward the AWS Enterprise Discount Program (EDP).

If you walk in fluent on Bedrock specifically, you're meaningfully ahead of most candidates.

---

## 1. Bedrock pricing modes

Bedrock has **three distinct pricing models** you must distinguish cleanly:

### Mode A — On-Demand
- Pay per input token and per output token.
- No commitment, instant scale, default mode.
- Subject to **regional throughput quotas** per model — you can be throttled at peak.
- Best for: spiky workloads, new use cases, exploration.

### Mode B — Provisioned Throughput (PT)
- Reserve capacity in units called **model units (MUs)**.
- Pay an hourly rate per MU. 1-month commitment (no discount over hourly) or 6-month commitment (~40% discount).
- Within the reserved capacity: **unlimited tokens, no per-token charge, guaranteed latency**.
- Best for: sustained, predictable high-volume workloads.
- The hourly rate varies dramatically by model — a Claude Opus MU is far more expensive than a Llama MU.

### Mode C — Batch Inference
- Async batch jobs, **50% off on-demand pricing**.
- 24-hour completion target.
- Best for: backfills, evaluations, overnight summarization, dataset processing.

### Decision rule
```
if workload is spiky OR new OR low-volume:           → On-Demand
elif latency-tolerant AND batchable:                  → Batch (50% off)
elif sustained_utilization >= 60% of needed capacity: → Provisioned Throughput
else:                                                  → On-Demand (default)
```

---

## 2. Cross-region inference & inference profiles

This is the heart of Bedrock cost attribution at scale. Understand the four concepts:

### Foundation Models (FMs)
The raw model — e.g., `anthropic.claude-3-5-sonnet-20241022-v2:0`.

### System-defined Inference Profiles (cross-region)
AWS-managed routing across regions to avoid regional throttling.
- Example: `us.anthropic.claude-3-5-sonnet-20241022-v2:0` (US cross-region).
- Same price as direct foundation model.
- **Important:** these absorb throttling spikes by load-balancing across US-East, US-West, etc.

### Application Inference Profiles (custom — the one you care about for cost)
- Custom inference profiles **you create** to wrap a foundation model with **tags**.
- Tags are arbitrary key-value pairs: `team=quant-research`, `project=alpha-7`, `cost_center=CC-1234`.
- Every invocation through the profile inherits the tags.
- Tags flow into **AWS Cost Explorer** and **CUR** when activated as cost allocation tags.
- This is the **single most important Bedrock construct for chargeback at Tower**.

### Workflow:
```
1. Admin creates Application Inference Profile per team/project:
   bedrock create-inference-profile \
       --inference-profile-name "quant-research-alpha7-sonnet" \
       --model-source ".../us.anthropic.claude-3-5-sonnet-20241022-v2:0" \
       --tags Key=Team,Value=QuantResearch Key=Project,Value=Alpha7 Key=CostCenter,Value=CC-1234

2. Team's application uses the profile ARN instead of raw model ID.

3. AWS bills the calls with the tags attached.

4. Cost Explorer / CUR group by tag → instant per-team / per-project chargeback view.
```

### Cost Explorer view you'd build
- **Dimension:** Cost Allocation Tag `Team`
- **Service filter:** Amazon Bedrock
- **Granularity:** Daily
- **Forecast on**: yes
- **Saved view:** "Bedrock Spend by Team — Last 90d"

**Repeat for:** Project, CostCenter, UseCase, Environment.

---

## 3. Cost Allocation Tags activation gotcha

Just adding tags isn't enough — they must be **activated** in AWS Billing as cost allocation tags. This is a per-account, per-tag-key operation in the AWS Billing console.

**Activation has a lag:** tags activated today only appear in CUR going forward; historical data is not retroactively tagged.

**Tower implication:** activate the full tagging schema **before** you start collecting baseline data. Otherwise you'll have a month of untagged Bedrock spend that's hard to attribute.

---

## 4. CUR (Cost and Usage Report) deep dive

The CUR is AWS's raw billing data — far more granular than Cost Explorer.

- Hourly granularity.
- Every line item: account, service, usage type, resource ARN, **all tags**, blended cost, unblended cost.
- Delivered to S3, queryable via Athena (or shipped to Snowflake/Redshift).
- **Bedrock line items show as:**
  - `service`: `AmazonBedrock`
  - `usageType`: e.g., `USE1-CompletionsTok-Claude-Sonnet-3-5` (input vs output is in the usage type)
  - `lineItemType`: `Usage`

### Sample Athena query for Bedrock spend by team
```sql
SELECT
    bill_billing_period_start_date AS month,
    resource_tags_user_team AS team,
    resource_tags_user_project AS project,
    SUM(line_item_unblended_cost) AS cost_usd,
    SUM(line_item_usage_amount) AS tokens
FROM aws_cur.cur_table
WHERE line_item_product_code = 'AmazonBedrock'
  AND bill_billing_period_start_date >= DATE '2026-01-01'
GROUP BY 1, 2, 3
ORDER BY 1, 4 DESC;
```

You should be able to write this on a whiteboard.

---

## 5. Bedrock Provisioned Throughput cost math

### Model Units (MUs)
- Unit of reserved throughput.
- Throughput per MU is **model-specific** and AWS-published — typically ~1,200 input tokens/sec and ~120 output tokens/sec for a Claude Sonnet MU (example only, verify current numbers).
- Hourly rate per MU is also model-specific.

### When PT wins — the formula
```
on_demand_monthly_cost  =  (input_tokens × input_$/token) + (output_tokens × output_$/token)
pt_monthly_cost         =  (number_of_MUs × hourly_$/MU × 720 hours)
```

PT is cheaper when:
```
on_demand_monthly_cost > pt_monthly_cost
```

Which simplifies to a **utilization threshold** — typically PT breaks even around **40–60% sustained utilization** of the throughput capacity. Above that, PT wins. Below, on-demand wins.

### The 6-month commitment discount
- 6-month MUs are roughly **40% cheaper hourly** than 1-month MUs (verify current rates).
- Only commit to 6-month for workloads where you have **6+ months of stable baseline**.
- Trap: forecasting a new product's demand 6 months out. Don't do it.

### Worked example
> Workload: 300M input tokens + 50M output tokens / month on Claude Sonnet.
> On-demand cost: (300M × $3/M) + (50M × $15/M) = $900 + $750 = **$1,650 / month**.
>
> Hmm — that's tiny. PT would never make sense here. PT is for the workloads spending $50K-500K+/month on a single model.
>
> Now scale up: 30B input + 5B output (1000x). On-demand = **$165K / month**.
> If you can saturate, say, 5 MUs at $X/hour each, PT might come out to $90K — a $75K/month win. Verify with the calculator.

### AWS Bedrock Pricing Calculator
- Built-in tool to compare on-demand vs PT for your workload profile.
- **Always run this before any PT commitment.**
- Run it again 30 days into a PT commitment to validate the assumption.

---

## 6. Bedrock cost optimization checklist (Tower-applicable)

| Lever | When | Expected savings |
|---|---|---|
| Right-size model (Sonnet vs Opus) | Always evaluate | 30–80% |
| Prompt caching (Claude on Bedrock) | Long stable prefixes | 30–70% on cached input |
| Batch inference | Latency-tolerant | 50% |
| Provisioned Throughput (1-month) | 60%+ sustained util | 20–30% |
| Provisioned Throughput (6-month) | Stable, 6mo proven | 35–45% |
| Application Inference Profiles | Always — for chargeback | (enables everything else) |
| Cross-region profiles | Throttling-bound workloads | (latency/availability, not $) |
| Knowledge Bases vs custom RAG | Lower volume, simpler | Eng time + 10–20% |
| AWS Bedrock Guardrails | Compliance-required | (risk reduction, not $) |
| Move to AWS EDP | Multi-million $ committed AWS spend | 5–15% blended |

---

## 7. Bedrock vs direct vendor API — the choice

| Dimension | Bedrock | Direct (Anthropic/OpenAI) |
|---|---|---|
| **Billing consolidation** | AWS one invoice | Separate invoice per vendor |
| **Cost attribution** | Application Inference Profiles → CUR | Vendor-specific (usually weaker) |
| **Pricing** | Near-parity in most regions | List price, but better committed-spend deals direct |
| **Data residency** | AWS region of your choice | Vendor-controlled |
| **Latency** | Slight overhead (~5-30ms) | Direct |
| **Feature parity** | Often lags vendor by weeks/months for new features | Day-one access |
| **Compliance** | AWS shared-responsibility model | Vendor's compliance |
| **Procurement** | Via AWS — leverages EDP | Separate MSA per vendor |
| **Multi-model flexibility** | Single API across providers | One vendor at a time |

**Tower recommendation:** Hybrid. Bedrock for production workloads where billing consolidation + AWS-native compliance matters. Direct API access for cutting-edge features and where you want vendor-specific committed-spend leverage. Internal proxy abstracts the choice from end users.

---

## 8. Common Bedrock pitfalls (mention these — shows you've operated this)

1. **Tags not activated in Billing.** Tags exist but don't surface in CUR. Diagnosis: Billing → Cost Allocation Tags page, look for inactive tags. Fix: activate, wait 24h.
2. **Cross-account Bedrock charges hard to allocate.** When one account makes Bedrock calls billed to another, attribution can break. Use consolidated billing + per-account tagging discipline.
3. **PT bought before baseline.** Burning $X/hour on idle MUs. Always start with on-demand baseline.
4. **Forgetting batch.** Teams default to on-demand even for clearly batchable workloads (overnight analytics). Default batch for anything not user-facing.
5. **Region sprawl.** Same model used in 3 regions for "redundancy" without need — triples some costs. Centralize unless latency demands otherwise.
6. **Guardrails on every call by default.** Bedrock Guardrails are billed per text unit. Apply selectively, not blanket.
7. **Knowledge Bases retrieval overhead.** Each KB query has its own embedding + retrieval cost on top of the LLM call. Audit if KB is actually needed vs simpler retrieval.

---

# Part 2: Vendor Negotiation Roleplay

## How to use this

Print or pull this up on a second screen. Have a friend play "Anthropic AE" using the prompts below. You play yourself.

Three full rounds:
- **Round 1:** They go aggressive. You hold the line.
- **Round 2:** Find the win-win. Trade asks for asks.
- **Round 3:** Close — or walk.

After each round, read the **"What good looked like"** notes to self-grade.

---

## Scenario setup (read aloud before starting)

> **Situation:** You are the AI Operations Manager at Tower Research Capital. Tower has been an Anthropic customer for 14 months. Current run-rate is **$280K/month** on Claude Sonnet 4 and Opus 4, spread across 6 internal teams. Growth has been ~15% month-over-month for the last 6 months.
>
> Today is the renewal meeting. Anthropic's AE, "Sarah," is on the call. Last year's contract was list-price with a 5% courtesy discount.
>
> **Your goals (in priority order):**
> 1. Lock in a meaningful committed-spend discount (target: 15%+).
> 2. Get a **price-protection clause** — your rate auto-adjusts if Anthropic's list price drops more than 10%.
> 3. Get **prompt caching** and **Message Batches API** at no incremental cost.
> 4. **No multi-year lock-in** — annual term only.
> 5. Stronger **SLA** (current is 99.5%; you want 99.9%) with **service credits** for misses.
> 6. **Zero data retention** clarified in writing.
> 7. **No price increase** on existing rates within the term.
>
> **Your BATNA:** You have a live OpenAI quote ($2.10 input / $9 output on GPT-4o equivalent if you commit $4M). You have AWS Bedrock pricing for Claude as a fallback (near-parity but with AWS EDP credit).
>
> **Sarah's likely goals:**
> 1. Larger commit (push you to $4M+ annual).
> 2. Multi-year lock-in (2 years preferred).
> 3. Tightest possible discount (start at 8%, end at 12%).
> 4. Avoid price-protection clauses.
> 5. Upsell to Claude Opus tier and Enterprise platform features.

---

## Round 1 — Opening

**Sarah:** "Thanks for making time. We're really glad to be partnering with Tower. Looking at your usage, you're tracking to about **$3.4M** annual — congrats, that's a 2.5x growth from last year. I want to propose a renewal that locks in your success: a **24-month commitment** at **$4M annual** in exchange for a **10% discount** off our list prices, plus access to our Enterprise tier features at no upcharge."

**Your response — what to say:**
> "Sarah, thanks — and we appreciate the partnership too. A few quick reactions before we dig in.
>
> The 2.5x growth is real, but we've also been deliberately experimental in year one. As we mature our use cases, we expect our spend mix to shift — more caching, more batch, more workload routing to smaller models. So while I expect us to keep growing, I'm not comfortable committing to a 25% increase over current run-rate as the floor.
>
> Two structural points before commercials. One — we need annual, not multi-year. The market is repricing every quarter and a 24-month lock isn't a partnership, it's a hedge in your favor. Two — any commitment we make has to come with price-protection: if your list drops, our effective rate drops. Otherwise we're committing to today's price for tomorrow's market.
>
> On the discount itself, 10% is below market for a customer of our size and growth trajectory. We've benchmarked against direct OpenAI and Bedrock-routed Claude — there's clearly more room. Walk me through how you got to 10%."

**What good looked like:**
- Reframed THEIR opening (no panic, no agreement).
- Front-loaded your structural asks (annual, price protection) before talking $.
- Asked them to defend their number — puts them on back foot.
- Used market data without bluffing.

**Sarah's likely counter:**
> "I hear you. The 10% reflects standard customer at your tier. To go to 15%, I'd typically need a longer commitment. If you can do 18 months, I can stretch to 13%."

**Your response:**
> "Let's separate term length from discount tier and treat them as independent variables. Term length costs me flexibility — I'm not going to trade it for incremental discount, because the option value of being able to renegotiate next year is worth more than the 3% delta you're offering.
>
> On the discount alone — 13% is moving in the right direction but still under what I expect to land. Here's what I propose: 12-month term, committed spend at **$3M** — slightly below my forecast for safety — at **15% discount**. In exchange, I'll commit to making Anthropic our primary Claude provider through the term, which is real value to you in terms of forecasting and account stability."

**What good looked like:**
- Refused to bundle term + discount.
- Anchored commit *below* forecast (smart — protects you on the downside).
- Offered them something non-monetary (primary status).
- Took control of the structure of the deal.

---

## Round 2 — Mid-game

**Sarah:** "I can probably get to 14% on a 12-month at $3.5M. But I'm not authorized to do a price-protection clause — that's a structural thing for our finance team."

**Your response:**
> "Sarah, let's talk about price protection because I think there's a misalignment on what I'm asking for. I'm not asking for an unlimited best-price guarantee. I'm asking for one specific protection: if your published list price for a model we're using drops more than 10% within our contract term, we get the lower rate going forward — not retroactive. That's a reasonable customer-friendly term and several of your peers offer it. It also costs Anthropic nothing in 90% of scenarios because list prices don't usually drop by that much.
>
> If it's truly a structural blocker, here's an alternative: a **mid-term review clause** at month 6. If list prices have materially moved, we renegotiate the rate in good faith. That gives Anthropic the structural flexibility you need and gives me the protection I need.
>
> Now, on the 14% at $3.5M — I'd like to add three non-monetary asks that don't move your commercials but matter to me:
> - **Prompt caching and Message Batches API** included, with our cached-token rate at the published 90% discount.
> - **Zero data retention** documented in the MSA — not just policy, contract.
> - **99.9% uptime SLA** on the production endpoints we use, with service credits for misses.
>
> If we can land those three plus the rate, we're close."

**What good looked like:**
- Reframed the "structural blocker" — narrowed your ask precisely.
- Offered the mid-term review as creative alternative.
- Bundled non-monetary asks separately so they're not seen as discount-grabs.
- Used "we're close" — signals willingness to close while keeping pressure.

**Sarah's likely counter:**
> "Caching and batch are already standard — those are free. ZDR I can do as a contractual term. The 99.9% SLA is a stretch — our standard is 99.5%. I could probably do 99.7% with service credits."

**Your response:**
> "ZDR contractual — appreciate that, that's important. 99.7% with service credits I can work with if the credit structure is meaningful — let's say 10% credit at 99.5-99.7%, 25% credit below 99.5%. Workable?
>
> And just to close the loop on the mid-term review — yes or no?"

**What good looked like:**
- Pinned them down on the SLA credit structure with specifics.
- Returned to the unresolved item before letting it slip.
- Short, direct close-out language.

---

## Round 3 — Close

**Sarah:** "Let me see what I can do. Stand by..." *[returns after 10 minutes]* "Okay. Here's where I can land: **12-month term, $3.5M committed spend, 15% discount, prompt caching and batch included, ZDR in MSA, 99.7% SLA with the credit structure you proposed, and a mid-term review clause at month 6.** That's my best and final."

**Your response — Option A: Accept**
> "Sarah, that's a good deal and I think we have an agreement subject to legal review. Let me confirm what I'm signing off on commercially:
>
> 12 months, $3.5M committed, 15% off list on input and output tokens, prompt caching included at the published cache rates, Message Batches API access at standard batch pricing, ZDR contractual, 99.7% SLA with credit tiers as discussed, mid-term review at month 6 in good faith.
>
> Procurement and Legal will pick up the paper from here. I'll connect you with [Procurement contact] today. Quarterly business reviews — let's set the first one for [date 3 months from now]. Thanks for the work on this."

**Your response — Option B: Push for one more thing**
> "Sarah, that's most of the way there. One last item — Procurement is going to push back on $3.5M commit when our current run rate annualizes to $3.36M. The risk of overcommit lands on us, not you. If you can come down to $3M committed at the same 15%, you have a deal today. Otherwise I need to take $3.5M back to my team for sign-off and it'll push us a week."

**What good looked like:**
- Option A: Read back the full deal before agreeing — eliminates "scope creep" later.
- Option B: One last small ask, anchored on a defensible reason, with a real "or else."
- Either way: clear close, named handoff to Procurement, scheduled QBR.

---

## Negotiation principles to internalize

1. **Never accept the first offer.** Even if it's good. The act of pushing back surfaces what else is available.
2. **Separate variables.** Don't let them bundle term + price + commit. Negotiate each independently.
3. **Anchor commit BELOW forecast.** Overcommit is asymmetric — you eat the loss, they keep your money.
4. **Non-monetary asks are free to ask for.** ZDR, SLA, caching, QBRs, named technical contact, capacity guarantees.
5. **Always have a BATNA you've actually validated.** Bluffing on alternatives gets you outed.
6. **Read back the deal.** Half of contract disputes come from "we agreed to X but the paper says Y."
7. **Name the next step explicitly.** Handoff to Procurement, draft turnaround time, QBR date.
8. **Be likeable.** AEs have discretion. They give the best terms to customers their team enjoys working with. Stay professional and warm even when pressing hard.

---

## Self-grading rubric for the roleplay

After each pass, score yourself 1–5 on:

- **Held structure** (didn't get railroaded into their framing)
- **Used data** (specific numbers, market benchmarks, BATNA references)
- **Asked for non-monetary value** (didn't just chase discount %)
- **Closed cleanly** (read-back, named handoff, dates)
- **Stayed warm** (firm without being adversarial)

Target: 4+ across all five by your third pass.

---

# Cross-Reference

These three documents work together:

| Document | Use it for |
|---|---|
| `Tower_AI_Ops_Manager_Interview_Prep.md` | The strategic backbone — read once, reference throughout |
| `Tower_AI_Ops_Flashcards.md` | Daily 5-min drills on pricing and concepts |
| `Tower_AI_Ops_Mock_Interview.md` | Three practice passes — solo or with a partner |
| `Tower_AI_Ops_Deep_Dives.md` (this file) | Bedrock fluency + negotiation muscle memory |

Run the flashcards every morning for the week before. Run the mock interview Wed, Fri, and the night before. Read the deep dives twice — once Monday, once Thursday. You're ready.
