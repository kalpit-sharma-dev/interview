# End-to-End Study Material
## IDFC FIRST Bank — Head, Intelligence Automation

> The depth reference. Each section is a self-contained primer on a domain the JD demands. Read for understanding; convert to flashcards in `03-Study-Guide.md`.

## Sections
1. [Decisioning engines, BRMS & decision flows](#1-decisioning-engines-brms--decision-flows)
2. [Enterprise architecture & platform reference architecture](#2-enterprise-architecture--platform-reference-architecture)
3. [Data plane: features, feature stores, lineage](#3-data-plane-features-feature-stores-lineage)
4. [APIs & integration patterns](#4-apis--integration-patterns)
5. [Distributed systems, scalability, resilience, latency](#5-distributed-systems-scalability-resilience-latency)
6. [MLOps / ModelOps & champion-challenger](#6-mlops--modelops--champion-challenger)
7. [Decisioning use cases (credit, fraud, collections, marketing)](#7-decisioning-use-cases)
8. [Time-to-market, DevEx & self-service authoring](#8-time-to-market-devex--self-service-authoring)
9. [Production operations: SRE, SLOs, incident, DR/BCP](#9-production-operations-sre-slos-incident-drbcp)
10. [Model risk governance, explainability, fairness](#10-model-risk-governance-explainability-fairness)
11. [BFSI regulation: RBI, DPDP, outsourcing, localization](#11-bfsi-regulation-rbi-dpdp-outsourcing-localization)
12. [Information security & data protection](#12-information-security--data-protection)
13. [Team, org design & vendor management](#13-team-org-design--vendor-management)
14. [FinOps, cost & build-vs-buy economics](#14-finops-cost--build-vs-buy-economics)

---

## 1. Decisioning engines, BRMS & decision flows

### What a decision engine is
A **decision engine** evaluates inputs (application data, customer attributes, real-time features) against **business rules** and **predictive models** to produce a **decision** plus **reason codes**. It externalizes decision logic from application code so it can be changed, versioned, tested, and governed independently.

**Core concepts:**
- **Business rule** — a declarative statement: `IF age < 21 THEN decline (reason: AGE_BELOW_MIN)`. Rules are authored by business analysts, not buried in app code.
- **Ruleset / decision table** — a tabular set of conditions → outcomes; readable by business users.
- **Decision flow / strategy tree** — a directed graph chaining rules, sub-strategies, model calls, and segmentation into a full decision (e.g., eligibility → KYC gate → bureau check → scorecard → policy rules → limit assignment → pricing).
- **Scorecard** — a points-based model (often logistic regression) producing a score (e.g., credit score) used in cutoffs.
- **Cutoff** — score threshold separating approve/decline/refer.
- **Reason codes / adverse action codes** — explanations for a decision (regulatory requirement for declines).
- **Champion-challenger** — run alternative strategies on portions of traffic to measure improvement.
- **Straight-through processing (STP)** — fully automated decision with no human touch; exceptions routed to manual review.

### BRMS (Business Rules Management System)
Software to author, version, simulate, deploy, and execute rules. Components: rule repository, authoring UI, rule engine (often **Rete algorithm** for efficient pattern matching), testing/simulation, deployment, and runtime.

**Common products (know the landscape):**
| Product | Notes |
|---|---|
| **Drools** (open source, Red Hat) | Java, Rete-based; KIE/jBPM for workflow; common in-house choice. |
| **IBM ODM** (Operational Decision Manager) | Enterprise BRMS; Decision Center (business authoring) + Decision Server (runtime). |
| **FICO Blaze Advisor / Decision Modeler** | Strong in credit; part of FICO Platform / DMP. |
| **SAS** (Intelligent Decisioning, RTDM) | Analytics + decisioning; strong in banking. |
| **Pega** (Customer Decision Hub) | Real-time NBA, omni-channel decisioning, case management. |
| **Experian PowerCurve** | Originations/customer mgmt decisioning for lenders. |
| **Provenir** | Cloud-native risk decisioning + data orchestration; popular with fintechs/NBFCs. |
| **Actico, Sapiens, ACTICO, Equifax InterConnect** | Other BRMS/decisioning suites. |
| **DMN (Decision Model & Notation)** | OMG standard for modeling decisions (decision tables, FEEL expressions). Vendor-neutral. |

### Rules vs Models vs Workflow — when to use each
- **Rules:** deterministic policy, compliance gates, eligibility, hard cutoffs, regulatory constraints, things that must be **explainable and exact**. Easy to change, fully auditable.
- **Models:** probabilistic ranking/scoring where patterns beat hand-written rules (risk of default, fraud likelihood, propensity to respond). Need governance + monitoring.
- **Workflow/orchestration:** sequencing, segmentation, calling external services (bureau, KYC), human-in-the-loop, case management, retries, SLAs.
- **In practice:** a decision flow = workflow that calls **models** for scores and **rules** for policy, combining them into a final decision. Models inform; rules constrain; workflow orchestrates.

### Interview-ready talking points
- "I externalize decision logic into a decision/rules layer so business changes don't require app releases."
- "Decisions are composed: workflow orchestrates, models score, rules enforce policy, all producing reason codes and an audit record."
- "DMN gives a vendor-neutral, business-readable way to model decisions; Rete makes rule evaluation efficient at scale."

---

## 2. Enterprise architecture & platform reference architecture

### Enterprise architecture (EA) basics
- **EA** aligns business capability with technology. Frameworks: **TOGAF** (ADM cycle), **Zachman**. You don't need to recite them, but reference business/data/application/technology architecture layers.
- **C4 model** (Context → Container → Component → Code) for communicating architecture. You already use this — say so.
- **Domain-Driven Design (DDD)** — bounded contexts, ubiquitous language; maps neatly to microservices and to "decisioning" as a bounded context.
- **Capability-based platform thinking** — build reusable capabilities (decision execution, feature serving, model serving, authoring) consumed by many business journeys (multi-tenancy).

### The 5-plane decisioning platform (memorize, see Guide §3)
1. **Authoring/Design plane** — studio for rules, flows, scorecards; versioning; simulation; approvals.
2. **Execution/Runtime plane** — stateless decision service; sync (gRPC/REST) + async (Kafka); rules engine + model server + orchestration + feature lookup.
3. **Data plane** — online + offline feature store; streaming features; golden sources; lineage.
4. **Governance plane** — model registry/risk, validation, approvals, explainability, immutable audit, drift/bias monitoring.
5. **Operations plane** — observability, SLOs/error budgets, champion-challenger/A-B/shadow, runbooks, DR.

### Architecture qualities (the "-ilities") and how you achieve them
| Quality | How |
|---|---|
| **Scalability** | Stateless services, horizontal scaling, partitioned Kafka, caching, autoscaling (HPA/KEDA). |
| **Resilience** | Multi-AZ, circuit breakers, bulkheads, retries with backoff + jitter, timeouts, graceful degradation, fallback decisions. |
| **Low latency** | Online feature store (in-memory), precomputation, model optimization, co-location, connection pooling, async where possible. |
| **Security** | Zero-trust, mTLS, RBAC/ABAC, encryption in transit/at rest, secrets mgmt, PII tokenization. |
| **Observability** | Metrics, structured logs, distributed tracing (OTel), decision-level audit. |
| **Maintainability/evolvability** | Modular bounded contexts, versioned APIs, IaC, CI/CD, contract testing. |
| **Auditability** | Immutable decision log: inputs, version of rules/model, output, reason codes, timestamp, actor. |

### Multi-tenancy & platform product mindset
- Many consumers (credit, fraud, marketing) share the platform. Provide **isolation** (quotas, rate limits, separate decision namespaces), **self-service**, **versioned contracts**, and **SLAs**. Treat internal teams as customers; publish a service catalog and onboarding docs.

---

## 3. Data plane: features, feature stores, lineage

### Features
- A **feature** is an input signal to a rule/model (e.g., `num_txns_last_30d`, `avg_balance`, `bureau_score`, `days_past_due`).
- **Batch features** computed periodically (e.g., daily aggregates in the lake).
- **Real-time/streaming features** computed on the fly from event streams (e.g., velocity counts for fraud).

### Feature store
A system that manages features for **both training and serving** to guarantee consistency.
- **Offline store** — historical features for training & backtesting (lake/warehouse: BigQuery, Snowflake, Delta).
- **Online store** — low-latency feature reads at decision time (Redis, Aerospike, DynamoDB, Bigtable).
- **Registry** — feature definitions, ownership, versions, lineage.
- **Key value:** eliminates **training-serving skew** (the model sees the same feature logic in prod as in training).
- **Products:** Feast (open source), Tecton, Vertex AI Feature Store, Databricks/Sagemaker feature stores.

### Streaming feature computation
- **Kafka** for event transport; **Flink / Kafka Streams / Spark Structured Streaming** for stateful aggregations (windowed counts, rolling stats).
- **CDC (Change Data Capture)** via Debezium to stream DB changes into the feature pipeline.
- **Materialization** — push computed features to the online store for fast reads.

### Data quality, lineage, governance
- **Golden source / system of record** — authoritative data; avoid divergent copies.
- **Data lineage** — trace a feature back to its raw sources (needed for audit, debugging, impact analysis).
- **Data quality** — completeness, freshness, validity checks (e.g., Great Expectations / Deequ); SLAs on freshness.
- **Point-in-time correctness** — when building training data, use only features available *as of* the decision time (avoid label leakage).
- **Data contracts** — agreed schema + semantics + SLAs between producers and the platform.

### Interview talking points
- "Online + offline feature store ensures train/serve consistency and sub-10ms feature reads at decision time."
- "Point-in-time joins prevent leakage; lineage makes features auditable."
- "Streaming features (Flink + Kafka) power velocity rules for fraud at low latency."

---

## 4. APIs & integration patterns

### API styles
- **REST** — ubiquitous, cacheable, simple; good for external/partner integration.
- **gRPC** — binary (protobuf), HTTP/2, low latency, streaming; great for internal high-throughput decision calls. (Your strength.)
- **GraphQL** — flexible client-driven queries; less common for decisioning runtime.
- **Webhooks / callbacks** — async notifications to consumers.
- **API gateway** — auth, rate limiting, routing, throttling, observability (Apigee, Kong, AWS API GW).

### Integration patterns (Enterprise Integration Patterns)
- **Request-reply (sync)** — caller waits for a decision (real-time underwriting at app submit).
- **Event-driven / pub-sub (async)** — decisions triggered by events (transaction posted → fraud check).
- **Message queue / broker** — Kafka (log/stream), RabbitMQ/SQS (work queues). Decouples producers/consumers, smooths spikes.
- **Saga pattern** — manage distributed transactions across services via choreography or orchestration with compensating actions.
- **Outbox pattern** — reliably publish events with DB writes (avoid dual-write inconsistency).
- **CQRS** — separate read/write models for scale.
- **Idempotency** — dedupe via idempotency keys so retries don't double-decide.
- **Anti-corruption layer** — adapter that shields your domain model from messy external/legacy schemas (core banking, vendor formats).
- **Strangler fig** — incrementally replace a legacy decisioning system by routing slices of traffic to the new platform.

### Bank-specific integrations the platform touches
- **Core banking system (CBS)** — accounts, balances (Finacle/Flexcube/etc.).
- **LOS/LMS** — Loan Origination / Loan Management Systems.
- **Credit bureaus** — CIBIL, Experian, Equifax, CRIF High Mark (India).
- **KYC / identity** — Aadhaar/eKYC, PAN, video KYC, AML/sanctions screening.
- **Fraud systems** — device fingerprinting, transaction monitoring.
- **CDP / marketing** — customer data platform, campaign tools.
- **Data lake / warehouse** — features and offline analytics.
- **Payment rails** — UPI, IMPS, NEFT (for transaction-time decisions).

### Talking points
- "Anti-corruption layers isolate the platform from legacy core/vendor quirks; strangler-fig lets us migrate decisions incrementally."
- "Idempotency keys + outbox ensure exactly-once *effects* even with retries."
- "Sync gRPC for inline decisions; Kafka for event-driven and high-volume async decisioning."

---

## 5. Distributed systems, scalability, resilience, latency

### Fundamentals
- **CAP theorem** — under partition, choose consistency or availability. Decisioning often favors **availability + eventual consistency** for features, but **strong** for money-moving/limit-setting.
- **PACELC** — even without partitions, trade latency vs consistency.
- **Consistency models** — strong, eventual, read-your-writes, causal. Pick per data domain.
- **Idempotency, retries, timeouts, backoff + jitter** — table stakes for reliability.
- **Backpressure & load shedding** — protect the system under overload; shed low-priority work.

### Scaling
- **Horizontal scaling** of stateless decision services (K8s HPA/KEDA on CPU/RPS/queue depth).
- **Partitioning/sharding** — Kafka partitions by key; DB sharding for hot data.
- **Caching** — online feature cache, decision/result caching where safe, model artifact caching. Cache invalidation strategy matters.
- **Connection pooling** & async I/O to maximize throughput.

### Resilience patterns
- **Circuit breaker** — stop calling a failing dependency; fail fast.
- **Bulkhead** — isolate resource pools so one dependency's failure doesn't sink everything.
- **Graceful degradation / fallback** — if model server is down, fall back to rules-only or a conservative default decision (decide fail-open vs fail-closed by risk).
- **Multi-AZ / multi-region** — availability + DR.
- **Rate limiting & quotas** — per consumer/tenant.

### Latency engineering
- Budget the latency: network + auth + feature lookup + rules + model inference + logging. Optimize the biggest slices.
- **p50/p95/p99** — always reason about tail latency; SLAs are on p99.
- Techniques: in-memory features, smaller/quantized models, batching where allowed, parallel feature fetch, avoid synchronous chains, co-location.

### Event-driven architecture (EDA) — deep
- **Event** = immutable fact ("LoanApplicationSubmitted"). **Command** = intent.
- **Event sourcing** — store state as a sequence of events (strong audit fit for decisions).
- **Stream processing** — continuous computation over event streams (Flink/Kafka Streams).
- **Delivery semantics** — at-most-once, at-least-once, exactly-once (Kafka EOS via idempotent producer + transactions). In practice aim for at-least-once + idempotent consumers.
- **Schema management** — Avro/Protobuf + Schema Registry; backward/forward compatibility.
- **Ordering** — guaranteed within a partition; design keys accordingly.
- **DLQ (dead-letter queue)** — park poison messages for inspection.

### Talking points
- "I budget p99 latency across the call chain and attack the largest contributor first."
- "Decisioning needs a deliberate consistency stance per data domain — eventual for features, strong for limits/money."
- "Fail-safe fallback to rules-only keeps approvals flowing if the model tier degrades."

---

## 6. MLOps / ModelOps & champion-challenger

### Model lifecycle
problem framing → data prep → feature engineering → training → **validation** → **governance/approval** → packaging → **deployment** → serving → **monitoring** (performance + drift + bias) → retrain/refresh → retire.

### Serving patterns
- **Online (real-time) inference** — model server behind the decision service (KServe, Seldon, BentoML, Vertex/SageMaker endpoints, Triton).
- **Batch inference** — score a population offline (e.g., nightly propensity scores).
- **Embedded** — model compiled into the decision artifact (e.g., scorecard as rules) for ultra-low latency.

### Deployment & rollout strategies (decisioning-safe)
- **Shadow / dark launch** — challenger runs alongside champion, logs decisions, affects nothing. Safest first step.
- **Canary** — small % of live traffic to new version; watch metrics.
- **A/B test** — randomized split to measure causal lift on a primary metric.
- **Champion-challenger** — production strategy (champion) vs candidate(s) (challenger) on traffic slices; promote on sustained, significant lift within guardrails.
- **Blue-green** — instant switch + instant rollback.

### Monitoring
- **Performance** — accuracy/AUC/precision-recall *with delayed labels* (defaults/fraud confirm later → use proxy metrics + backtests).
- **Data drift** — input distribution shift (PSI — Population Stability Index, KS test).
- **Concept drift** — relationship between features and target changes.
- **Prediction drift** — score distribution shift.
- **Operational** — latency, throughput, error rate, feature freshness/nulls.
- **Bias/fairness** — outcomes across segments over time.

### Model registry & reproducibility
- **Registry** — versioned models with lineage (data, code, params, metrics), stage (staging/prod), approvals.
- **Experiment tracking** — MLflow, Vertex, W&B.
- **Reproducibility** — pin data snapshot, code, environment (containerized).

### Retraining
- **Triggers** — scheduled, drift-based, performance-based.
- **Pipeline** — automated, with validation gates and human approval for regulated models.
- Beware **feedback loops** (model affects future training data — e.g., declined applicants never produce repayment labels → reject inference / use champion-challenger to gather counterfactuals).

### GenAI/agents angle (your differentiator, used carefully)
- For a bank decisioning platform, GenAI is **augmentation**, not the core decision: document extraction (OCR/IDP), summarizing case files for reviewers, drafting adverse-action explanations, copilots for analysts authoring rules, RAG over policy docs. Keep **deterministic, auditable** models/rules for the actual lending/fraud decision; use GenAI where errors are recoverable and human-checked. Mention guardrails: grounding, eval, PII handling, hallucination control, human-in-the-loop.

### Talking points
- "Shadow → canary → champion-challenger is my safe path to production for any new decision logic."
- "Labels are delayed in credit, so I monitor drift (PSI), score distributions, and run backtests, not just live accuracy."
- "I separate the deterministic, auditable lending decision from GenAI assistance that's always human-checked."

---

## 7. Decisioning use cases

### Credit / underwriting (the flagship)
- **Origination decisioning:** eligibility → KYC/fraud gates → bureau pull → application + bureau scorecards → policy rules → approve/decline/refer → **limit assignment** → **risk-based pricing**.
- **Reject inference** — handle the missing-label problem for declined applicants.
- **Cutoff strategy** — set thresholds balancing approval rate vs expected loss; swap-set analysis when changing cutoffs.
- **Customer management** — limit increases, renewals, cross-sell eligibility, churn.
- **Metrics:** approval rate, bad rate / NPA, expected loss, RAROC, GINI/KS of scorecards, STP rate.

### Fraud & AML
- **Application fraud** — synthetic identity, first-party fraud; device/behavior signals.
- **Transaction fraud** — real-time scoring + velocity rules; balance false positives (customer friction) vs losses.
- **AML** — sanctions screening, transaction monitoring, suspicious activity; rules + scenarios + ML.
- **Metrics:** fraud detection rate, false-positive rate, $ losses prevented, alert-to-SAR conversion.

### Collections
- **Prioritization** — who to contact, when, via which channel (NBA for collections).
- **Treatment optimization** — settlement offers, restructuring eligibility.
- **Metrics:** roll rates, recovery rate, cost-to-collect.

### Marketing / cross-sell (Next-Best-Action)
- **Propensity models** + eligibility rules + arbitration (which offer wins) + contact policy (frequency caps).
- **Real-time NBA** at channel touchpoints (app, call center).
- **Metrics:** response rate, conversion, incremental revenue, offer relevance.

### Cross-cutting
- **Segmentation & strategy design** — different decision flows per segment.
- **Simulation & backtesting** — test a new strategy on historical data before going live.
- **Swap-set analysis** — who would be approved-now-declined / declined-now-approved under a new policy.

### Talking points
- "The platform serves credit, fraud, collections, and marketing from one governed runtime — reuse of features, models, and rules."
- "Every credit policy change is backtested + swap-set analyzed + champion-challenged before full rollout."

---

## 8. Time-to-market, DevEx & self-service authoring

### Why time-to-market is a JD success measure
If decisions live in app code, every tweak = full SDLC. The platform's value is letting the business change decisions **fast and safely**.

### Levers
- **Externalize decision logic** into BRMS/decision studio (no code deploy to change a rule).
- **Self-service authoring** for BAs/risk with guardrails (templates, validation, linting, approval gates).
- **Automated testing** — unit tests for rules, simulation on historical data, regression suites, contract tests.
- **CI/CD for decision artifacts** — version, test, promote (dev → UAT → prod) with approvals; treat rules/models as deployable artifacts (GitOps).
- **Champion-challenger** — ship safely; measure before full cutover.
- **Reuse** — shared feature library, reusable sub-strategies, standard reason codes.
- **Environments & data** — UAT with prod-like data (masked); sandbox for experimentation.
- **Decoupled release cadence** — platform releases vs decision-logic releases are independent.

### Developer/analyst experience (DevEx)
- Good docs, golden-path templates, fast local/sandbox testing, clear ownership, paved-road CI/CD, observability built in.
- **DORA metrics** — deployment frequency, lead time for change, change failure rate, MTTR — use to track engineering health.

### Talking points
- "I reduced time-to-market by externalizing decisions, giving BAs guarded self-service, and automating test + champion-challenger — speed *with* control."
- "I track DORA metrics for engineering health and lead-time-to-decision as a business KPI."

---

## 9. Production operations: SRE, SLOs, incident, DR/BCP

### SRE core
- **SLI** (indicator) — measured signal: e.g., decision latency p99, availability, error rate, decision-correctness.
- **SLO** (objective) — target: e.g., 99.95% availability, p99 < 200ms.
- **SLA** — contractual promise to consumers (with consequences).
- **Error budget** — allowed unreliability (1 − SLO); when exhausted, freeze features and focus on reliability.
- **Toil reduction & automation** — automate repetitive ops.

### Monitoring & observability
- **Three pillars:** metrics (Prometheus/Grafana), logs (structured, centralized — ELK/Loki), traces (OpenTelemetry/Jaeger).
- **Decision-specific telemetry:** decision volume, approve/decline rates, score distributions, reason-code frequencies, feature null rates, model latency — alert on anomalies (a sudden approval-rate jump may mean a broken rule).
- **Synthetic checks** & golden transactions in prod.

### Support model
- **L1/L2/L3** — triage → app/platform support → engineering. Runbooks for common incidents. On-call rotation with escalation policy.
- **ITIL processes** — incident, problem, change, release management. Banks usually run change advisory boards (CAB) — know how to ship within change windows.

### Incident management
- **Severity levels** (Sev-1..4), **Incident Commander** role, comms cadence, mitigate-first, then RCA.
- **Blameless postmortems** — timeline, root cause (5 whys), corrective + preventive actions, action owners.
- **MTTR/MTTD/MTBF** — measure and improve.

### Resilience & continuity
- **DR (Disaster Recovery)** — RPO (data loss tolerance) + RTO (downtime tolerance); active-active or active-passive; regular DR drills.
- **BCP (Business Continuity)** — keep deciding during outages (rules-only fallback, manual queues).
- **Capacity planning** — headroom for peaks (campaigns, month-end, festive lending spikes).
- **Chaos engineering** — inject failures to validate resilience.

### Talking points
- "SLOs + error budgets give an objective lever to balance velocity and reliability."
- "We design a fail-safe path: if the model/feature tier degrades, we keep approving via conservative rules and queue exceptions."
- "Blameless postmortems convert every Sev-1 into a systemic improvement."

---

## 10. Model risk governance, explainability, fairness

### Model risk management (MRM)
- Models can be wrong or misused → **model risk**. Banks govern it formally (globally guided by ideas in the US Fed **SR 11-7**; RBI expects sound model governance too).
- **Model inventory** — every model registered with owner, purpose, data, risk tier.
- **Independent validation** — a team separate from developers validates conceptual soundness, data, performance, and ongoing monitoring.
- **Tiering** — higher scrutiny for high-impact models (credit, capital) than low-risk ones.
- **Approval workflow** — documented sign-off before production; periodic re-validation.
- **Documentation** — model development docs, assumptions, limitations, monitoring plan.

### Explainability (XAI)
- **Global** — overall feature importance (e.g., for a scorecard, the points table).
- **Local** — why *this* decision (SHAP values, reason codes / adverse-action codes).
- **Regulatory need:** declines often require **specific reasons** to the customer (adverse action). Favor inherently interpretable models (scorecards/GBMs with SHAP) for credit; reserve black-box for low-stakes or with strong post-hoc explanation.
- **Techniques:** SHAP, LIME, counterfactual explanations, monotonic constraints (enforce sensible direction, e.g., higher income shouldn't lower approval).

### Fairness & bias
- **Protected attributes** — avoid using/proxying for prohibited attributes; check for disparate impact.
- **Metrics:** demographic parity, equal opportunity, disparate impact ratio.
- **Mitigations:** pre-processing (reweighing), in-processing (constraints), post-processing (threshold adjustment); strong documentation.
- In India, be mindful of fairness, consumer protection, and avoiding discriminatory outcomes even where formal anti-discrimination law differs from the US.

### Audit & traceability
- **Immutable audit trail** — for every decision: inputs, feature values, rule/model versions, output, reason codes, timestamp, actor. Reproducible on demand for audit/disputes.
- **Change audit** — who changed which rule/model, when, approved by whom.

### Talking points
- "Model risk is governed with an inventory, independent validation, risk tiering, and re-validation — I treat governance as a platform feature."
- "For credit declines we produce specific reason codes and prefer interpretable models with monotonic constraints + SHAP."
- "Every decision is reproducible from an immutable audit log — versions of rules and models included."

---

## 11. BFSI regulation: RBI, DPDP, outsourcing, localization

> You don't need to be a lawyer; you need to show you operate fluently within the regulatory frame and partner with compliance.

### RBI (Reserve Bank of India) themes relevant to a decisioning platform
- **IT governance / IT outsourcing / IT risk** — RBI Master Directions on IT Governance, Risk, Controls and Assurance Practices; outsourcing of IT services (board-approved policy, due diligence, exit, concentration risk, right to audit).
- **Outsourcing of financial services** — when vendors make/assist decisions, accountability stays with the bank.
- **Digital lending guidelines** — transparency (Key Fact Statement), no hidden charges, data collection limits, control over LSPs (Lending Service Providers), customer consent, cooling-off period. Highly relevant for automated credit decisioning.
- **Fair Practices Code** — fair, transparent treatment; reasons for rejection.
- **Cyber security framework** for banks — controls, SOC, incident reporting.
- **Data localization** — RBI's **payment data** must be stored in India (Storage of Payment System Data, 2018).
- **Model/algorithm transparency** — expectation that automated decisions are explainable and non-discriminatory.
- **Risk-Based Internal Audit (RBIA)** and **three lines of defense**.

### DPDP Act 2023 (Digital Personal Data Protection)
- India's data privacy law. Key concepts: **Data Principal** (individual), **Data Fiduciary** (the bank), **consent** (free, specific, informed), **purpose limitation**, **data minimization**, **rights** (access, correction, erasure, grievance), **Significant Data Fiduciaries** (extra obligations), breach notification.
- Implication for the platform: capture consent, minimize PII in features, support data-subject rights, log purpose of processing, secure PII.

### Audit & compliance operating posture
- Maintain **audit-ready** artifacts: decision logs, model docs, change approvals, access reviews.
- Partner early with **compliance, risk, infosec** (don't surprise them at go-live).
- Be ready for **regulatory inspection** — produce evidence of governance, controls, and explainability.

### Talking points
- "Accountability for outsourced/vendor-assisted decisions stays with the bank — so I bake governance and right-to-audit into vendor and platform design."
- "Digital lending rules mean transparent, consent-based, explainable automated credit decisions — the platform enforces KFS, consent capture, and reason codes."
- "Payment data localization and DPDP shape where and how we store features and PII."

*(Always frame regulation as something you operationalize with compliance, not something you interpret unilaterally. Verify current specifics with the Bank's compliance team.)*

---

## 12. Information security & data protection

### Security architecture
- **Zero-trust** — never trust, always verify; authenticate + authorize every call (mTLS between services).
- **AuthN/AuthZ** — OAuth2/OIDC for users; service identities (SPIFFE/mTLS) for services; **RBAC** + **ABAC** for fine-grained access (who can author/approve/deploy decisions).
- **Least privilege & segregation of duties** — author ≠ approver ≠ deployer (four-eyes).
- **Secrets management** — Vault/KMS; no secrets in code/config; rotation.
- **Encryption** — TLS in transit; AES-256 at rest; field-level encryption/tokenization for PII (PAN, Aadhaar, card data).
- **PII handling** — tokenization, masking in non-prod, data minimization in features, access logging.
- **PCI-DSS** — for card data flows.
- **Network** — segmentation, WAF, private endpoints, egress control.
- **Supply chain** — SAST/DAST/SCA, signed artifacts, SBOM, image scanning.
- **Audit logging** — tamper-evident logs of access and changes; SIEM integration; SOC monitoring.
- **Secure SDLC** — threat modeling (STRIDE), security review gates, pen tests.

### Prompt-injection / GenAI-specific (if GenAI used)
- Input/output filtering, grounding, no secrets in prompts, PII redaction, guardrails, human-in-the-loop for actions, eval for jailbreaks.

### Talking points
- "Segregation of duties — author, approver, deployer are different roles with four-eyes and full audit."
- "PII is minimized in features and tokenized; non-prod uses masked data; every access is logged to SIEM."

---

## 13. Team, org design & vendor management

### The multidisciplinary team (from the JD)
| Role | Owns |
|---|---|
| **Product managers** | Vision, roadmap, prioritization, stakeholder value, intake. |
| **Business analysts** | Decision logic, rules authoring, requirements, UAT. |
| **Architects** | Reference architecture, standards, tech decisions, NFRs. |
| **Engineers** (platform, data, ML) | Build runtime, pipelines, integrations, feature/model serving. |
| **QA / test engineers** | Functional + decision simulation + performance + regression. |
| **Production support / SRE** | Monitoring, on-call, incident, reliability. |
| **(adjacent) Risk/compliance/infosec liaisons** | Governance, validation, controls. |

### Org design principles
- **Stream-aligned teams** around business journeys + a **platform team** providing the decisioning capability (Team Topologies). Avoid silos that drop the lifecycle ball.
- **RACI** for every major flow (intake, change, incident, model approval).
- **Operating cadences** — sprint/PI planning, governance forum, ops review, stakeholder steering committee.
- **Career growth** — IC and lead tracks; grow seniors; succession planning (a JD success measure: retention).

### Hiring & retention
- Hire for the gaps (decisioning/BRMS, ML serving, SRE). Mix of build (engineers) and run (support). Use a structured loop. Retain via growth, ownership, clear impact, and protecting from chaos.

### Vendor / partner management (DSAs, agencies, COTS vendors)
- **SOW + SLAs**, escalation matrix, right-to-audit, exit clauses, data-protection terms, concentration-risk awareness, performance reviews. Avoid lock-in (abstraction layers, data portability).
- **External partners** in the JD (DSAs, agencies) — they consume decisions (eligibility, offers) → secure APIs, rate limits, monitoring, and contractual data handling.

### Talking points
- "I run a platform team that serves stream-aligned business teams, with RACI and SLAs so the lifecycle never falls between the cracks."
- "Retention is a success measure — I invest in growth paths, ownership, and shielding the team from churn."

---

## 14. FinOps, cost & build-vs-buy economics

### Cost levers for a decisioning platform
- **Compute** — right-size, autoscale, spot for batch, efficient model serving (batching, quantization, CPU vs GPU).
- **Data** — storage tiering, retention policies, avoid duplicate pipelines, query cost control.
- **Licensing** — COTS BRMS/decisioning suites can be expensive (per-decision or per-core); negotiate committed-use.
- **Per-decision cost** — track cost per decision / per 1000 decisions as a unit economic; attribute to consuming business unit (chargeback/showback).

### Build vs Buy vs Compose
| Option | Pros | Cons | When |
|---|---|---|---|
| **Buy** COTS suite (Pega/FICO/SAS/Provenir) | Fast, proven, governance built in, vendor support | Cost, lock-in, customization limits, latency | Time-to-market critical; limited in-house talent; standard use cases. |
| **Build** in-house | Control, fit, no license, your strengths (Go/K8s/Kafka) | Time, talent, you own everything incl. governance UI | Differentiated needs, scale economics, strong eng org. |
| **Compose** (hybrid) | Buy engine/studio, own platform/integration/runtime | Integration complexity | Most realistic enterprise answer. |

Decision criteria: regulatory fit, latency/scale, TCO over 3–5 yrs, lock-in, talent, time-to-market, differentiation.

### Talking points
- "I manage unit economics — cost per decision — and chargeback to consuming functions to drive accountability."
- "My default is compose: buy the proven decisioning/governance engine, own the integration, runtime, and data plane where our scale and differentiation live."

---

*Next:* drill with [`03-Study-Guide.md`](./03-Study-Guide.md) and [`04-500-Interview-Questions.md`](./04-500-Interview-Questions.md).
