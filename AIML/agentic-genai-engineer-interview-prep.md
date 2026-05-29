# Agentic / Generative AI Engineer — Interview Preparation

> **Role:** IC — design, build, deploy LLM-powered & agentic systems for enterprise  
> **Experience band:** 5–12 years total · **1–3+ years** production LLM apps preferred  
> **Mandatory:** Prior **Data Engineering** or **Data Science** background (pipelines, ML lifecycle, or analytics engineering)

**Quick access:** [Cheat Sheet](./agentic-genai-engineer-cheat-sheet.md) · [Mock Q&A](./agentic-genai-engineer-mock-interview-qa.md)

**Technical depth (read these):**

- [Guide to AI Agent](./guide-to-ai-agent.md) — RAG, tools, APIs, testing, compliance, lifecycle  
- [Master AI Agent Guide](./master-ai-agent-guide.md) — LangGraph, multi-agent, K8s, security, production structure  

**Less relevant for this loop:** [AI Engineering Manager prep](./ai-engineering-manager-interview-prep.md) (leadership-heavy). **Supplement:** TowerResearch folder for cost/observability depth.

---

## Table of Contents

1. [JD → What Interviewers Probe](#1-jd--what-interviewers-probe)
2. [Competency Rubric](#2-competency-rubric)
3. [Mandatory DE/DS Background — How to Prove It](#3-mandatory-deds-background--how-to-prove-it)
4. [RAG End-to-End (Core Skill)](#4-rag-end-to-end-core-skill)
5. [Agentic Systems (Single & Multi-Agent)](#5-agentic-systems-single--multi-agent)
6. [Prompt Engineering & Orchestration](#6-prompt-engineering--orchestration)
7. [Production APIs & Integration](#7-production-apis--integration)
8. [Guardrails, Safety & Evaluation](#8-guardrails-safety--evaluation)
9. [Collaboration: Data Eng, MLOps, Product](#9-collaboration-data-eng-mlops-product)
10. [Azure & Multi-Cloud (Good-to-Have)](#10-azure--multi-cloud-good-to-have)
11. [Fine-Tuning vs RAG vs Agents](#11-fine-tuning-vs-rag-vs-agents)
12. [Coding & System Design Expectations](#12-coding--system-design-expectations)
13. [Portfolio & Stories to Prepare](#13-portfolio--stories-to-prepare)
14. [Likely Questions Checklist](#14-likely-questions-checklist)
15. [10-Day Study Plan](#15-10-day-study-plan)
16. [Corpus Coverage — Is AIML Enough?](#16-corpus-coverage--is-aiml-enough)

---

## 1. JD → What Interviewers Probe

| JD line | Interview signal |
|---------|------------------|
| Agentic LLM solutions (single/multi-agent) | Architecture diagram, tool design, when **not** to use agents |
| RAG end-to-end | Ingestion → chunk → embed → retrieve → synthesize; **metrics** |
| Prompt orchestration, cost/latency | Chains, routers, caching, model selection |
| Production APIs (FastAPI) | Async, idempotency, auth, streaming, background jobs |
| Guardrails + eval | Golden set, groundedness, injection tests, HITL |
| Work with Data Eng / MLOps | Data contracts, CI/CD, monitoring, lineage |
| Documentation & reusable components | RFC mindset, libraries, prompt registry |
| **Mandatory DE or DS** | Concrete pipeline or modelling story with scale |
| Claude + LangChain/LangGraph | Model tradeoffs, framework choice |
| Azure AI Search / Azure OpenAI | Index design, private networking, content safety |

---

## 2. Competency Rubric

| Area | Strong (hire) | Weak (pass) |
|------|---------------|-------------|
| **RAG quality** | Explains chunking, eval, rerank, failure modes | “We embedded and called GPT” |
| **Agents** | Max steps, tool validation, HITL for writes | Unbounded ReAct loop |
| **Engineering** | Tests, types, structured logs, CI eval gates | Notebook-only |
| **Data foundations** | ETL, schema, freshness, governance | Ignores source data quality |
| **Measurement** | Accuracy, latency, cost per successful task | No metrics |
| **Security** | PII, ACL on retrieval, injection awareness | Prompt-only security |
| **Communication** | Tradeoffs in business terms | Jargon without outcomes |

---

## 3. Mandatory DE/DS Background — How to Prove It

Interviewers **will disqualify** candidates who only have chatbot demos without data depth. Prepare **at least two** stories:

### Data Engineering story

- **Pipeline:** sources → orchestration (Airflow/Dagster/dbt/Spark) → curated tables  
- **Scale:** volume, freshness SLA, backfills  
- **Quality:** tests, schema contracts, lineage  
- **Link to GenAI:** “This curated corpus became our RAG knowledge base with document IDs tied to warehouse tables.”

### Data Science / ML story

- **Problem:** classification, ranking, NLP, forecasting  
- **Lifecycle:** train/val/test, leakage checks, deployment, monitoring drift  
- **Link to GenAI:** “We reused evaluation discipline—golden sets and regression tests—for LLM outputs.”

### Analytics engineering angle

- Semantic layer, metrics definitions, self-serve BI → “GenAI assistant grounded on **approved metrics definitions** only.”

**One-liner for interviews:**

> “I’m not only prompting models—I own the **data path** that makes retrieval trustworthy and the **eval path** that proves it in production.”

---

## 4. RAG End-to-End (Core Skill)

### Pipeline (know cold)

```
Sources (SharePoint, S3, DB, tickets)
  → Ingestion (schedule, ACL metadata)
  → Parse (PDF/HTML/OCR)
  → Chunk (size, overlap, semantic)
  → Embed (model version recorded)
  → Index (vector + optional BM25 hybrid)
  → Query: embed + filter + top-k + rerank
  → Synthesis (citations required)
  → Eval (offline + online sample)
```

### Quality levers (rank by impact)

1. **Source data quality** and ACL-aware retrieval  
2. **Chunking** matched to document structure  
3. **Hybrid search** + **reranker**  
4. **Metadata filters** (tenant, date, doc type)  
5. **Prompt** with cite-or-abstain policy  
6. **Eval set** with regression in CI  

### Metrics to cite

| Metric | Meaning |
|--------|---------|
| **Recall@k** | Right chunk in top-k? |
| **MRR / nDCG** | Ranking quality |
| **Groundedness / faithfulness** | Answer supported by chunks? |
| **Answer correctness** | Human or LLM-judge vs reference |
| **Abstention rate** | “I don’t know” when appropriate |
| **p95 latency** | Retrieval + generation |
| **$/successful query** | Cost attribution |

Deep reference: [guide-to-ai-agent.md §10](./guide-to-ai-agent.md#10-retrieval-augmented-generation-rag).

---

## 5. Agentic Systems (Single & Multi-Agent)

### When agents fit this JD

- **Knowledge assistant** with tools (search CRM, create ticket)  
- **Document automation** (extract → validate → route)  
- **Workflow orchestration** (multi-step approvals)  

### Single-agent pattern

```
User → Orchestrator → LLM ⟷ Tools → Memory → Response
```

### Multi-agent pattern

```
Coordinator → [Researcher | Writer | Reviewer] → Aggregator → User
```

Use when: specialization beats one prompt; parallel tool calls; separate security review agent.

### Production guardrails (always mention)

- `max_iterations` / max steps  
- Tool **allowlist** + pydantic validation  
- **Human approval** for writes/sends/payments  
- Trace ID per run; log tool I/O (redacted)  

Deep reference: [master-ai-agent-guide.md §4–5](./master-ai-agent-guide.md#4-langgraph-full-tutorial).

---

## 6. Prompt Engineering & Orchestration

| Pattern | Use |
|---------|-----|
| **Prompt chain** | Sequential steps (extract → classify → generate) |
| **Router** | Cheap model picks intent / model tier |
| **Parallel fan-out** | Multiple retrievals then merge |
| **ReAct / tool loop** | Dynamic tool use with cap |

### Cost / latency optimization

- Cache embeddings and frequent queries  
- Smaller model for classification; Claude/GPT-4 class for hard synthesis  
- Prompt compression; trim context via rerank  
- Batch offline summarization  
- Stream tokens to UI for perceived latency  

### Claude-specific talking points

- Strong long-context and instruction following  
- Tool use / computer use (where enabled)—emphasize **your** wrapper for validation  
- Compare to OpenAI on: context, price, safety filters, enterprise BAAs  

---

## 7. Production APIs & Integration

### FastAPI checklist

- `pydantic` request/response models  
- Auth (JWT/OAuth), **tenant_id** on every call  
- `POST /chat` sync vs `POST /runs` async for long agents  
- **Idempotency-Key** for side effects  
- SSE/WebSocket for streaming  
- Background worker (Celery/ARQ) for long graphs  

### Enterprise integration

- Read from data lake / warehouse via governed APIs  
- Write-back only through approved tools with audit log  
- Secrets from vault; never in prompts  

Snippet to recognize: see [Mock Q&A § FastAPI](./agentic-genai-engineer-mock-interview-qa.md).

---

## 8. Guardrails, Safety & Evaluation

### Reduce hallucinations

- Require **citations** with chunk IDs  
- Low-confidence → abstain  
- Reranker threshold  
- Post-check: claim ⊆ union(retrieved chunks)  

### Policy constraints

- System prompt + **output schema** (JSON)  
- Blocked topics list; regex/ML moderation  
- Separate **policy model** or rules engine for regulated domains  

### Safe tool usage

- Read-only default; scoped credentials  
- No arbitrary SQL—parameterized queries or semantic layer only  
- Confirm destructive actions  

### Eval strategy

| Layer | What |
|-------|------|
| **Offline** | Golden Q&A, citation checks, toxicity |
| **CI** | Regression on prompt/model/index version |
| **Online** | Sampled human review, thumbs, task success |
| **Adversarial** | Prompt injection suite |

---

## 9. Collaboration: Data Eng, MLOps, Product

### With Data Engineering

- **Data contract** for ingestion: schema, PII tags, refresh cadence  
- Lineage: document_id → source system → ACL  
- Joint definition of “golden corpus” for RAG  

### With MLOps / Platform

- Containerized deploy; model/embedding version in registry  
- Prometheus metrics: latency, errors, tokens, retrieval hit rate  
- Canary on prompt + index changes  

### With Product

- Translate “smart search” into **task success metric**  
- Phase delivery: RAG read-only → tools → limited autonomy  

**Sound bite:** “I deliver **measurable** features, not demos—success metric agreed before we pick agents vs RAG.”

---

## 10. Azure & Multi-Cloud (Good-to-Have)

| Component | Role |
|-----------|------|
| **Azure OpenAI** | GPT models with private networking |
| **Azure AI Search** | Hybrid search, semantic ranker, indexers from blob |
| **Document Intelligence** | PDF/layout extraction |
| **Key Vault** | Secrets |
| **Entra ID** | Auth integration |

**Architecture sketch:**

```
App (FastAPI on App Service/AKS)
  → Azure OpenAI (chat + embeddings)
  → Azure AI Search (hybrid retrieval)
  → Blob/Data Lake (documents)
  → App Insights (traces)
```

Also show **cloud-agnostic** fluency: same patterns on AWS (Bedrock + OpenSearch) or GCP (Vertex + Vector Search).

---

## 11. Fine-Tuning vs RAG vs Agents

| Need | Start with |
|------|------------|
| Private knowledge | **RAG** |
| Stable JSON / tone at huge volume | **Fine-tune** (LoRA/PEFT) after RAG plateaus |
| Multi-step + tools | **Agent** with evals + caps |
| Tabular prediction | Classical ML—not LLM |

**Preferred (good-to-have):** Discuss LoRA when labels exist and inference cost dominates; prompt tuning for small style shifts.

---

## 12. Coding & System Design Expectations

### Coding round (likely)

- Implement **retrieval function** + simple synthesis stub  
- Parse tool-call JSON and validate with pydantic  
- Write **eval function** (exact match or contains-citation)  
- Debug a broken chunking pipeline  

### System design (45 min)

Common prompts:

- Enterprise **policy Q&A** over 10M documents, multi-tenant  
- **Support copilot** with CRM tools  
- **Document summarization** batch + API  

Structure: requirements → data → RAG/agent arch → eval → security → deploy → metrics.

Use [master-ai-agent-guide.md §14–15](./master-ai-agent-guide.md#14-ai-agent-system-design-interview-guide).

---

## 13. Portfolio & Stories to Prepare

Prepare **3 shipped projects** (even internal):

1. **RAG** — metric improvement (e.g. groundedness 72% → 89%)  
2. **Agent or workflow** — steps, tools, HITL, cost cap  
3. **Data pipeline** — how data reached the index  

Each story: **problem → your role → architecture → metrics → failure + fix**.

Optional: GitHub with redacted FastAPI + eval harness (high signal).

---

## 14. Likely Questions Checklist

- [ ] Walk through RAG pipeline you built; what would you change?  
- [ ] How do you evaluate retrieval vs generation errors?  
- [ ] Design multi-tenant knowledge assistant.  
- [ ] Tool calling: how do you validate arguments?  
- [ ] Prompt injection example and defenses.  
- [ ] Claude vs GPT for your use case.  
- [ ] How did your DE/DS background help this project?  
- [ ] Cost optimization story with numbers.  
- [ ] Failed POC—what killed it?  
- [ ] Azure AI Search vs managed Pinecone—tradeoffs.  

Full answers: [Mock Q&A](./agentic-genai-engineer-mock-interview-qa.md).

---

## 15. 10-Day Study Plan

| Day | Focus |
|-----|--------|
| 1 | [guide-to-ai-agent.md](./guide-to-ai-agent.md) §1–10; write your RAG diagram |
| 2 | [guide-to-ai-agent.md](./guide-to-ai-agent.md) §9–15; tool schema exercise |
| 3 | [master-ai-agent-guide.md](./master-ai-agent-guide.md) §4–5 LangGraph; sketch multi-agent |
| 4 | DE/DS stories—write 2 STAR narratives |
| 5 | Evals: build 10-row golden CSV; define metrics |
| 6 | Security: injection list + mitigations |
| 7 | Mock Q&A—practice 5 answers aloud |
| 8 | System design: enterprise RAG whiteboard timed 45m |
| 9 | Azure section + map your experience to Azure names |
| 10 | Cheat sheet + light coding (FastAPI endpoint) |

---

## 16. Corpus Coverage — Is AIML Enough?

### Best fit from existing docs

| Doc | Fit for this JD |
|-----|-----------------|
| [guide-to-ai-agent.md](./guide-to-ai-agent.md) | ★★★★★ Primary |
| [master-ai-agent-guide.md](./master-ai-agent-guide.md) | ★★★★★ Primary |
| [agentic-genai-engineer-*](./agentic-genai-engineer-interview-prep.md) (this pack) | ★★★★★ Role-specific |
| [ai-engineering-manager-*](./ai-engineering-manager-interview-prep.md) | ★★☆☆☆ Skip leadership sections |
| TowerResearch | ★★★☆☆ Cost/observability only |

### Realistic pass probability

| Preparation | Outcome |
|-------------|---------|
| Read all agent docs only | ~45–55% — weak on **your** DE/DS proof and spoken delivery |
| Docs + mock Q&A + 2 projects with metrics | **Strong** for many senior IC loops |
| Docs only, no production LLM experience | Unlikely to pass “1–3+ years production LLM” bar |

### You must bring externally

1. **Proof of DE or DS** — non-negotiable in JD  
2. **Production LLM** war stories (incidents, evals, cost)  
3. **Hands-on** LangChain/LangGraph or equivalent  
4. Company-specific Azure/AWS stack research  

---

## Questions to ask interviewers

- How is the **golden eval set** maintained today?  
- Split between **RAG** vs **agents** on the roadmap?  
- Who owns **document ACLs** in the vector index?  
- CI/CD for prompts and indexes—exists or greenfield?  
- Claude vs Azure OpenAI—standard or case-by-case?  

Good luck — lead with **data + measurement + production**, not model hype.
