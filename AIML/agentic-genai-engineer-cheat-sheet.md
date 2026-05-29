# Agentic / GenAI Engineer — One-Page Cheat Sheet

> IC role · 5–12 yrs · **Mandatory DE or DS background** · Production RAG + agents  
> Full prep: [Interview Prep](./agentic-genai-engineer-interview-prep.md) · [Mock Q&A](./agentic-genai-engineer-mock-interview-qa.md)

---

## JD in one line

Build **enterprise RAG + agentic workflows** (Claude/LangGraph/FastAPI), with **guardrails, evals**, and tight partnership with **Data Eng + MLOps**.

---

## Prove mandatory DE/DS (open with this)

| Path | Say |
|------|-----|
| **DE** | Owned pipelines → curated corpus → RAG index with lineage + ACL |
| **DS** | ML lifecycle + eval discipline → golden sets for LLM regression |
| **Analytics eng** | Approved metrics layer → assistant never invents KPIs |

---

## RAG pipeline (memorize order)

`Ingest → Parse → Chunk → Embed → Index → (filter) Retrieve → Rerank → Synthesize + cite → Eval`

**Top fixes:** ACL metadata · hybrid search · reranker · cite-or-abstain · golden CI

---

## Agent vs RAG

| Need | Use |
|------|-----|
| Q&A on docs | RAG |
| Multi-step + tools | Agent + **max steps** + validated tools |
| Tabular ML | Not LLM |

---

## Production non-negotiables

- Auth + **tenant** on retrieval  
- Tool **allowlist** + pydantic validation  
- **Idempotency** on writes  
- Traces: prompt version, index version, model ID  
- **$/successful task** + p95 latency  

---

## Eval (split retrieval vs generation)

| Failure | Signal | Fix |
|---------|--------|-----|
| Wrong chunk | Low recall@k | Chunking, hybrid, metadata |
| Right chunk, wrong answer | High recall, low faithfulness | Prompt, rerank, stronger model |
| Unsafe | Policy eval fail | Guardrails, HITL |

---

## Prompt / cost

Router (small) → retrieve → synthesize (large) · cache embeddings · stream UI · batch summaries offline

---

## Claude talking point

Strong instructions + tools; always **your** validation layer; compare cost/context vs Azure OpenAI deployment

---

## Azure (if asked)

`FastAPI → Azure OpenAI + Azure AI Search (hybrid) → Blob → App Insights`

---

## System design (45m)

Requirements → data/ACL → RAG or agent diagram → eval → security → deploy → metrics

---

## 3 stories ready

1. RAG + metric delta  
2. Agent/workflow + guardrails  
3. DE/DS pipeline feeding GenAI  

---

## AIML doc map

| Doc | Use |
|-----|-----|
| [guide-to-ai-agent](./guide-to-ai-agent.md) | RAG, tools, APIs |
| [master-ai-agent-guide](./master-ai-agent-guide.md) | LangGraph, multi-agent, K8s |
| [agentic-genai-engineer-mock-qa](./agentic-genai-engineer-mock-interview-qa.md) | Full answers |

**Skip for this role:** EM leadership pack (unless panel includes mgr round).

---

## Enough to pass?

Docs ≈ **50–60%** · You need **DE/DS proof + 1–2 prod LLM projects + mocks + coding practice**.
