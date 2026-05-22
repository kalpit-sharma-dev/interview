# Mock Interview Script — Tower Research Capital, AI Operations Manager

> **How to use this:**
> 1. **Solo mode:** Read each question aloud, set a 2-minute timer, answer out loud (record yourself). Then read the "model answer framework" and the "what great looks like" notes to self-grade.
> 2. **Partner mode:** Give this doc to a friend. They ask the questions in order, ad-lib follow-ups, and use the "interviewer notes" to probe.
> 3. **Goal:** Three full passes before the real interview. Pass 1 = read everything. Pass 2 = answer cold. Pass 3 = answer crisply in <2 minutes each.

---

## Round 1 — Recruiter / HR Screen (30 min)

**Tone:** Friendly, conversational. Screening for motivation, communication, baseline fit.

---

### Q1. "Tell me about yourself and why you're interested in this role."

**Framework (60–90 seconds, NOT your life story):**
- Present: what you do now, in one sentence with a number.
- Past: 1–2 relevant prior experiences that build to this moment.
- Future: why Tower, why this role, why now.

**Example structure:**
> "I currently [current role] where I [most relevant achievement, quantified]. Before that I [prior role bridging to AI/cost/ops]. The reason this role caught my attention is that AI cost has gone from a rounding error to a board-level line item in the last 18 months, and Tower sits at the intersection of where that matters most — a firm where every dollar is P&L and the AI footprint is growing fast. I want to be the person who turns that from a cost problem into a strategic advantage."

**What great looks like:**
- Under 90 seconds.
- One concrete number from your past.
- A clear "why Tower specifically" — not generic "I love AI."
- Energy in your voice — sound like you want this.

**Interviewer probe:** "What specifically about Tower over a tech company or a bank?"
> "Tower is buy-side and prop — which means cost discipline is direct P&L, not a budget line item to be defended. And the pod model means I'd be working with smart, demanding internal customers who'll push my thinking. I'd rather be in that environment than at a SaaS vendor selling FinOps to other people."

---

### Q2. "What do you know about Tower Research Capital?"

**Framework:**
- 3 facts (founding, business model, tech).
- 1 insight (what makes them different).
- 1 question (shows curiosity).

**Example:**
> "Tower's a proprietary quantitative trading firm — Mark Gorton founded it in 1998 — and they're known for low-latency systematic trading across asset classes, with serious investment in FPGA and hardware acceleration. The thing that stands out to me is the pod model: independent PMs supported by a strong central platform. That's a very different operating model from a top-down hedge fund, and it makes the central platform's job — including Core AI & ML — both higher leverage and higher stakes. One question I'm curious about: how much of the AI footprint today is centralized vs. PM-owned?"

**What great looks like:** Specific facts (not Wikipedia recital), shows you've thought about the *operating model*, ends in a question.

---

### Q3. "Walk me through your resume."

**Framework:** Chronological but selective. 60 seconds per role. Each role: scope → biggest impact (quantified) → why you moved on.

**Pitfall to avoid:** Don't read your resume verbatim. The interviewer has it. Highlight the through-line.

**Through-line to land on:**
> "If I look back, the thread is that I've consistently moved toward roles where I sit between the technology and the money — where the win is measured in both system reliability and unit economics. This Tower role is the cleanest expression of that pattern."

---

### Q4. "Why are you leaving your current role?"

**Framework:** Positive framing. Never bash current employer. Pull toward Tower, don't push from current job.

> "I'm happy where I am — I'm not running from anything. But this role is a step-change in scope: working directly with the Global Head of Core AI & ML at a firm where AI is becoming infrastructure, not just experimentation. That's the kind of move I'd make once and stay for."

---

### Q5. "What are your compensation expectations?"

**Framework:** Deflect with a range or with curiosity, don't anchor low.

> "I'd rather understand the full scope and package before anchoring. My current total comp is [X], and I'd be looking for a meaningful step up to make a move — but I'm flexible if the overall opportunity is right. Can you share the band you're working with?"

**What great looks like:** Confident, not apologetic. Asks them to share first.

---

### Q6. "Notice period and availability?"

> "[X weeks/months]. I can start interviewing the rest of the loop immediately."

---

## Round 2 — Hiring Manager (Global Head of Core AI & ML) — 60 min

**Tone:** Senior, direct, will test depth and judgment. They've done this 100 times.

---

### Q7. "Walk me through your first 90 days in this role."

**Framework:** Inform → Optimize → Operate, with concrete deliverables per phase.

**Detailed answer:**
> "Days 1–30 is **Inform**. The first thing I do is build a single, defensible picture of the firm's AI footprint — every vendor, every API key, every self-hosted deployment, every developer tool like Cursor and Copilot. I'd pull billing from each provider, reconcile against AWS CUR for Bedrock, and produce a consolidated spend baseline. In parallel, I'd interview the top 10 consumers and the heads of the major desks to understand workloads, criticality, and what's actually painful. The deliverable at the end of month one is a one-pager: where the money goes, who spends it, what the top 5 risks are.
>
> Days 31–60 is **Optimize**. I pick the 3 highest-ROI levers. In my experience that's almost always: (1) close the attribution gap — most firms have 40-60% of calls untagged, so a central proxy with mandatory tagging is the foundation everything else depends on; (2) model routing — there's always a workload running on Opus that works fine on Sonnet, or on GPT-4o that works on 4o-mini; (3) prompt caching and batch API on the obvious candidates. I also start the weekly FinOps review with Eng and Procurement so we're not running this through Slack.
>
> Days 61–90 is **Operate**. We turn on showback for the top 5 cost centers — visibility only, no real billing yet — and that alone usually drives 15–25% cost reduction through behavior change. I publish the first monthly AI spend report to you and to desk heads. I draft the governance policy: budgets, model allow-lists, escalation runbooks. And I'd want to start the first vendor renegotiation conversation by day 90, because now we'd have clean usage data to negotiate from."

**Interviewer probes:**
- "What if attribution is harder than you think and takes 60 days?" → "Then I do optimization in parallel — I don't need 100% attribution to fix the obvious waste on the top 3 consumers we already know about."
- "What's the one thing you'd refuse to do in the first 90 days?" → "I wouldn't roll out chargeback. The data isn't clean enough yet and you'd lose trust with the desks. Showback first."

---

### Q8. "We have a quant PM running daily research summarization on Claude Opus. Spend is $200K/month. He's happy with the quality. What do you do?"

**Framework:** Don't kill it — measure it.

> "I don't touch the workload until I understand it. First, I'd sit with the PM or his lead engineer for an hour: what's the actual task, what does 'good output' look like, what's the worst failure mode, what's the downstream decision. Then I'd ask him to define quality formally — even a rough rubric on 50 samples works. With that rubric, I run a controlled comparison: same prompts on Opus vs Sonnet vs Haiku, scored blind. In my experience, 60-70% of tasks marketed as 'Opus-only' actually score the same on Sonnet — but until we've measured, we don't know which 60% are his.
>
> If the test confirms Sonnet works, I route easy summaries to Sonnet and keep the hard ones on Opus. That's typically a 60-70% cost reduction without quality loss. Then I layer prompt caching on the stable system prompt and corpus, and batch API since summarization is overnight. Realistic outcome: $200K/month becomes $50-70K/month.
>
> If Opus genuinely is required, then I shift to optimizing the call itself — caching, output length caps, structured output. I'd never tell the PM 'you can't use the best model.' My job is to make the best model affordable, not to substitute a worse one."

**What great looks like:** You don't reflexively cost-cut. You measure. You partner with the user. You quantify outcomes.

---

### Q9. "How do you negotiate with Anthropic for next year's renewal?"

**Framework:** Data → Leverage → Ask → Walk-away.

> "I'd walk in with four things:
>
> One — **clean usage data**. By now I'd have 6+ months of tagged usage showing model mix, peak vs sustained throughput, cache utilization, and growth trajectory. That's what lets me ask for the right things.
>
> Two — **leverage**. I'd have a current quote from OpenAI for equivalent capacity, and Bedrock pricing for Claude as a backup path. If Anthropic knows I can shift 30% of workload in 60 days, they negotiate differently.
>
> Three — **the ask is structured**: I want a committed-spend discount of X% at a commit level slightly below my forecast — never overcommit on year-one of a tier. I want a price-protection clause: if their list price drops more than 10% in the term, my rate adjusts. I want prompt-caching uplift if it's not already in the base, batch API access included, named technical contact for our top use cases, and a quarterly business review with their AE.
>
> Four — **the walk-away**: I know my BATNA. If they won't move below my walk-away number, I'm prepared to shift workload to OpenAI or Bedrock-routed Claude. I'd never bluff on this — but having the migration path actually built and tested is what makes the negotiation real.
>
> I'd run this jointly with Procurement and Legal — they own the paper, I own the technical and commercial logic."

**Interviewer probe:** "What's your BATNA actually look like — can you really migrate in 60 days?"
> "Honestly, only if I've architected for it. That's why on day one I'd push the firm toward a vendor-abstraction layer in our internal proxy — same SDK call, swap the backend. The proxy is the difference between having real leverage and just talking about it."

---

### Q10. "Tower already has an internal LLM proxy. What would you do differently to make it a chargeback-ready system?"

**Framework:** Identify the 4 gaps most internal proxies have, fix them.

> "Most internal proxies I've seen are built by engineers for engineers — they handle routing and auth but not financial-grade attribution. The four gaps I'd assess:
>
> (1) **Mandatory tagging**, not optional. Calls without team/project/cost-center/use-case get rejected after a grace period. Today most proxies log tags but don't enforce them.
>
> (2) **Price book.** The proxy needs to log not just tokens but a snapshot of the price applied — input price, cached input price, output price, model version — at the moment of the call. Otherwise back-calculating spend after a vendor price change is a nightmare.
>
> (3) **Reconciliation.** Daily job that reconciles proxy-logged usage against the vendor's reported usage. The delta is your data quality KPI; I'd target <1%.
>
> (4) **Exposed cost as a first-class API.** Other internal systems — budgets, finance, dashboards — should pull from one canonical cost API the proxy serves. Not three different queries against three different log stores.
>
> Once those are in place, chargeback is a SQL query, not a data engineering project."

---

### Q11. "What's the one thing you'd push back on me about in this role?"

**Framework:** Show you'd disagree professionally with data. This is a culture test.

> "Where I'd push back, gently, is if there's pressure to roll out chargeback before the data is clean. Chargeback is a one-shot trust event with desk heads — if the first statement has errors, you spend the next 12 months defending the system instead of using it. I'd advocate hard for 2-3 months of showback first, even if the firm feels it's losing time. The discipline pays for itself many times over.
>
> The flip side: I'd want clarity from you on the *one* metric that matters most. Is the goal absolute cost reduction, cost-per-output efficiency, or cost transparency? They lead to different trade-offs and I'd want us aligned on which we're optimizing."

**What great looks like:** Confident disagreement on a real technical issue, not posturing. Ends with a question that shows you want to partner with them.

---

### Q12. "What's your biggest weakness in this role?"

**Framework:** Genuine, with the work you're doing to address it.

**Example (adapt to truth):**
> "I'm stronger on the systems and quantitative side than on the formal procurement-and-legal contracting craft. I've negotiated vendor terms — but I haven't run a 50-page MSA redline cycle solo. I've been deliberately partnering more closely with Procurement and Legal on my current contracts to learn the muscles, and at Tower I'd lean on the Enterprise and Procurement teams the JD calls out. I'd own the commercial logic; I'd want them as full partners on the paper."

**What great looks like:** Real weakness (not "I work too hard"), specific, with active mitigation.

---

## Round 3 — Technical Deep Dive (60 min, possibly with an engineering lead)

**Tone:** Whiteboard / scenario-driven. They'll push on architecture and trade-offs.

---

### Q13. "Whiteboard: design the token attribution and chargeback system from scratch."

**Approach: 4 quadrants on the board.**

1. **Capture** (proxy)
2. **Store & enrich** (warehouse + price book)
3. **Compute** (allocation + chargeback engine)
4. **Consume** (dashboards, alerts, billing)

**Talk track:**
> "Top-left, **Capture**. A thin proxy — FastAPI or Envoy with a Lua filter — sitting in front of every external LLM API. Auth via SSO-issued team-scoped keys. Every request carries mandatory headers: team, project, cost_center, use_case, optionally user. Reject any call without them after a 30-day grace period. The proxy also captures: provider, model, model_version, input_tokens, output_tokens, cached_input_tokens, latency, status, request_id. For Bedrock, we use Application Inference Profiles so AWS does the per-call tagging; the proxy still logs metadata for cross-provider consistency.
>
> Top-right, **Store**. Async write to Kafka or Kinesis — never block the request path. Sink to a warehouse: Snowflake or BigQuery. Maintain a separate **price book table** with effective-dated rows per provider/model/token-type. Every usage row joins to the price book at the timestamp of the call. That's how we handle vendor price changes without breaking history.
>
> Bottom-right, **Compute**. Nightly batch rolls usage into cost-per-team, cost-per-project, cost-per-use-case. Add allocation logic for shared resources — PTU and fine-tuned models get pool-allocated by consumption. Output: a `monthly_chargeback` table that's the source of truth.
>
> Bottom-left, **Consume**. Three faces:
> - **Dashboards** (Looker / Tableau / Superset) for desk heads.
> - **Alerts** — real-time anomaly detection on $/hour per project, plus budget-threshold alerts (50%, 80%, 100%).
> - **Chargeback feed** to Finance — first 3 months showback, then real internal billing entries.
>
> Cross-cutting: trace IDs in the proxy log link to LangSmith or Langfuse traces so a $-anomaly investigation can drill from spend → tokens → call → step in the agent graph."

**Probes to expect:**
- "How do you handle privacy of prompts in the log?" → Log metadata only, never prompt content; or log to an isolated bucket with restricted access; or hash prompts for dedup-without-leakage.
- "How do you handle streaming?" → Token counts come from the final usage event in the SSE stream; same logging path, just deferred.
- "What about self-hosted models?" → Same proxy, model_provider='internal', token counting from the model's tokenizer; cost is amortized GPU-hour ÷ tokens served per period.
- "What's the failure mode if the warehouse is down?" → Kafka buffers up to 7 days; proxy never blocks; alarms fire after 1 hour of warehouse lag.

---

### Q14. "Walk me through how you'd detect and respond to a runaway agent burning $50K/hour."

**Framework: Prevent → Detect → Respond → Learn.**

> "**Prevent.** Every agent has compile-time and runtime caps: max tokens per session (say 200K), max recursion depth (say 25), max wall-clock (say 10 min), per-user-per-minute rate limit at the proxy. Tool outputs are length-capped before being fed back into context. These should be invisible in the normal case.
>
> **Detect.** Three parallel signals: (1) per-project $/hour with 3-sigma anomaly detection; (2) per-key call rate with hard threshold alerts; (3) trace-level alerts in LangSmith/Langfuse for recursion depth exceeded. The fastest signal usually wins — for cost spikes that's the per-key rate, which can fire within 60 seconds.
>
> **Respond.** Runbook: on-call engineer gets paged, immediately throttles the offending key at the proxy (don't kill outright — that breaks audit trails). 5-minute confirmation: real incident or noise? If real, escalate to me as L2; I have the authority to disable the key entirely. Slack incident channel opens. The team is looped in within 15 minutes — they almost always have the fastest fix.
>
> **Learn.** Post-mortem within 48 hours. Always-questions: was the agent's design at fault, or did a user provide pathological input, or was a tool returning oversized output? Update the guardrails. Add a regression test to the agent's eval suite. Publish the PIR to a shared library so other teams learn."

**Probe: "What if the runaway is in a trading-adjacent workflow and killing it has business risk?"**
> "Then the on-call doesn't kill it — they call me and the relevant desk lead simultaneously. We make the kill/throttle decision together with eyes on the business impact. The principle: cost controls never auto-kill production-critical flows. They alert, throttle gradually, and escalate."

---

### Q15. "When does Bedrock Provisioned Throughput beat on-demand?"

**Framework: Math + situational.**

> "On-demand is pay-per-token, infinite scale, zero commitment. PT reserves capacity in **model units** for 1-month or 6-month terms — you pay hourly whether or not you use the capacity. The math: take 30 days of on-demand baseline cost for the workload, then compare to (model_units × hourly_PT_rate × 720 hours). PT wins when:
>
> (1) Sustained utilization is roughly **60%+** of the reserved capacity — below that, you're paying for idle. (2) The workload needs throughput guarantees — Bedrock on-demand throttles can hit you during peak. (3) Latency consistency matters — PT has guaranteed latency, on-demand is best-effort. (4) The 6-month commit gives an additional discount over the 1-month, but I'd only do 6-month for workloads with 6 months of validated baseline.
>
> The trap is buying PT for forecasted demand that doesn't materialize. My rule: 30 days of on-demand minimum before any PT decision, and never PT more than 80% of forecast — keep the spiky overflow on on-demand."

**Probe: "What if the team insists on PT before you have baseline?"**
> "I'd ask them to put it in writing as a recommendation with their forecast and reasoning. Then I'd commit to 1-month PT at 50% of their forecast — capped risk. If utilization is high, we expand. If it's low, we walk back at the renewal point. That's a 4-week test, not a 6-month gamble."

---

### Q16. "What's the difference between LangChain agents and LangGraph, and why does it matter for cost?"

**Framework:**
> "LangChain's traditional agents — ReAct, plan-and-execute — are flexible but free-form. The agent decides what step to take next at runtime, and that's exactly where runaway cost happens: nothing prevents it from looping on a failed tool call or fanning out to too many sub-tools.
>
> LangGraph treats the agent as an explicit **state machine**. You declare nodes (steps) and edges (transitions). That gives you four cost properties LangChain doesn't:
>
> (1) **Bounded by design** — no edge means no transition; you can't accidentally infinite-loop.
> (2) **Per-node observability** — you can measure $ per node in LangSmith and find the expensive step.
> (3) **Checkpointing** — failed runs can resume from a checkpoint without re-running expensive prefix steps.
> (4) **Human-in-the-loop** — interrupt expensive nodes for review.
>
> For Tower, where agents may touch trading-adjacent workflows, I'd push hard for LangGraph or equivalent explicit-graph orchestration. LangChain agents have their place for prototyping; I wouldn't run an unbounded ReAct loop on a billed key in production."

---

### Q17. "How would you decide between LangSmith, Langfuse, and Helicone for Tower?"

**Framework: Match the firm's constraints.**

> "Three different sweet spots:
>
> **LangSmith** is the deepest LangChain/LangGraph integration — best traces, evals, datasets, prompt management. Downside: SaaS-only, your prompts and outputs sit on LangChain's infra. For Tower, that's a no-starter on sensitive workloads.
>
> **Langfuse** is open-source first. Self-hostable on your own infra, full feature set including evals and prompt management. Less polished than LangSmith but on a fast trajectory. For a prop trading firm where data residency matters, Langfuse self-hosted is the natural choice.
>
> **Helicone** is proxy-based — you point your SDK at their endpoint and get tracing + caching + rate limits for free. Easiest install. Less depth on evals and graph-aware tracing.
>
> My recommendation for Tower would be **Langfuse self-hosted** as primary observability — keeps data internal, gives us the eval and prompt-management muscles — combined with the firm's own proxy for the routing/caching/budget logic, so we don't take a dependency on Helicone's proxy. We'd use LangSmith only if a team has a deep LangChain investment and the data sensitivity allows."

---

## Round 4 — Cross-functional / Stakeholder Round (45 min)

**Tone:** Conversational, scenario-heavy. Often someone from Finance, Procurement, or a senior Eng leader.

---

### Q18. "Finance wants AI spend forecasted to ±10% accuracy by quarter. How?"

> "Forecasting LLM spend ±10% is hard because growth is non-linear and price-per-token drops mid-quarter. My approach is layered:
>
> **Bottom-up baseline.** Last 90 days of usage by team and use case, with a trend line on each. That's the 'steady state' forecast.
>
> **Pipeline overlay.** Active projects with launch dates and estimated volumes — get them from the team leads, not from guesswork. I'd track these in a simple intake form.
>
> **Vendor price view.** Known committed-spend rates, known PT commitments, expected list-price changes (when announced). Built into the price book as effective-dated rows.
>
> **Buffer.** A discrete 10-15% contingency line for unknowns — new tools, capability releases, experimental workloads. Explicit, not hidden in line items.
>
> Variance review monthly: actual vs forecast by team, with explanations. After 2 quarters the forecast tightens because the unknowns become knowns. I'd commit to ±15% in quarter one and ±10% from quarter two."

---

### Q19. "Procurement wants a single preferred AI vendor to reduce vendor management overhead. What's your position?"

> "I'd push back firmly. Single-vendor sounds clean but it's strategically fragile: this market re-prices every 6 months and capability gaps reshuffle annually. Last year Claude was behind on coding; this year it's ahead. Locking in is yesterday's bet.
>
> My counter-proposal: **strategic dual-source plus aggregator.** OpenAI and Anthropic as primaries, with AWS Bedrock as an aggregation layer. That gives us:
> - Real renegotiation leverage every cycle.
> - Outage hedging — both have had multi-hour incidents this year.
> - Best-model-for-task at the workload level.
> - AWS billing consolidation through Bedrock for the workloads we route there.
>
> The overhead cost — extra MSAs, extra integrations — is 5-10% in eng and procurement time. The cost savings from leverage alone usually pay for it 3-5x. I'd present it that way to Procurement: 'Here's the dollar cost of single-source vs multi-source. Here's the leverage value. The math says multi-source.'"

---

### Q20. "A trading PM is convinced his agent is producing alpha-generating ideas. He wants 10x his current $/month limit, no questions. What do you do?"

> "I say yes — and then I ask one question.
>
> 'Yes' because if the workload is genuinely producing alpha, the cost is irrelevant. The worst thing I can do as the AI ops manager is be the person who gates a PM's strategy on a budget line.
>
> The one question: 'Can we instrument it together?' Not to gatekeep — to learn. I want to understand what's actually driving the cost, whether the productive part of the agent is 10% of calls or 90%, and whether we can keep the productive part while trimming the rest. If 80% of the spend is on retries and tool-loop overhead, we can fund his expansion *and* reduce per-idea cost. That's the win-win.
>
> I'd also use this as a forcing function to get our cost-per-business-outcome metric defined for trading workflows — once we can measure $/idea-that-traded, every PM gets a much more honest conversation."

**Probe: "What if the agent is actually pathological and burning cash?"**
> "Then I find that out in the instrumentation, and I bring it back to the PM with data. 'Here's what we found. 70% of your spend is here. Here's what changing it costs you in quality. You decide.' I never override a PM unilaterally on a workload they own — but I never duck the data conversation either."

---

### Q21. "You inherit a team of 3 ops engineers in different time zones. How do you operate?"

> "Three principles.
>
> **Follow-the-sun L1.** Each region owns their working-hours triage. Clear playbooks. PagerDuty routes by region + service + severity. I sit on top as L2 / global owner.
>
> **One source of truth.** A single internal wiki for runbooks, dashboards, escalation paths, and incident retrospectives. No tribal knowledge.
>
> **Weekly all-hands and 1:1s on a rotation that's fair to everyone's time zone — not always the APAC team taking the 10pm call.** That's an easy thing to get wrong and it builds resentment fast.
>
> I'd also be honest about expectations: as the global owner I'm reachable in major incidents regardless of time zone, but I don't expect the team to be. We document, we hand off, we trust each other."

---

## Round 5 — Final Round (with Global Head / Senior Leadership) — 45 min

**Tone:** Strategic, candid, judgment-focused. They're deciding if they want to work with you, not just hire you.

---

### Q22. "Six months in, what would 'success' look like to you in this role?"

> "Three things, in priority order.
>
> One — **A defensible, single number for firm-wide AI spend that your CFO trusts.** That sounds basic but most firms don't have it. If by month six I can hand you a chart that shows the firm's AI spend, by team, by use case, by provider, with <1% reconciliation gap, that's the foundation everything else stands on.
>
> Two — **20-30% in-flight cost reduction from quick wins** — prompt caching, model routing, batch API, eliminating orphan keys and dead workloads. This shouldn't be hard if attribution is clean.
>
> Three — **The governance scaffolding the firm needs as AI scales 5x in the next 18 months.** Policies, budgets, escalation paths, vendor management cadence. So that when the next vendor capability releases or the next desk wants to spin up an agent platform, we have a process — not a fire drill.
>
> The thing I'd be measured by but I'd hold myself to a higher bar on: whether desk heads see me as a partner who unblocks them or a tax collector. Six months in, I want at least two PMs telling you unprompted that AI ops made their team faster, not slower."

---

### Q23. "What do you think is the most important problem in AI ops that nobody's solving yet?"

**Framework:** Show original thinking. Pick a real gap.

> "I think the unsolved problem is **cost-per-business-outcome** — not just $/token or $/call. Every vendor's dashboard and every observability tool measures input metrics: tokens, latency, calls. None of them measure what you actually care about: did this $X of spend produce a trade idea that worked, a PR that merged, a customer ticket that closed?
>
> The reason is hard: business outcomes are firm-specific. There's no SaaS product that knows what 'success' means for Tower's research workflow. So the firm has to instrument it themselves — define the outcome events, log them, join them to the usage data. That's the work I'd want to push toward in the second half of year one. Once we have it, the conversation with PMs and desk heads transforms — we're not arguing about $/token, we're arguing about $/idea-that-traded. That's a much healthier conversation."

---

### Q24. "Anything you want to ask me?"

**Have 4–6 ready. Pick 3 based on the conversation flow.**

1. "What's the firm's current run-rate on external LLM spend, and what's the trajectory?"
2. "How is AI ROI currently measured — at the firm, desk, or use-case level?"
3. "What would success in this role look like from your perspective at 6 months and 12 months?"
4. "What separates someone who's great in this role from someone who's just good?"
5. "What's the biggest open problem on the AI ops side today that you'd want me thinking about before I started?"
6. "How do you see Core AI & ML evolving over the next two years, and where does this role fit in that picture?"

**Don't ask:**
- Anything you could Google.
- Anything about comp, benefits, vacation in this round — save for the recruiter.
- "What's it like to work here?" (lazy).

---

## Self-grading rubric (use after each practice pass)

For each answer, score yourself 1–5:

- **Structure (1-5):** Did I open with a framework or a number, not a meander?
- **Specificity (1-5):** Did I use concrete numbers, vendor names, technical terms?
- **Trade-offs (1-5):** Did I acknowledge what I'd give up to get the benefit I described?
- **Tower-fit (1-5):** Did I tie back to prop trading / Tower's context, not generic SaaS?
- **Brevity (1-5):** Was I done in 90 seconds (recruiter) / 2-3 min (technical) / 3-4 min (strategic case)?

**Target:** 4+ across all five categories on every question by pass 3.

---

*Run this script three times. After pass 3, you'll be tighter, faster, and calmer than 90% of the candidates in that loop. Good luck.*
