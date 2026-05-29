# Agentic / GenAI Engineer — Coding Practice (Exercises + Reference Solutions)

> Aligns with JD: FastAPI, RAG retrieval, tool calling, evals, pydantic validation.  
> Pair with [Mock Q&A](./agentic-genai-engineer-mock-interview-qa.md) and [Interview Prep](./agentic-genai-engineer-interview-prep.md).

**How to use:** Try each exercise **45–60 min** without looking at solutions. Then compare and refactor.

---

## Exercise 1 — Tenant-aware vector search

**Prompt:** Implement `search(query_embedding, k, tenant_id, user_groups)` over in-memory records. Each record: `doc_id`, `tenant_id`, `text`, `embedding`, `allowed_groups: set[str]`. User sees doc only if `tenant_id` matches and `allowed_groups` intersects `user_groups` (non-empty).

```python
from typing import Iterable
import math

Record = dict  # doc_id, tenant_id, text, embedding, allowed_groups


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def search(
    records: Iterable[Record],
    query_embedding: list[float],
    k: int,
    tenant_id: str,
    user_groups: set[str],
) -> list[Record]:
  # TODO
    ...
```

<details>
<summary>Reference solution</summary>

```python
def search(
    records: Iterable[Record],
    query_embedding: list[float],
    k: int,
    tenant_id: str,
    user_groups: set[str],
) -> list[Record]:
    scored: list[tuple[float, Record]] = []
    for rec in records:
        if rec["tenant_id"] != tenant_id:
            continue
        if not rec["allowed_groups"].intersection(user_groups):
            continue
        score = cosine(query_embedding, rec["embedding"])
        scored.append((score, rec))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in scored[:k]]
```

**Follow-ups to mention in interview:** hybrid BM25 + vector; metadata pre-filter in DB; HNSW index; cache embeddings.

</details>

---

## Exercise 2 — Validate and execute a tool call

**Prompt:** LLM returns JSON `{"name": "create_ticket", "arguments": {"title": str, "priority": 1|2|3}}`. Validate with pydantic; reject invalid; return structured result.

```python
from pydantic import BaseModel, Field
from typing import Literal, Any

# TODO: ToolCall schema, validate_tool_call(raw: dict) -> ToolCall
# TODO: execute_tool(call, user_id) with allowlist
```

<details>
<summary>Reference solution</summary>

```python
from pydantic import BaseModel, Field, ValidationError
from typing import Literal, Any

ALLOWED_TOOLS = {"create_ticket", "search_kb"}

class CreateTicketArgs(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: Literal[1, 2, 3]

class ToolCall(BaseModel):
    name: Literal["create_ticket", "search_kb"]
    arguments: dict[str, Any]

def validate_tool_call(raw: dict) -> ToolCall:
    call = ToolCall.model_validate(raw)
    if call.name not in ALLOWED_TOOLS:
        raise ValueError("tool not allowed")
    if call.name == "create_ticket":
        CreateTicketArgs.model_validate(call.arguments)
    return call

def execute_tool(call: ToolCall, user_id: str) -> dict:
    if call.name == "create_ticket":
        args = CreateTicketArgs.model_validate(call.arguments)
        ticket_id = f"T-{user_id}-{hash(args.title) % 10_000}"
        return {"status": "ok", "ticket_id": ticket_id}
    return {"status": "ok", "results": []}
```

</details>

---

## Exercise 3 — Faithfulness check (claims ⊆ chunks)

**Prompt:** Given `answer` and list of `chunks`, return `True` if every sentence in `answer` has significant word overlap with at least one chunk (simple baseline—not production LLM-judge).

```python
import re

def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def is_faithful(answer: str, chunks: list[str], overlap_threshold: float = 0.35) -> bool:
    # TODO
    ...
```

<details>
<summary>Reference solution</summary>

```python
def sentence_overlap(sent: str, chunk: str) -> float:
    s, c = tokenize(sent), tokenize(chunk)
    if not s:
        return 1.0
    return len(s & c) / len(s)

def is_faithful(answer: str, chunks: list[str], overlap_threshold: float = 0.35) -> bool:
    sentences = [s.strip() for s in re.split(r"[.!?]+", answer) if s.strip()]
    if not sentences:
        return True
    for sent in sentences:
        best = max((sentence_overlap(sent, ch) for ch in chunks), default=0.0)
        if best < overlap_threshold:
            return False
    return True
```

**Interview note:** Production uses NLI models or LLM-as-judge with calibration; this shows you separate retrieval vs generation QA.

</details>

---

## Exercise 4 — FastAPI: async agent run with idempotency

**Prompt:** `POST /v1/runs` accepts `goal`, `tenant_id`, `idempotency_key`. Return existing `run_id` if key seen; else enqueue and return `202` with `run_id`.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
IDEMPOTENCY_STORE: dict[tuple[str, str], str] = {}  # (tenant, key) -> run_id
RUNS: dict[str, dict] = {}

class RunRequest(BaseModel):
    tenant_id: str
    goal: str
    idempotency_key: str

# TODO: POST /v1/runs , GET /v1/runs/{run_id}
```

<details>
<summary>Reference solution</summary>

```python
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
IDEMPOTENCY_STORE: dict[tuple[str, str], str] = {}
RUNS: dict[str, dict] = {}

class RunRequest(BaseModel):
    tenant_id: str
    goal: str = Field(max_length=4000)
    idempotency_key: str

class RunResponse(BaseModel):
    run_id: str
    status: str

@app.post("/v1/runs", response_model=RunResponse, status_code=202)
def create_run(req: RunRequest) -> RunResponse:
    key = (req.tenant_id, req.idempotency_key)
    if key in IDEMPOTENCY_STORE:
        run_id = IDEMPOTENCY_STORE[key]
        return RunResponse(run_id=run_id, status=RUNS[run_id]["status"])
    run_id = str(uuid.uuid4())
    IDEMPOTENCY_STORE[key] = run_id
    RUNS[run_id] = {"tenant_id": req.tenant_id, "goal": req.goal, "status": "queued"}
  # production: push to Celery/PubSub
    return RunResponse(run_id=run_id, status="queued")

@app.get("/v1/runs/{run_id}", response_model=RunResponse)
def get_run(run_id: str) -> RunResponse:
    if run_id not in RUNS:
        raise HTTPException(status_code=404, detail="not found")
    return RunResponse(run_id=run_id, status=RUNS[run_id]["status"])
```

</details>

---

## Exercise 5 — Chunk text without splitting tables (simplified)

**Prompt:** Split markdown-ish text on double newlines; if a block starts with `|`, keep table as single chunk.

```python
def chunk_document(text: str, max_chars: int = 2000) -> list[str]:
    # TODO
    ...
```

<details>
<summary>Reference solution</summary>

```python
def chunk_document(text: str, max_chars: int = 2000) -> list[str]:
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]
    chunks: list[str] = []
    buf = ""
    for block in blocks:
        if block.startswith("|"):
            if buf:
                chunks.extend(_flush(buf, max_chars))
                buf = ""
            chunks.extend(_flush(block, max_chars))
            continue
        candidate = f"{buf}\n\n{block}".strip() if buf else block
        if len(candidate) <= max_chars:
            buf = candidate
        else:
            if buf:
                chunks.extend(_flush(buf, max_chars))
            buf = block
    if buf:
        chunks.extend(_flush(buf, max_chars))
    return chunks

def _flush(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    out = []
    for i in range(0, len(text), max_chars):
        out.append(text[i : i + max_chars])
    return out
```

</details>

---

## Exercise 6 — Golden eval regression (CI-style)

**Prompt:** Load `cases.json` `[{question, expected_doc_ids, min_score}]`. Mock `retrieve(q)` returning doc ids. Fail if recall below threshold.

```python
import json

def recall_at_k(retrieved: list[str], expected: list[str], k: int) -> float:
    top = set(retrieved[:k])
    hit = len(top.intersection(expected))
    return hit / len(expected) if expected else 1.0

def run_eval(cases_path: str, retrieve_fn) -> None:
    # TODO: raise SystemExit(1) on failure
    ...
```

<details>
<summary>Reference solution</summary>

```python
def run_eval(cases_path: str, retrieve_fn) -> None:
    with open(cases_path) as f:
        cases = json.load(f)
    failures = []
    for i, case in enumerate(cases):
        retrieved = retrieve_fn(case["question"])
        r = recall_at_k(retrieved, case["expected_doc_ids"], k=5)
        if r < case.get("min_recall_at_5", 1.0):
            failures.append((i, r, case["question"]))
    if failures:
        for idx, score, q in failures:
            print(f"FAIL case {idx} recall@5={score:.2f} q={q[:60]}")
        raise SystemExit(1)
    print(f"PASS {len(cases)} cases")
```

</details>

---

## Leetcode-style systems thinking (no full code)

| Prompt | What they're testing |
|--------|----------------------|
| Rate limiter for LLM API per tenant | Token bucket, Redis |
| Design embedding cache | TTL, invalidation on doc version |
| Long conversation memory | Summarize + pin system facts |
| Parallel tool calls | asyncio.gather, timeout per tool |

---

## Related

- [Personalized guide — Kalpit Sharma](./kalpit-sharma-interview-guide.md)
- [agentic-genai-engineer-mock-interview-qa.md](./agentic-genai-engineer-mock-interview-qa.md)
