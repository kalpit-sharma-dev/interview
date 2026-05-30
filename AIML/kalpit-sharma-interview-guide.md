# Kalpit Sharma — End-to-End Interview Preparation Guide

> **Profile:** 13+ years IT · AVP, HDFC Bank · Leading **~20** (mobile banking backend) + **~6** (AI Banking) · Golang primary · GenAI/agents (Python) · M.Tech AI/ML & DE (IIT Jodhpur) · Banking (HDFC, HSBC) + platform (ConnectWise) + regulatory (Barclays)  
> **Contact:** kalpit.cool2006@gmail.com · [LinkedIn](https://www.linkedin.com/in/kalpit-sharma/)

This is your **master playbook**. Technical depth lives in other AIML docs; this file tells you **which roles to target**, **how to position your resume**, **what stories to tell**, and **how to prepare week by week**.

---

## Table of Contents

1. [Executive Summary — Best Roles for You](#1-executive-summary--best-roles-for-you)
2. [Profile Strengths & Gaps](#2-profile-strengths--gaps)
3. [Role Fit Matrix (Ranked)](#3-role-fit-matrix-ranked)
4. [Roles to Apply vs Avoid](#4-roles-to-apply-vs-avoid)
5. [Resume Positioning](#5-resume-positioning)
6. [Your Core Narrative (30-Second Pitch)](#6-your-core-narrative-30-second-pitch)
7. [STAR Stories from Your Experience](#7-star-stories-from-your-experience)
8. [AI Banking (AI Skin) — Deep Dive for Interviews](#8-ai-banking-ai-skin--deep-dive-for-interviews)
9. [Management & Leadership Stories](#9-management--leadership-stories)
10. [Technical Revision Map (AIML Library)](#10-technical-revision-map-aiml-library)
11. [Interview Loops by Role Type](#11-interview-loops-by-role-type)
12. [Coding Preparation (600+ Leetcode + GenAI)](#12-coding-preparation-600-leetcode--genai)
13. [6-Week Preparation Calendar](#14-6-week-preparation-calendar)
14. [Company Research Checklist](#15-company-research-checklist)
15. [Day-Before & Interview-Day Checklist](#16-day-before--interview-day-checklist)
16. [Honest Readiness Scorecard](#17-honest-readiness-scorecard)
17. [ML/DL/NLP/MLOps Q&A Bank](#18-ml--dl--nlp--mlops--500-qa-bank)

---

## 1. Executive Summary — Best Roles for You

You are **not** a junior GenAI IC and **not** a pure research data scientist. Your rare combination is:

**Large-scale banking backend leadership + hands-on GenAI/agents + architecture (C4, gRPC, GCP) + team scale (26 people).**

### Top 3 best-fit role types (in order)

| Rank | Role type | Why you fit |
|------|-----------|-------------|
| **1** | **AI Engineering Manager / Senior Engineering Manager (AI + Platform)** — product co, fintech, enterprise bank tech | You already lead a **dedicated AI squad (6)** inside a **major regulated domain**; AVP title; agents + RAG + MCP; can speak product + compliance + scale |
| **2** | **Staff / Principal Engineer — GenAI Platform or Banking AI** | If you want **IC track**: 13 yrs, Golang platform depth, AI Banking builder, Leetcode strong, architecture owner |
| **3** | **Head of Engineering / Director — Digital Banking or AI Enablement** (BFSI or vendor serving banks) | 20-person backend + AI initiative; HSBC/HDFC/Barclays domain; executive stakeholder exposure (typical at AVP) |

### Strong secondary fits

| Role | Fit | Caveat |
|------|-----|--------|
| **Agentic / GenAI Engineer (Staff / Lead)** | Hands-on RAG, LangChain, MCP, FastAPI | Target **Staff/Lead**, not mid-level IC — otherwise you look overqualified |
| **Engineering Manager — Backend/Platform (with AI charter)** | Golang, Kafka, K8s, GCP, 20-team lead | Emphasize AI as **growth vector**, not only legacy backend |
| **Solution / Principal Architect — BFSI AI** | C4 diagrams, microservices, regulatory background | Need 2–3 **named** architecture decision stories with tradeoffs |

### Weaker fits (unless company is flexible)

| Role | Why |
|------|-----|
| **Pure Data Scientist** | Career is engineering-led; ML projects are academic/GitHub, not 5 yrs production DS |
| **AI Ops / FinOps only (Tower-style)** | You have observability (Grafana/OTel) but not primary career in token chargeback / procurement |
| **Mid-level GenAI IC (5–8 yr bar)** | You will be bored; interviewers may think you won’t stay |

### Recommended job objective (rewrite)

**Current (generic):** “leadership role in scalable AI-driven systems…”

**Stronger:**

> Engineering leader (Manager or Staff+) building **regulated, production GenAI and agentic systems** on **Golang/Python microservices** — RAG, MCP, tool orchestration — with proven delivery in **banking at scale** and teams of **20+**.

---

## 2. Profile Strengths & Gaps

### Strengths (lead with these)

| Strength | Evidence |
|----------|----------|
| **Scale & leadership** | ~26 engineers (20 backend + 6 AI); AVP at top-tier bank |
| **Regulated domain** | HDFC mobile banking, HSBC retail, Barclays SDR/MiFID |
| **Platform engineering** | Golang, Kafka, gRPC, Cassandra/Postgres, multi-DC, GCP |
| **GenAI production path** | AI Skin: agents, MCP, RAG, orchestration, Golang + Python |
| **Architecture** | C4, ER, API specs — speaks to architect panels |
| **Observability** | Grafana, OpenTelemetry |
| **Academic upskilling** | M.Tech AI/ML & DE (IIT Jodhpur) — signals DE/DS foundation for GenAI JDs |
| **Coding** | 600+ Leetcode — systems + DSA rounds |
| **Portfolio** | GitHub: emotion recognition, log pipeline, flight DE project |

### Gaps (address proactively)

| Gap | How to fix in interview |
|-----|-------------------------|
| **“3+ years managing AI/ML engineers”** (some EM JDs) | Frame: “**6 direct AI Banking** + **20 backend** with AI platform dependency; hiring, 1:1s, delivery ownership” |
| **Python yrs vs Golang** | “**Production AI in Python**; **platform integration in Golang**” — intentional split |
| **Quantified GenAI metrics** | Add to stories: latency, accuracy/groundedness, cost, users, incident MTTR (**use real numbers**) |
| **Pure DE title** | Lead with **log-monitoring pipeline**, **Flight-Delay DE phases**, **M.Tech DE** for mandatory DE JDs |
| **LangGraph** (JD often lists it) | Map **LangChain / Crew.ai / Semantic Kernel / Swarm** experience; 1 LangGraph tutorial if gap |
| **Azure OpenAI / AI Search** | You have **GCP** — learn Azure mapping (1 day); see [GenAI engineer prep §10](./agentic-genai-engineer-interview-prep.md#10-azure--multi-cloud-good-to-have) |

---

## 3. Role Fit Matrix (Ranked)

Score: **9–10** = apply aggressively · **7–8** = strong with tailoring · **5–6** = only if brand/comp matters

| Role | Score | Notes |
|------|-------|-------|
| AI Engineering Manager (product / fintech / bank tech) | **9/10** | Match JD you shared earlier; use EM pack + this guide |
| Staff / Principal — GenAI or AI Platform | **9/10** | Best if you prefer IC influence without HR-heavy EM |
| Director / Head of Eng — AI or Digital (BFSI) | **8/10** | Needs executive storytelling, budget, vendor mgmt |
| Agentic GenAI Engineer — **Staff / Lead** | **8/10** | Use [GenAI IC pack](./agentic-genai-engineer-interview-prep.md); don’t down-level title |
| Engineering Manager — Backend (AI charter) | **8/10** | Easy hire profile; confirm AI roadmap ownership |
| Solution Architect — Enterprise AI | **7/10** | Strong on diagrams + banking; add 2 ADR stories |
| AI Ops / FinOps Manager | **6/10** | Tower prep helps; not your primary brand |
| Pure Data Scientist | **4/10** | Poor fit unless hybrid “DS + eng” |

---

## 4. Roles to Apply vs Avoid

### Apply when JD mentions

- AI agents, RAG, LLM orchestration, MCP  
- Banking / fintech / regulated enterprise  
- Golang or polyglot backend + Python AI  
- Engineering manager / staff / principal / AVP-Director  
- GCP or cloud-native, K8s, microservices  
- **Leadership of ML/AI or platform teams**

### Be cautious when JD is

- “**5–8 years** GenAI engineer” only (no leadership) — negotiate **Lead/Staff**  
- “**PhD + 5 yrs research**” — misaligned  
- “**Only PyTorch research**” — highlight IIT + emotion recognition, but lead with production  
- “**Only AWS Bedrock FinOps**” — use Tower folder, not core identity  

---

## 5. Resume Positioning

### Front-load (top third of page)

1. **Title line:** `Assistant Vice President — Engineering | AI Banking & Mobile Platform (HDFC Bank)`  
2. **One-line impact:** e.g. “Lead **26 engineers**; shipped **AI Skin** (agents, MCP, RAG) on **GCP** integrated with mobile banking microservices.”  
3. **Skills:** Split **Leadership** | **GenAI** | **Platform (Golang)** | **Cloud/Data**

### AI Banking bullet template (fill real metrics)

- Led squad of **6** building **AI Skin** — agentic workflows, **MCP** tool servers, **RAG** over banking knowledge; integrated with **Golang/gRPC** services on **GCP**.  
- Improved **[metric]** by **[X%]**; p95 latency **[Ys]**; **[N]** internal users / customers.  
- Established **[eval/guardrail]** — citation policy, PII handling, human approval for **[action]**.

### Backend leadership (20 team)

- Own **mobile retail banking** microservices (**Golang**, Pub/Sub, Aerospike, Postgres, **GCS**).  
- **[Availability/latency]** SLOs; **OTel/Grafana** observability; release train with **[Agile/CI tool]**.

### M.Tech — one line under education

“Coursework: ML, NLP, data engineering pipelines — applied to **AI Banking** and capstone projects.”

### GitHub — tie to DE/GenAI JD

| Repo | Interview line |
|------|----------------|
| log-monitoring | “End-to-end **DE pipeline**: Kafka → ES → Grafana; same patterns as log/RAG ingestion SLAs” |
| flight-analysis | “**ELT, warehousing, ML** — proves DE lifecycle” |
| Face-Emotion-Recognition | “CNN training/deployment (**TensorFlow**, Flask) — classic ML lifecycle” |

---

## 6. Your Core Narrative (30-Second Pitch)

“I’m an engineering leader with **13 years** building **high-scale backend systems**, currently **AVP at HDFC Bank** leading **mobile banking platform** and an **AI Banking** squad. My team ships **Golang microservices** on **GCP** for millions of customers, and our **AI Skin** initiative delivers **agentic and RAG-based** capabilities using **Python orchestration**, **MCP tools**, and integration back into the same secure banking stack. I’m **hands-on** on architecture and code review, with **600+ Leetcode** and an **M.Tech in AI/ML and Data Engineering from IIT Jodhpur**. I’m looking for a **[Manager / Staff]** role where I can scale **production GenAI in a regulated product company**.”

---

## 7. STAR Stories from Your Experience

Prepare **8 stories** (2–3 min each). **Replace bracketed text with real metrics.**

### Story A — AI Banking delivery (GenAI / agents)

- **S:** HDFC needed **[AI feature]** in mobile banking without compromising security.  
- **T:** Lead **6** engineers; deliver MCP + RAG + agent orchestration integrated with Golang services.  
- **A:** Architecture with **[diagram]**; prompt/tool guardrails; phased rollout; eval on **[golden set]**.  
- **R:** **[Users/adoption]**, **[latency]**, **[quality metric]**, zero **[SEV]** or **[how handled]**.

### Story B — Scale & reliability (20-person backend)

- **S:** Mobile banking peak load / **[festival launch]**.  
- **T:** Ensure **[SLO]** during **[event]**.  
- **A:** Capacity planning, Kafka/PubSub tuning, Aerospike/Postgres optimization, observability dashboards.  
- **R:** **[uptime %]**, **[p95 latency]**, **[incident count]**.

### Story C — ConnectWise platform (technical leadership IC→lead)

- **S:** Multi-product sync to unified platform.  
- **T:** Design sync for **Company/Site/Contact** using **Lambda + Step Functions**.  
- **A:** API specs, idempotent sync, Kafka for ticket pipeline elsewhere.  
- **R:** **[sync volume]**, reduced **[manual work/errors]**.

### Story D — Regulatory / compliance mindset (Barclays)

- **S:** SDR/MiFID reporting — message orchestration to **DTCC/CFTC**.  
- **T:** Migration + accurate transformation pipelines.  
- **A:** Validation workflows, auditability, performance tuning.  
- **R:** Reliable regulatory delivery; **link to AI**: “same rigor for **audit logs** on agent tool calls.”

### Story E — DE foundation (log-monitoring GitHub / IIT)

- **S:** Need real-time log analytics at scale.  
- **T:** Build pipeline Kafka → Logstash → ES → Kibana/Grafana.  
- **A:** Golang + Python components; anomaly goals.  
- **R:** **[throughput]**, **[alert time]** — “this is how I think about **RAG ingestion SLAs**.”

### Story F — Conflict / prioritization

- **S:** Product wanted **[big AI scope]** mid-release.  
- **T:** Protect mobile banking stability + deliver AI milestone.  
- **A:** Phased roadmap; read-only RAG first; **[said no]** to risky autonomy with data.  
- **R:** Shipped **[MVP]** on date; **[metric]**.

### Story G — Hiring / mentoring

- **S:** Team needed **[Golang/Python/AI]** skills.  
- **T:** Hire and upskill.  
- **A:** Structured interviews, pairing, RFC reviews.  
- **R:** **[hires]**, **[promotion or productivity metric]**.

### Story H — Failure / incident

- **S:** **[Outage / bad retrieval / cost spike]**.  
- **T:** Restore service + prevent recurrence.  
- **A:** MTTR actions, postmortem, eval/alert added.  
- **R:** **[MTTR]**, no repeat in **[N months]**.

---

## 8. AI Banking (AI Skin) — Deep Dive for Interviews

Interviewers will probe **one project** deeply. Prepare this fact sheet:

| Topic | Your answer (fill in) |
|-------|------------------------|
| **User** | Internal staff / customers? Which journeys? |
| **Architecture** | Python orchestration ↔ Golang services ↔ Postgres/Aerospike ↔ GCS docs |
| **RAG** | Source documents, chunk strategy, vector store, ACL model |
| **Agents** | Single vs multi-agent; frameworks (LangChain, Crew.ai, SK, Swarm) |
| **MCP** | Which servers; tool boundaries; auth |
| **Models** | Claude/GPT/Gemini; routing; why |
| **Safety** | PII, prompt injection, HITL for transactions |
| **Eval** | Golden questions, regression, human review % |
| **Metrics** | Latency, cost per query, task success, incidents |
| **CI/CD** | How prompts/models deploy; canary |

**Whiteboard diagram to practice:**

```
Mobile App → API Gateway → Golang services → AI Orchestrator (Python)
                → MCP tools / Core banking APIs
                → RAG (GCS docs → embed → vector store)
                → LLM → Guardrails → Response
```

---

## 9. Management & Leadership Stories

For **AI Engineering Manager** loops, emphasize:

| Theme | Your HDFC angle |
|-------|-----------------|
| **Team topology** | 20 backend + 6 AI — coordination, dependencies, release alignment |
| **Career development** | 1:1s, growth paths Golang ↔ Python AI |
| **Performance** | Delivery metrics, not vanity AI demos |
| **Stakeholders** | Product, compliance, infra, MLOps on GCP |
| **Innovation budget** | AI Skin as incubation with production gates |

Use [ai-em-mock-interview-qa.md](./ai-em-mock-interview-qa.md) — replace generic examples with **your** AVP stories.

---

## 10. Technical Revision Map (AIML Library)

| If interviewing for… | Read / practice |
|----------------------|-----------------|
| **AI Engineering Manager** | [ai-engineering-manager-interview-prep](./ai-engineering-manager-interview-prep.md) → [mock Q&A](./ai-em-mock-interview-qa.md) → [cheat sheet](./ai-em-interview-cheat-sheet.md) |
| **Agentic / GenAI Engineer (Staff)** | [agentic-genai-engineer-interview-prep](./agentic-genai-engineer-interview-prep.md) → [mock Q&A](./agentic-genai-engineer-mock-interview-qa.md) → [coding practice](./agentic-genai-engineer-coding-practice.md) |
| **Technical depth (all)** | [guide-to-ai-agent](./guide-to-ai-agent.md) + [master-ai-agent-guide](./master-ai-agent-guide.md) |
| **AI cost / Bedrock / chargeback** | [TowerResearch/](./TowerResearch/) |
| **This role — you** | **This file** + one pack above |

---

## 11. Interview Loops by Role Type

### AI Engineering Manager (5–6 rounds typical)

1. Recruiter — level, compensation, **why leave HDFC**  
2. Hiring manager — leadership, roadmap, AI Skin story  
3. System design — enterprise RAG/agent in **banking**  
4. Technical deep dive — RAG eval, tools, MCP, Golang integration  
5. Behavioral — STAR, conflict, underperformer  
6. Bar raiser / VP — strategy, culture, compliance  

### Staff / Principal IC (4–5 rounds)

1. Hiring manager — scope & influence without direct reports  
2. Coding — Leetcode medium + **[coding practice](./agentic-genai-engineer-coding-practice.md)**  
3. System design — platform + RAG/agent  
4. Deep dive — AI Skin architecture  
5. “Cross-team” — how you influence 20-person backend org  

### Agentic GenAI Engineer Staff (4 rounds)

1. RAG + agent deep dive  
2. Live coding / take-home (FastAPI + retrieval)  
3. DE/DS mandatory story — **log-monitoring + IIT + M.Tech**  
4. Culture / collaboration  

---

## 12. Coding Preparation (600+ Leetcode + GenAI)

| Week focus | Activity |
|------------|----------|
| **Maintenance** | 3–5 Leetcode mediums/week (graphs, heaps, concurrency) |
| **GenAI** | Complete [coding practice](./agentic-genai-engineer-coding-practice.md) exercises 1–6 |
| **Systems** | Rate limiter, idempotency, cache — explain in banking context |
| **Live** | Practice thinking aloud — interviewers know your 600+ score; don’t skip **design narration** |

---

## 13. 6-Week Preparation Calendar

| Week | Goals |
|------|--------|
| **1** | Finalize 8 STAR stories with **real metrics**; update resume; read this guide + [GenAI IC prep](./agentic-genai-engineer-interview-prep.md) OR [EM prep](./ai-engineering-manager-interview-prep.md) based on target role |
| **2** | [guide-to-ai-agent](./guide-to-ai-agent.md) full pass; draw AI Skin architecture from memory |
| **3** | [master-ai-agent-guide](./master-ai-agent-guide.md); 2 timed system designs (support copilot, B2B RAG) |
| **4** | [Mock Q&A](./agentic-genai-engineer-mock-interview-qa.md) or [EM mock](./ai-em-mock-interview-qa.md) — **10 answers aloud**, recorded |
| **5** | [Coding practice](./agentic-genai-engineer-coding-practice.md); Leetcode concurrency; Azure/GCP mapping if JD requires |
| **6** | Cheat sheet only; company research; mock with friend; prepare **questions for them** |

---

## 14. Company Research Checklist

- [ ] Product: how AI appears in UX (copilot, search, automation)  
- [ ] Stack: GCP vs Azure vs AWS (map your GCP HDFC experience)  
- [ ] Regulatory posture (bank / fintech / SaaS)  
- [ ] Team size & reporting (EM vs Staff)  
- [ ] Recent news, funding, AI announcements  
- [ ] 3 smart questions (eval harness, agent vs RAG split, promotion path)  

---

## 15. Day-Before & Interview-Day Checklist

**Day before**

- [ ] Re-read [cheat sheet](./agentic-genai-engineer-cheat-sheet.md) OR [EM cheat sheet](./ai-em-interview-cheat-sheet.md)  
- [ ] AI Skin diagram on paper  
- [ ] 3 STAR stories refreshed  
- [ ] Questions for interviewer written  

**Interview day**

- [ ] Lead with **leadership + regulated production**, not “I did Leetcode”  
- [ ] Every answer: **context → action → metric → learning**  
- [ ] For unknowns: “At HDFC we’d …” or structured tradeoff, not bluff  

---

## 16. Honest Readiness Scorecard

| Target role | AIML docs + your experience | After 6-week plan |
|-------------|----------------------------|-------------------|
| **AI Engineering Manager** | **Strong** — lead with 6+20 team, AI Skin | **Very strong** if STAR metrics filled |
| **Staff / Principal GenAI** | **Strong** — platform + agents | **Very strong** + coding practice |
| **Agentic GenAI IC (mid)** | Overqualified — risk of mismatch | N/A — aim Staff/Lead title |
| **Director / Head (bank)** | **Good** — need executive/budget stories | Add 2 business-impact narratives |
| **Pure DS** | Weak | Don’t optimize resume for this |

### Are all AIML files + Tower enough?

| Corpus | Enough alone? |
|--------|----------------|
| **3 agent/EM/GenAI packs + this guide** | **~60–70%** with your **real HDFC stories** |
| **+ TowerResearch** | Adds cost/FinOps for platform/ops interviews |
| **+ mocks + metrics + 6-week plan** | **Interview-ready** for Manager / Staff GenAI in BFSI/product |

**Nothing replaces:** practicing aloud, filling **quantified** AI Skin metrics, and targeting the **right seniority** in the job title.

---


## 18. ML / DL / NLP / MLOps — 500+ Q&A bank

For drill and rapid revision use **[kalpit-ml-dl-nlp-mlops-interview-500-qa.md](./kalpit-ml-dl-nlp-mlops-interview-500-qa.md)** (**783 questions**) covering:

- Machine learning fundamentals & statistics  
- Deep learning & transformers  
- NLP, LLMs, RAG, agents (market 2025–26)  
- MLOps, data engineering, GCP/production  
- Banking leadership behavioral  
- Python/Golang/cloud for ML  

**Study method:** 5–10 questions/day; each answer has **short opener + detailed explanation + practice + pitfalls**. Read aloud until you can teach without notes. Prioritize sections for your target JD (GenAI IC → NLP/LLM/MLOps; EM → leadership + system design).

**Note:** Answers are **detailed for learning** (~1–2 min read each). Customize *For your profile* with real AI Skin metrics.

## Quick links

- [500+ ML/DL/NLP/MLOps Q&A](./kalpit-ml-dl-nlp-mlops-interview-500-qa.md)
- [AIML README](./README.md)  
- [Your coding drills](./agentic-genai-engineer-coding-practice.md)  
- [GenAI Engineer prep](./agentic-genai-engineer-interview-prep.md)  
- [AI EM prep](./ai-engineering-manager-interview-prep.md)  

*Last updated for profile: Kalpit Sharma — May 2026*
