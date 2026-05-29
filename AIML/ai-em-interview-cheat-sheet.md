# AI Engineering Manager — One-Page Interview Cheat Sheet

> Print or keep open during prep. Deep dives: [EM Interview Prep](./ai-engineering-manager-interview-prep.md) · [Mock Q&A](./ai-em-mock-interview-qa.md)

---

## Role in one line

Ship **production AI** (ML + GenAI/agents) through an **8–9 person squad**, partner with **Product / Data / MLOps**, own **KPIs (accuracy, latency, cost)**, stay **30–40% hands-on**.

---

## JD → prove in interview

| They want | You prove with |
|-----------|----------------|
| Lead 8–9 engineers | Hiring, 1:1s, performance, retention, delegation |
| Production AI | Launch phases, eval gates, postmortem, SLAs |
| Vertex + MLOps | Pipelines, registry, endpoints, RACI with platform team |
| Bridge stakeholders | Roadmap story, said-no with data, RACI |
| Hands-on | FastAPI/agent pattern, code review example |
| Best practices | CI/CD for ML, monitoring, prompt/model versioning |
| Innovation | Time-boxed POCs + kill criteria |

---

## Agent vs RAG vs fine-tune vs classical ML

```
Tabular / structured prediction?     → Classical ML (XGBoost, logistic)
Private knowledge Q&A, no actions?   → RAG (+ citations)
Fixed format, high volume?           → Fine-tune (after RAG baseline)
Multi-step + tools + side effects?   → Agent + guardrails + HITL
```

**Non-negotiables:** max steps · max cost · max time · tool allowlist · eval in CI

---

## Metric tree

```
Business (retention, deflection, revenue)
  → Product (task success, CSAT, escalation %)
    → ML/AI (groundedness, hallucination rate, eval pass %)
      → Eng (p95 latency, availability, $/successful task)
```

---

## Vertex AI (name-drop with purpose)

| Component | Use |
|-----------|-----|
| Vertex Pipelines | Reproducible train/eval/deploy |
| Model Registry | Staging → prod promotion |
| Endpoints | Managed online serve |
| Gemini + grounding | GenAI with corp data |
| Feature Store | Train/serve consistency (if adopted) |

**Partnership line:** App team owns APIs/agents/evals; MLOps owns cluster standards, IAM, promotion gates, cost guardrails.

---

## ML / GenAI CI/CD gates

Code tests → integration → **golden eval set** → security (injection) → staging → **canary** → prod → monitor (drift, cost, quality)

Version: **code · image · data hash · model · prompts · index**

---

## System design (45 min)

1. Requirements & SLAs  
2. Users & HITL points  
3. Diagram (gateway → orchestrator → models → data)  
4. Data (OLTP, vector, audit)  
5. Model strategy + eval  
6. Rollout (shadow → canary)  
7. Failures (injection, drift, cost loop, vendor down)  
8. Team/RACI  
9. Phased roadmap  

---

## STAR (always end with metrics)

| Story | Have ready |
|-------|------------|
| Scaled delivery | Date, scope, team size |
| Hiring / coaching | Level change, retention |
| Conflict w/ PM | Data, decision, outcome |
| Prod incident | MTTR, prevention |
| Cost spike | $ saved, policy |
| Killed bad POC | Kill criteria |

---

## First 90 days

| Days | Do |
|------|-----|
| 1–30 | 1:1s, on-call shadow, inventory models/prompts/evals, align KPIs with PM |
| 31–60 | One reliability win (eval CI, cost dash, runbook), RACI with MLOps |
| 61–90 | Roadmap v1, hiring plan, team working agreements |

---

## Questions to ask them

Success at 6/12 months? Vertex vs custom GKE split? Eval/registry maturity? On-call? Who owns roadmap prioritization? Biggest AI incident last year?

---

## 3-doc map

| Doc | Use |
|-----|-----|
| [guide-to-ai-agent](./guide-to-ai-agent.md) | RAG, tools, APIs, lifecycle |
| [master-ai-agent-guide](./master-ai-agent-guide.md) | Architecture, LangGraph, K8s, security |
| [ai-engineering-manager-interview-prep](./ai-engineering-manager-interview-prep.md) | Leadership, Vertex, cases, study plan |
| [ai-em-mock-interview-qa](./ai-em-mock-interview-qa.md) | Full spoken answers |

---

## TowerResearch folder — when to use

**Use for:** token economics, FinOps, Bedrock/cost attribution, governance, observability depth.  
**Don’t rely on alone for:** product EM leadership, Vertex-centric loops, squad management stories.

---

## Enough to pass?

**Content:** these docs ≈ **50–65%** of prep for **product AI EM**.  
**You still need:** STAR stories (metrics), 2 mocks, 1 shipped GenAI/ML prod narrative, company research.  
**Senior architect title:** add distributed systems depth + ADRs + cross-org influence stories (see EM prep § “Architect variant”).
