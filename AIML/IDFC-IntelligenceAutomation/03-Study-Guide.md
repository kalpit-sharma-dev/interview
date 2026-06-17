# Study Guide
## IDFC FIRST Bank — Head, Intelligence Automation

> The drill layer: syllabus checklist, mastery scorecard, 200+ flashcards, a 150+ term glossary, "must-be-able-to-draw" diagrams, and the vendor/tooling landscape. Use daily.

## Contents
1. [Syllabus checklist](#1-syllabus-checklist)
2. [Mastery scorecard](#2-mastery-scorecard)
3. [Must-be-able-to-draw diagrams](#3-must-be-able-to-draw-diagrams)
4. [Flashcards (200+)](#4-flashcards)
5. [Glossary (150+ terms)](#5-glossary)
6. [Vendor & tooling landscape](#6-vendor--tooling-landscape)
7. [Metrics cheat sheet](#7-metrics-cheat-sheet)
8. [One-page cram sheet](#8-one-page-cram-sheet)

---

## 1. Syllabus checklist

Tick when you can explain it to a peer **without notes**.

**A. Decisioning core**
- [ ] Decision engine vs rules engine vs decision flow vs scorecard
- [ ] BRMS: authoring, versioning, Rete, deployment, runtime
- [ ] DMN (decision tables, FEEL)
- [ ] Rules vs models vs workflow — when to use each
- [ ] Reason/adverse-action codes; STP & exception management
- [ ] Champion-challenger, shadow, A/B, canary

**B. Architecture**
- [ ] 5-plane decisioning platform reference architecture
- [ ] C4 model; DDD bounded contexts; capability/platform thinking
- [ ] The "-ilities" and how to achieve each
- [ ] Multi-tenancy, quotas, SLAs to internal consumers

**C. Data**
- [ ] Feature store (online/offline), train-serve consistency
- [ ] Streaming features (Kafka/Flink, CDC), point-in-time correctness
- [ ] Lineage, data quality, golden sources, data contracts

**D. Integration**
- [ ] REST vs gRPC vs events; API gateway
- [ ] EIP: request-reply, pub-sub, saga, outbox, CQRS, idempotency
- [ ] Anti-corruption layer, strangler fig
- [ ] Bank systems: CBS, LOS/LMS, bureaus, KYC, fraud, CDP, payment rails

**E. Distributed systems**
- [ ] CAP/PACELC, consistency models
- [ ] Scaling: stateless, sharding, caching, autoscaling
- [ ] Resilience: circuit breaker, bulkhead, fallback, backpressure
- [ ] Latency budgeting, p50/p95/p99
- [ ] EDA deep: event sourcing, delivery semantics, schema registry, DLQ

**F. MLOps/ModelOps**
- [ ] Model lifecycle; serving patterns (online/batch/embedded)
- [ ] Rollout: shadow/canary/A-B/champion-challenger/blue-green
- [ ] Monitoring: data/concept/prediction drift, PSI/KS, delayed labels
- [ ] Registry, reproducibility, retraining triggers, feedback loops
- [ ] Where GenAI/agents fit (augment, not core decision)

**G. Use cases**
- [ ] Credit/underwriting (cutoffs, limits, pricing, reject inference, swap-set)
- [ ] Fraud/AML (real-time scoring, FP/loss trade-off)
- [ ] Collections (prioritization, treatment)
- [ ] Marketing/NBA (propensity, arbitration, contact policy)

**H. Delivery & ops**
- [ ] Time-to-market levers; self-service authoring; CI/CD for decisions
- [ ] DORA metrics
- [ ] SRE: SLI/SLO/SLA, error budgets
- [ ] Observability (metrics/logs/traces + decision telemetry)
- [ ] Incident mgmt, postmortems, MTTR; DR (RPO/RTO), BCP, capacity

**I. Governance/regulation/security**
- [ ] Model risk management (inventory, validation, tiering)
- [ ] Explainability (SHAP, reason codes, monotonic constraints)
- [ ] Fairness/bias metrics + mitigations
- [ ] RBI themes (IT governance, outsourcing, digital lending, localization)
- [ ] DPDP Act 2023 essentials
- [ ] InfoSec (zero-trust, RBAC/ABAC, SoD, encryption, PII, SIEM)

**J. Leadership**
- [ ] Multidisciplinary org design, RACI, Team Topologies
- [ ] Hiring/retention; vendor mgmt; exec comms
- [ ] First 90 days; FinOps/build-vs-buy

---

## 2. Mastery scorecard

Rate 1–5 (5 = could teach it). Re-score weekly. Anything ≤3 → study.

| Domain | Wk1 | Wk2 | Wk3 | Wk4 |
|---|---|---|---|---|
| Decisioning/BRMS | | | | |
| Enterprise architecture | | | | |
| Data/feature store | | | | |
| APIs/integration | | | | |
| Distributed systems/EDA | | | | |
| MLOps/ModelOps | | | | |
| Use cases (credit/fraud) | | | | |
| Delivery/time-to-market | | | | |
| SRE/ops/DR | | | | |
| Model governance | | | | |
| RBI/DPDP regulation | | | | |
| InfoSec | | | | |
| Leadership/org | | | | |
| FinOps/build-buy | | | | |

**Target before interview:** all ≥4; architecture, decisioning, governance, leadership = 5.

---

## 3. Must-be-able-to-draw diagrams

Practice drawing each from memory in <3 min:

1. **5-plane decisioning platform** (Authoring / Runtime / Data / Governance / Ops) — see Guide §3.
2. **A decision flow** — eligibility → KYC/fraud gate → bureau pull → scorecard → policy rules → approve/decline/refer → limit → pricing → reason codes → audit.
3. **Real-time fraud pipeline** — event (Kafka) → stream features (Flink) → online store (Redis) → model+rules → decision; async case mgmt + feedback loop.
4. **Feature store** — sources → batch + streaming pipelines → offline store (training) + online store (serving) → registry/lineage; train-serve consistency.
5. **Champion-challenger** — traffic split → champion + challenger(s) → metric comparison + guardrails → promote/rollback.
6. **CI/CD for decisions** — author in studio → version (Git) → test/simulate → UAT approval → promote to prod → monitor → rollback.
7. **Resilience view** — gateway → decision svc (multi-AZ) with circuit breakers/bulkheads → model server (fallback to rules-only) → online store (cache).

---

## 4. Flashcards

> Format: **Q** — A. Cover the answer, recall, flip.

### Decisioning
1. **What is a decision engine?** — Service that evaluates rules + models on inputs to produce a decision + reason codes, externalizing decision logic from app code.
2. **BRMS?** — Business Rules Management System: author, version, simulate, deploy, execute rules.
3. **Rete algorithm?** — Efficient pattern-matching algorithm rules engines use to evaluate many rules over facts.
4. **DMN?** — Decision Model & Notation; OMG standard; decision tables + FEEL expressions; business-readable.
5. **Decision flow/strategy tree?** — Graph chaining segmentation, rules, model calls into a full decision.
6. **Scorecard?** — Points-based (often logistic) model producing a score for cutoffs.
7. **Cutoff?** — Score threshold separating approve/decline/refer.
8. **Reason codes?** — Explanations for a decision; declines need adverse-action reasons (regulatory).
9. **STP?** — Straight-through processing: fully automated decision, no human touch.
10. **Champion-challenger?** — Prod strategy vs candidate(s) on traffic slices; promote on sustained significant lift within guardrails.
11. **Shadow deployment?** — Challenger runs alongside, logs decisions, affects nothing — safest first step.
12. **Swap-set analysis?** — Who flips approve↔decline under a new policy; assess impact.
13. **Reject inference?** — Estimating performance of declined applicants who never get labels.
14. **Rules vs models?** — Rules: deterministic policy/compliance, fully explainable. Models: probabilistic patterns; need governance/monitoring.

### Architecture
15. **C4 model?** — Context, Container, Component, Code — levels of architecture diagrams.
16. **DDD bounded context?** — A boundary within which a domain model + language is consistent; maps to services.
17. **Multi-tenancy?** — One platform serving many consumers with isolation, quotas, SLAs.
18. **Anti-corruption layer?** — Adapter shielding your model from messy external/legacy schemas.
19. **Strangler fig?** — Incrementally replace a legacy system by routing slices to the new one.
20. **The 5 planes?** — Authoring, Runtime, Data, Governance, Operations.

### Data
21. **Feature store?** — Manages features for training + serving to ensure consistency; offline + online + registry.
22. **Training-serving skew?** — Mismatch between features in training vs prod; feature store prevents it.
23. **Online store examples?** — Redis, Aerospike, DynamoDB, Bigtable (low-latency reads).
24. **CDC?** — Change Data Capture; stream DB changes (Debezium) into pipelines.
25. **Point-in-time correctness?** — Use only features available as of decision time; avoid label leakage.
26. **Data lineage?** — Trace a feature back to raw sources; needed for audit/debugging.
27. **Data contract?** — Agreed schema+semantics+SLA between producer and consumer.
28. **Golden source?** — Authoritative system of record for a data domain.

### Integration / distributed systems
29. **gRPC vs REST?** — gRPC: binary protobuf, HTTP/2, low latency, streaming (internal). REST: text/JSON, ubiquitous (external).
30. **Saga?** — Manage distributed transaction via local steps + compensating actions.
31. **Outbox pattern?** — Write event to an outbox table in same txn; relay publishes — avoids dual-write inconsistency.
32. **CQRS?** — Separate read and write models.
33. **Idempotency key?** — Dedup token so retries don't double-process.
34. **CAP theorem?** — Under partition, choose Consistency or Availability.
35. **PACELC?** — Even without partition (Else), trade Latency vs Consistency.
36. **Circuit breaker?** — Stop calling a failing dependency; fail fast; auto-recover.
37. **Bulkhead?** — Isolate resource pools so one failure doesn't sink all.
38. **Backpressure?** — Signal/limit producers when consumers overwhelmed.
39. **Graceful degradation?** — Keep serving with reduced function (e.g., rules-only fallback).
40. **p99 latency?** — 99th percentile; tail latency; SLAs target it.
41. **Exactly-once (Kafka)?** — Idempotent producer + transactions; in practice at-least-once + idempotent consumers.
42. **DLQ?** — Dead-letter queue for poison messages.
43. **Event sourcing?** — Store state as an immutable event log; strong audit fit.
44. **Schema registry?** — Manages Avro/Protobuf schema versions + compatibility.

### MLOps
45. **Model registry?** — Versioned model store with lineage, stage, approvals.
46. **Data drift?** — Input distribution shift (detect with PSI/KS).
47. **Concept drift?** — Feature→target relationship changes.
48. **PSI?** — Population Stability Index; measures distribution shift.
49. **Canary deploy?** — Send small % traffic to new version, watch metrics.
50. **Blue-green?** — Two environments; instant switch + rollback.
51. **Shadow vs canary?** — Shadow affects nothing (logs only); canary affects a small % of real decisions.
52. **Feedback loop risk?** — Model affects future training data (declined applicants lack labels).
53. **Delayed labels?** — Credit/fraud outcomes confirm later; monitor drift + backtests, not just live accuracy.
54. **KServe/Seldon?** — Kubernetes model-serving frameworks.

### Use cases
55. **GINI/KS (scorecard)?** — Discrimination power metrics of a credit model.
56. **RAROC?** — Risk-adjusted return on capital.
57. **Bad rate / NPA?** — Default proportion; non-performing assets.
58. **Risk-based pricing?** — Price (interest) varies by risk score.
59. **Next-Best-Action?** — Real-time choice of best offer/action per customer.
60. **Arbitration (NBA)?** — Choosing which eligible offer wins.
61. **AML?** — Anti-Money Laundering: screening + transaction monitoring + SAR.
62. **Roll rate (collections)?** — Rate accounts move to worse delinquency buckets.

### Delivery & ops
63. **DORA metrics?** — Deploy frequency, lead time for change, change failure rate, MTTR.
64. **SLI/SLO/SLA?** — Indicator / Objective / Agreement.
65. **Error budget?** — 1 − SLO; allowed unreliability; governs velocity vs reliability.
66. **MTTR/MTTD?** — Mean time to recover / detect.
67. **RPO/RTO?** — Recovery Point (data loss tolerance) / Recovery Time (downtime tolerance).
68. **BCP vs DR?** — Business continuity (keep operating) vs disaster recovery (restore systems).
69. **Three pillars of observability?** — Metrics, logs, traces.
70. **Incident Commander?** — Single owner coordinating a major incident.
71. **Blameless postmortem?** — RCA focused on systems, not blame; action items.
72. **Chaos engineering?** — Inject failures to validate resilience.
73. **CAB?** — Change Advisory Board (ITIL change governance).

### Governance / regulation / security
74. **Model risk management?** — Inventory + independent validation + tiering + approvals + monitoring.
75. **SR 11-7?** — US Fed model risk guidance (conceptual reference for sound MRM).
76. **SHAP?** — Shapley-value-based local feature attributions for explainability.
77. **Monotonic constraints?** — Force sensible direction (more income ⇒ not less approval).
78. **Disparate impact?** — Adverse outcome ratio across groups; fairness check.
79. **Adverse action notice?** — Reasons given to a declined applicant.
80. **DPDP Act 2023?** — India privacy law: consent, purpose limitation, data-principal rights, fiduciary duties.
81. **Data localization (RBI)?** — Payment system data stored in India.
82. **Digital lending guidelines?** — Transparency (KFS), consent, control of LSPs, cooling-off.
83. **Three lines of defense?** — Business (1st), risk/compliance (2nd), audit (3rd).
84. **Zero-trust?** — Never trust, always verify every request.
85. **RBAC vs ABAC?** — Role-based vs attribute-based access control.
86. **Segregation of duties?** — Author ≠ approver ≠ deployer (four-eyes).
87. **Tokenization?** — Replace PII with non-sensitive token; reversible via vault.
88. **SIEM?** — Security Information & Event Management; central security monitoring.
89. **STRIDE?** — Threat-modeling taxonomy (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation).

### Leadership
90. **Team Topologies?** — Stream-aligned, platform, enabling, complicated-subsystem teams.
91. **RACI?** — Responsible, Accountable, Consulted, Informed.
92. **Build vs buy vs compose?** — In-house / COTS / hybrid; choose by reg fit, latency, TCO, lock-in, talent, time-to-market.
93. **Showback vs chargeback?** — Report costs vs actually bill internal teams.
94. **Cost per decision?** — Unit economic for the platform.
95. **TOGAF ADM?** — Architecture Development Method cycle in TOGAF EA framework.

*(Add your own cards for any glossary term below you can't yet define.)*

---

## 5. Glossary

**ABAC** — Attribute-Based Access Control. · **Adverse action** — required reasons for a declined application. · **AML** — Anti-Money Laundering. · **Anti-corruption layer** — adapter isolating domain from external schemas. · **API gateway** — entry point handling auth, routing, rate limits. · **Audit trail** — immutable record of decisions/changes. · **Autoscaling** — scale instances by load (HPA/KEDA). · **Backpressure** — flow control when consumers overwhelmed. · **Backtesting** — evaluate a strategy on historical data. · **Bad rate** — proportion of defaults. · **Blue-green** — two-env deploy for instant switch/rollback. · **BRMS** — Business Rules Management System. · **Bulkhead** — fault isolation between resource pools. · **CAB** — Change Advisory Board. · **Canary** — gradual rollout to a small % traffic. · **CAP** — Consistency/Availability/Partition trade-off. · **CBS** — Core Banking System. · **CDC** — Change Data Capture. · **CDP** — Customer Data Platform. · **Champion-challenger** — compare prod vs candidate strategies. · **Chaos engineering** — deliberate failure injection. · **Chargeback** — bill internal teams for usage. · **Circuit breaker** — stop calling failing dependency. · **Concept drift** — feature→target relationship shifts. · **Consent** — DPDP lawful basis for processing. · **CQRS** — Command Query Responsibility Segregation. · **C4 model** — Context/Container/Component/Code diagrams. · **Cutoff** — score threshold for decision. · **Data contract** — producer-consumer schema/SLA agreement. · **Data drift** — input distribution shift. · **Data fiduciary** — entity deciding purpose/means of processing (the bank). · **Data localization** — store data in-country. · **Data principal** — the individual (DPDP). · **DDD** — Domain-Driven Design. · **Decision flow** — orchestrated decision logic graph. · **Decision table** — tabular rules. · **DLQ** — Dead-Letter Queue. · **DMN** — Decision Model & Notation. · **DORA metrics** — delivery performance metrics. · **DPDP** — Digital Personal Data Protection Act 2023 (India). · **DR** — Disaster Recovery. · **Drift** — distribution/relationship change over time. · **DSA** — Direct Selling Agent. · **EDA** — Event-Driven Architecture. · **EIP** — Enterprise Integration Patterns. · **Error budget** — allowable unreliability (1−SLO). · **Event sourcing** — state as event log. · **Explainability (XAI)** — making decisions interpretable. · **Fail-open/closed** — default decision when a dependency fails. · **Fairness** — equitable outcomes across groups. · **Feature** — input signal to rule/model. · **Feature store** — system serving features for train+serve. · **FEEL** — Friendly Enough Expression Language (DMN). · **FinOps** — cloud/AI cost management discipline. · **Four-eyes** — dual approval control. · **GINI** — scorecard discrimination metric. · **Golden source** — authoritative data system. · **gRPC** — high-performance RPC over HTTP/2. · **Guardrail metric** — counter-metric protecting against harm while optimizing. · **HITL** — Human-in-the-loop. · **HPA/KEDA** — Kubernetes autoscalers. · **Idempotency** — repeated op has same effect once. · **IDP** — Intelligent Document Processing. · **Incident Commander** — incident coordination owner. · **ITIL** — IT service management framework. · **KFS** — Key Fact Statement (digital lending). · **KS statistic** — distribution-difference metric. · **KServe/Seldon** — K8s model serving. · **KYC** — Know Your Customer. · **Latency budget** — allocation of time across call chain. · **Lineage** — data/feature provenance. · **LOS/LMS** — Loan Origination/Management System. · **LSP** — Lending Service Provider. · **mTLS** — mutual TLS service auth. · **Model registry** — versioned model catalog. · **Model risk** — risk of model errors/misuse. · **ModelOps/MLOps** — operationalizing models. · **Monotonic constraint** — enforce feature direction. · **MRM** — Model Risk Management. · **MTTR/MTTD/MTBF** — recovery/detect/between-failure times. · **Multi-tenancy** — shared platform, isolated tenants. · **NBA** — Next-Best-Action. · **NPA** — Non-Performing Asset. · **OIDC/OAuth2** — identity/authorization protocols. · **Outbox** — reliable event publishing pattern. · **PACELC** — extends CAP with latency trade-off. · **PCI-DSS** — card-data security standard. · **PII** — Personally Identifiable Information. · **PSI** — Population Stability Index. · **RACI** — responsibility matrix. · **RAROC** — Risk-Adjusted Return on Capital. · **RBAC** — Role-Based Access Control. · **RBIA** — Risk-Based Internal Audit. · **Reason codes** — decision explanations. · **Reject inference** — modeling declined applicants. · **Rete** — rules pattern-matching algorithm. · **RPO/RTO** — recovery point/time objectives. · **Saga** — distributed-transaction pattern. · **SAST/DAST/SCA** — security testing types. · **Scorecard** — points-based scoring model. · **SBOM** — Software Bill of Materials. · **Segregation of duties** — split sensitive roles. · **SHAP** — Shapley explainability. · **Showback** — report (not bill) costs. · **SIEM** — security event management. · **SLI/SLO/SLA** — service-level indicator/objective/agreement. · **SoD** — Segregation of Duties. · **SR 11-7** — US model risk guidance. · **STP** — Straight-Through Processing. · **Strangler fig** — incremental legacy replacement. · **STRIDE** — threat model taxonomy. · **Swap-set** — applicants flipped by a policy change. · **Team Topologies** — team-design framework. · **Three lines of defense** — risk governance model. · **TOGAF** — EA framework. · **Tokenization** — replace PII with tokens. · **Toil** — repetitive manual ops work. · **Training-serving skew** — train/prod feature mismatch. · **Zero-trust** — verify every request.

---

## 6. Vendor & tooling landscape

| Category | Examples | Note for you |
|---|---|---|
| **Decisioning suites** | Pega CDH, FICO Platform/Blaze, SAS Intelligent Decisioning, Experian PowerCurve, Provenir, Actico | Know 2–3 well; Provenir/FICO common with lenders/NBFCs. |
| **Open-source rules** | Drools/KIE, Camunda+DMN | Likely in-house option (Java). |
| **Feature store** | Feast, Tecton, Vertex AI FS, Databricks FS | Train-serve consistency story. |
| **Model serving** | KServe, Seldon, BentoML, Triton, Vertex/SageMaker endpoints | K8s-native fits your stack. |
| **Streaming** | Kafka, Flink, Kafka Streams, Spark Structured Streaming, Debezium (CDC) | Your strength. |
| **Online store** | Redis, Aerospike, DynamoDB, Bigtable | Low-latency feature reads. |
| **Data/lake** | BigQuery, Snowflake, Databricks/Delta | Offline features/analytics. |
| **Orchestration/workflow** | Temporal, Airflow, Camunda, Argo | Decision flow + pipelines. |
| **MLOps** | MLflow, Vertex AI, Kubeflow, SageMaker | Registry/experiments/pipelines. |
| **Observability** | Prometheus/Grafana, OpenTelemetry, ELK/Loki, Jaeger | Decision telemetry too. |
| **API/integration** | Apigee, Kong, gRPC, GraphQL | Gateway + contracts. |
| **Security** | Vault, KMS, SPIFFE, SIEM (Splunk/Elastic) | SoD, secrets, audit. |
| **GenAI (augment)** | Vertex/OpenAI/Anthropic, LangChain/LangGraph, RAG, vector DBs | Analyst copilots, IDP, case summaries — human-checked. |

---

## 7. Metrics cheat sheet

| Area | Metric | Why it matters |
|---|---|---|
| Platform | Decision latency p99, availability | Real-time SLA |
| Platform | Throughput (decisions/sec) | Scale |
| Delivery | Time-to-market for new rule/model | JD success measure |
| Delivery | DORA (deploy freq, lead time, CFR, MTTR) | Eng health |
| Adoption | # business functions / use cases live | JD success measure |
| Reliability | SLO attainment, error budget burn, MTTR | Production stability |
| Credit | Approval rate, bad rate/NPA, GINI/KS, STP rate, expected loss | Decision quality |
| Fraud | Detection rate, false-positive rate, $ losses prevented | Risk vs friction |
| Marketing | Response/conversion, incremental revenue | Value |
| Governance | % models validated, drift alerts, audit findings closed | Compliance |
| Cost | Cost per decision / per 1000 decisions | Unit economics |
| Team | Attrition, time-to-hire, engagement | Retention success measure |

---

## 8. One-page cram sheet

- **Role:** own enterprise decisioning platform end-to-end (concept→ops) in a regulated bank.
- **4 pillars:** Data + Rules + Models + Workflow. **Wrap:** Governance + Operations.
- **5 planes:** Authoring, Runtime, Data, Governance, Ops.
- **Safe change path:** shadow → canary → champion-challenger → full, with rollback.
- **Latency:** budget the chain; online feature store; fallback to rules-only.
- **Resilience:** multi-AZ, circuit breaker, bulkhead, backpressure, graceful degradation.
- **Governance:** model inventory + independent validation + tiering; reason codes; SHAP; monotonic constraints; immutable audit.
- **Regulation:** RBI (IT governance, outsourcing, digital lending, localization), DPDP 2023; three lines of defense.
- **Security:** zero-trust, RBAC/ABAC, SoD/four-eyes, tokenized PII, SIEM.
- **Delivery:** externalize logic, self-service authoring, CI/CD for decisions, DORA.
- **Ops:** SLO/error budget, observability + decision telemetry, incident command, DR (RPO/RTO), BCP.
- **Leadership:** multidisciplinary team (PM/BA/architect/eng/QA/support), RACI, Team Topologies, retention.
- **90 days:** listen+map → strategy+foundation+quick win → deliver first use case + onboard second.
- **Mantra:** Outcome → capability → architecture/governance → operations → metric.

Next: rehearse [`04-500-Interview-Questions.md`](./04-500-Interview-Questions.md).
