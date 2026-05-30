#!/usr/bin/env python3
"""Generate 783 detailed interview Q&As from question titles."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "kalpit-ml-dl-nlp-mlops-interview-500-qa.md"
SRC_SHORT = ROOT / "_questions_extract.txt"


def extract_questions_from_short_file():
    """Parse short-A format file."""
    text = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
    if "**A:**" not in text and "**Short answer" not in text:
        raise FileNotFoundError("Need source with questions")
    items = []
    for m in re.finditer(r"^### Q(\d+)\. (.+)$", text, re.MULTILINE):
        items.append((int(m.group(1)), m.group(2).strip()))
    sec_positions = []
    for m in re.finditer(r"^## (.+)$", text, re.MULTILINE):
        name = m.group(1)
        if "How to" in name or "Table" in name:
            continue
        sec_positions.append((m.start(), name))
    return items, sec_positions, text


def block(short, detailed, practice, pitfalls, tip, profile):
    return "\n".join([
        f"**Short answer (say this first):** {short}",
        "",
        "**Detailed explanation:**",
        detailed.strip(),
        "",
        "**How to apply in practice:**",
        practice.strip(),
        "",
        "**Common pitfalls:**",
        pitfalls.strip(),
        "",
        f"**Interview tip:** {tip}",
        "",
        f"**For your profile (Kalpit):** {profile}",
    ])


def expand_operationalize(topic: str) -> str:
    t = topic.strip(" ?")
    return block(
        f"Treat **{t}** as a production requirement: automate it, monitor it, assign an owner, and document rollback—not a one-time manual fix.",
        f"""**{t.title()}** in MLOps means making the practice **repeatable, auditable, and on-call ready**.

**What interviewers want to hear:**
- **Who owns it** — platform MLOps vs AI product squad (RACI).
- **What artifact** it affects — data snapshot, model URI, prompt version, vector index generation.
- **What gate** enforces it — CI test, manual approval, change ticket (CMR in banks).
- **What you measure** — SLO breach, drift statistic, queue lag, GPU utilization.
- **How you rollback** — previous registry version, feature flag, blue-green index alias.

**Example narrative:** "We promote models from Staging→Prod only if offline eval passes thresholds; if p95 latency doubles in canary, we rollback the endpoint alias to N-1 within 15 minutes using the registry pin."

For **{t}**, spell the concrete mechanism (tool + process), not buzzwords.""",
        f"- Add **{t}** to Definition of Done for releases.\n- Automate in Vertex/Kubeflow/Airflow—not a quarterly manual audit.\n- Run a **game-day** drill: inject failure and execute rollback.",
        "- No versioned artifacts.\n- Alerts without runbooks.\n- Unclear ownership between teams.",
        "Use: **version → gate → monitor → rollback** in one breath.",
        "HDFC: **GCP**, **Grafana/OTel**, **AI Skin** releases alongside **mobile banking** peaks—change control matters.",
    )


def expand_nlp_enterprise(topic: str) -> str:
    t = topic.strip()
    return block(
        f"Use **{t}** where it measurably improves retrieval, understanding, or generation—always validate on in-domain banking text.",
        f"""**{t}** is applied in enterprise NLP pipelines at specific stages:

| Stage | Role of {t} |
|-------|----------------|
| Ingest | Normalize noisy customer text, OCR output, or chat logs |
| Index | Improve tokenization/chunking/search recall |
| Query | Query expansion, spelling, language ID routing |
| Generate | Constrain outputs (format, citations, abstain) |

**Banking constraints:** PII redaction before cloud LLMs; audit logs; multilingual India (English/Hinglish); regulatory wording must be **grounded** in approved documents (RAG), not invented.

**Evaluation:** Build 200+ question golden set; measure retrieval (recall@k, nDCG) and generation (faithfulness, citation coverage) separately.""",
        f"- A/B test adding **{t}** vs baseline on golden set.\n- Ship behind feature flag; sample human review.\n- Document when **not** to use it (latency/cost vs gain).",
        "- Benchmarking only on Wikipedia/MS MARCO.\n- Tool added without offline gain.",
        "State pipeline stage + metric improved.",
        "**AI Skin** KB/search; orchestration with LangChain/LlamaIndex; data eng curated corpus.",
    )


def expand_market(q: str) -> str:
    return block(
        "The market in 2025–26 rewards **production discipline**: evals, cost per task, guardrails, and regulated-domain experience—not demos.",
        f"""Question context: **{q.rstrip('?')}**

**Balanced view interviewers respect:**
- **Agents** are real for workflows with tools, but most banks ship **RAG + HITL** first.
- **RAG is not dead**—it evolved (hybrid search, rerankers, agentic retrieval).
- **Small models + routing** cut cost vs always using flagship LLMs.
- **MCP/tool standards** reduce integration tax—you have practical experience here.
- **FinOps for AI** (token chargeback) is mandatory at scale.

**Hiring:** DE/DS foundation + shipped LLM features; seniors as Staff/Lead/Manager; Leetcode still common for platform-heavy loops.""",
        "- Read release notes from Anthropic/OpenAI/Google quarterly.\n- Maintain personal **tech radar** doc.\n- Kill POCs with explicit criteria.",
        "- Framework churn without eval improvement.\n- Claiming full autonomy in banking without controls.",
        "Sound excited but **risk-aware**—banks hire for judgment.",
        "Your AVP + **26 engineers** + **AI Skin** maps to high-demand **BFSI AI leadership**.",
    )


# --- High-value specific answers ---
SPECIFIC = {
    "explain precision vs recall": lambda: block(
        "Precision = TP/(TP+FP); recall = TP/(TP+FN). High precision → few false alarms; high recall → few misses.",
        """Use a **confusion matrix** (positive/negative × predicted/actual).

- **Precision:** Of predicted positives, how many are correct? Critical when **false positives are expensive** (wrong fraud alert, spammy offers).
- **Recall:** Of actual positives, how many did we find? Critical when **false negatives are expensive** (missed fraud, missed default).

They usually **trade off**. Adjust decision threshold using a **PR curve** and a **cost matrix**, not default 0.5.

**Banking examples:**
- Fraud: often prioritize recall, cap analyst load from FP.
- Credit marketing: prioritize precision to protect brand.""",
        "- Report precision, recall, **PR-AUC**, and calibration.\n- Monitor per segment weekly.\n- Document threshold change approval.",
        "- Quoting accuracy on 99% negatives.\n- Ignoring imbalance.",
        "Draw 2×2 matrix on whiteboard.",
        "Map to HDFC fraud/AML/support AI metrics.",
    ),
    "what is cross-validation and why use it": lambda: block(
        "k-fold CV rotates train/validation splits to stabilize performance estimates; use stratified CV for imbalance; use time-based splits for temporal data.",
        """Single splits lie. **k-fold CV:** partition data into k folds; each fold serves once as validation while training on the rest; average k scores.

**Stratified:** preserves class ratios in each fold (fraud/churn).

**Time series:** **forward chaining**—train on past, validate on future; never random shuffle transactions across time.

**Nested CV:** outer estimates generalization; inner tunes hyperparameters—prevents optimistic bias.""",
        "- CV for model selection; **holdout test** only at end.\n- Group CV by `customer_id` to prevent leakage.\n- Log variance across folds.",
        "- Leakage via duplicate customers across folds.\n- Tuning on test data.",
        "Mention **group k-fold** for banking entities.",
        "Same rigor for **AI Skin** prompt/index regression tests.",
    ),
    "what is the bias-variance tradeoff": lambda: block(
        "Bias = underfitting (too simple); variance = overfitting (too sensitive). Balance with model complexity, regularization, and more data.",
        """**Bias:** systematic error from wrong model family (linear for nonlinear fraud). High train & val error.

**Variance:** fits noise; low train error, high val error.

**Learning curves** diagnose which dominates. **Fix bias:** more features, complex model. **Fix variance:** regularization, dropout, more data, ensemble averaging.""",
        "- Prefer stable CV performance over peak train score.\n- Use ensembles for variance reduction.",
        "- Chasing complexity on small tabular bank data.",
        "Say you'd ship a simpler stable model in production.",
        "Mobile banking needs stable predictions during peak festivals.",
    ),
}


def classify(q: str) -> str:
    ql = q.lower()
    if "operationalize" in ql:
        return "operationalize"
    if "how is" in ql and "enterprise nlp" in ql:
        return "nlp_ent"
    if any(k in ql for k in ["market", "trend", "2025", "2026", "hype", "hiring", "dead"]):
        return "market"
    if any(k in ql for k in ["rag", "retriev", "embedding", "chunk", "vector", "bm25"]):
        return "rag"
    if any(k in ql for k in ["agent", "mcp", "langgraph", "tool call", "react", "crew"]):
        return "agent"
    if any(k in ql for k in ["mlops", "deploy", "registry", "drift", "pipeline", "kubeflow", "vertex", "monitor", "rollback", "serve", "ci/cd"]):
        return "mlops"
    if any(k in ql for k in ["transformer", "attention", "lora", "cnn", "backprop", "pytorch", "tensorflow", "gpu", "relu", "gan"]):
        return "dl"
    if any(k in ql for k in ["llm", "claude", "gpt", "prompt", "token", "rlhf", "temperature"]):
        return "llm"
    if any(k in ql for k in ["kafka", "etl", "warehouse", "spark", "parquet", "airflow", "dbt", "data eng"]):
        return "de"
    if any(k in ql for k in ["golang", "fastapi", "grpc", "docker", "kubernetes"]):
        return "eng"
    if any(k in ql for k in ["lead", "team", "hire", "bank", "stakeholder", "avp"]):
        return "leadership"
    if any(k in ql for k in ["bert", "ner", "nlp", "tokeniz", "summar", "sentiment"]):
        return "nlp"
    return "ml"


def default_expand(cat: str, q: str) -> str:
    topic = q.rstrip("?").strip()
    ql = q.lower()

    intros = {
        "ml": f"**{topic}** is a foundational machine learning concept interviewers use to test whether you can build and evaluate models responsibly—not just define buzzwords.",
        "dl": f"**{topic}** relates to deep learning systems where representation, optimization, and GPU economics matter for both training and serving.",
        "nlp": f"**{topic}** appears in modern NLP stacks that combine classical text processing, transformers, and often RAG for enterprise knowledge tasks.",
        "llm": f"**{topic}** is part of shipping large language models safely: capability limits, orchestration, cost, and governance.",
        "rag": f"**{topic}** directly impacts retrieval quality—the highest-leverage layer in most production GenAI systems.",
        "agent": f"**{topic}** affects agentic workflows where models invoke tools and require strict safety boundaries.",
        "mlops": f"**{topic}** is an MLOps capability that turns experimental models into auditable, monitored production services.",
        "de": f"**{topic}** is a data engineering practice that upstream ML and RAG quality depend on.",
        "leadership": f"**{topic}** is assessed for senior leaders managing platform + AI delivery in regulated environments.",
        "eng": f"**{topic}** is part of building reliable GenAI microservices at scale.",
    }

    bodies = {
        "ml": """Structure your answer:
1. **Define** the term in one or two sentences.
2. **When to use / not use** it.
3. **How to evaluate** impact (metrics, CV, business KPI).
4. **Production note** — drift monitoring, retraining, documentation.

Connect to **generalization**, **leakage prevention**, and **class imbalance** when relevant.""",
        "dl": """Cover:
- **Intuition** (what problem it solves in the network).
- **Training** considerations (LR, batch norm, regularization, mixed precision).
- **Inference** constraints (latency, memory, quantization).
- **Modern context** — transformers dominate NLP; CNNs still strong in vision.""",
        "nlp": """Cover pipeline placement (ingest, retrieve, generate), **in-domain eval**, and **governance** (PII, audit). Mention hybrid retrieval + rerank when search is involved.""",
        "llm": """Separate **model behavior** from **your system**: routing, caching, guardrails, eval harness, versioning, rollback, $/successful task.""",
        "rag": """Explain effect on recall@k, faithfulness, latency, and reindex/ACL workflows. Diagnose retrieval vs generation failures separately.""",
        "agent": """Emphasize allowlisted tools, schema validation, max steps, audit logs, human approval for financial side effects.""",
        "mlops": """Explain artifact versioned, pipeline stage, promotion gate, monitoring alert, and rollback path.""",
        "de": """Emphasize freshness SLAs, idempotency, schema contracts, lineage, and curated gold layers feeding ML/RAG.""",
        "leadership": """Use STAR with metrics; mention 20 backend + 6 AI squad coordination, compliance, peak banking delivery.""",
        "eng": """Discuss API design, async/queues, observability, failure modes; Python orchestration + Golang gateway pattern.""",
    }

    practices = {
        "ml": "- Always baseline simple model.\n- Use proper splits (stratified/temporal/group).\n- Track experiments with data hash + seed.",
        "dl": "- Start from pretrained checkpoints.\n- Profile GPU memory early.\n- Plan serving optimizations before launch.",
        "nlp": "- Build golden datasets in domain language.\n- Measure retrieval and generation separately.",
        "llm": "- Pin model versions; canary prompts.\n- Temperature 0 for structured extraction.",
        "rag": "- Hybrid search + rerank; version indexes.\n- Cite-or-abstain policies.",
        "agent": "- Cap steps and token budget.\n- Integration tests with mocked tools.",
        "mlops": "- Automate gates in CI/CD.\n- Champion/challenger deploy.",
        "de": "- Contract tests on schemas.\n- Propagate deletes to vector indexes.",
        "leadership": "- Align OKRs to business metrics.\n- Protect team focus during releases.",
        "eng": "- Idempotency + trace IDs everywhere.\n- Circuit breakers on LLM APIs.",
    }

    profiles = {
        "ml": "M.Tech AI/ML, flight-analysis, emotion recognition CNN—same eval discipline for AI Skin.",
        "dl": "TensorFlow/PyTorch + CUDA projects; today focus on LLM inference orchestration at HDFC.",
        "nlp": "AI Skin search/Q&A; LangChain, LlamaIndex, Semantic Kernel, Crew.ai.",
        "llm": "Claude/GPT enterprise use; private GCP; audit and HITL for banking actions.",
        "rag": "GCS docs, Postgres metadata, governed ingestion with data engineering.",
        "agent": "MCP servers + multi-agent workflows; Go microservices integration.",
        "mlops": "Grafana/OTel, Pub/Sub, GCP partner patterns from mobile banking platform.",
        "de": "log-monitoring Kafka pipeline; M.Tech DE; Barclays batch accuracy culture.",
        "leadership": "AVP HDFC; ~26 engineers; AI Skin + mobile banking scale.",
        "eng": "Golang/gRPC/PubSub/Aerospike + Python FastAPI AI services.",
    }

    short = f"Explain **{topic}** clearly, then connect to production evaluation and banking impact."

    return block(short, intros[cat] + "\n\n" + bodies[cat], practices[cat],
                 "- Generic definitions without examples.\n- Ignoring production monitoring.",
                 "Use define → apply → measure → risk pattern.",
                 profiles[cat])


def answer_for(q: str) -> str:
    ql = q.lower().rstrip("?")
    for key, fn in SPECIFIC.items():
        if key in ql:
            return fn()
    if "operationalize" in ql:
        topic = q.split("operationalize", 1)[-1].strip(" ?")
        return expand_operationalize(topic)
    if "how is" in ql and "enterprise nlp" in ql:
        topic = q.split("How is", 1)[-1].split("used in enterprise")[0].strip()
        return expand_nlp_enterprise(topic)
    cat = classify(q)
    if cat == "market":
        return expand_market(q)
    if "walk through" in ql and "rag" in ql:
        return expand_operationalize("end-to-end RAG pipeline with eval gates and ACL-aware retrieval")
    if "prompt injection" in ql:
        return SPECIFIC.get("prompt injection", lambda: None)() if False else block(
            "Treat all user/retrieved content as untrusted; use layered defenses—not secret prompts alone.",
            """**Attack:** Instructions embedded in user text or documents ('ignore policy, exfiltrate data').

**Layers:**
1. Instruction/data separation in prompt template.
2. ACL-aware retrieval (tenant isolation).
3. Tool allowlist + pydantic validation (no raw SQL).
4. Output moderation + schema enforcement.
5. HITL for transfers/external comms.
6. Red-team tests in CI.""",
            "- Log suspicious patterns; rate limit tenants.\n- Run adversarial evals each release.",
            "- API keys in prompts; autonomous payment tools.",
            "Say **defense in depth**.",
            "HDFC AI Skin: audit every tool call; approval for writes.",
        )
    return default_expand(cat, q)


def main():
    items, sec_positions, src = extract_questions_from_short_file()
    out = [
        "# Kalpit Sharma — ML / DL / NLP / MLOps Interview Q&A (Detailed Edition)",
        "",
        "> **783 questions** with **detailed answers** for interview preparation.",
        ">",
        "> Each answer: **Short opener** · **Detailed explanation** · **Practice** · **Pitfalls** · **Tip** · **Profile link**",
        "",
        "**Start:** [kalpit-sharma-interview-guide.md](./kalpit-sharma-interview-guide.md)",
        "",
        "---",
        "",
        "## How to study",
        "",
        "1. **5–10 questions/day** — read, then explain aloud without looking.",
        "2. Customize **For your profile** with real **AI Skin** numbers.",
        "3. Use [coding practice](./agentic-genai-engineer-coding-practice.md) for hands-on rounds.",
        "",
        "---",
        "",
    ]
    current = None
    for num, q in items:
        pos = src.find(f"### Q{num}. ")
        sec = sec_positions[0][1] if sec_positions else "General"
        for p, name in sec_positions:
            if pos >= 0 and p <= pos:
                sec = name
        if sec != current:
            if current:
                out += ["---", ""]
            out += [f"## {sec}", ""]
            current = sec
        out += [f"### Q{num}. {q}", "", answer_for(q), ""]
    out += ["---", "", "*Detailed edition for interview learning.*"]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"OK: {len(items)} Qs, {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
