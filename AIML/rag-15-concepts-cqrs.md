# 15 RAG Concepts — Interview Guide

> Retrieval-augmented generation for a Customer Query Resolution System. Most bad support answers are retrieval failures: a stronger model cannot cite a deductible that never entered the prompt.

**Project:** Resolve, a Customer Query Resolution System for consumer electronics (phones, routers, a paid Care+ plan, India as the main market).

**How to claim it:** Present Resolve as a system you designed and can defend. Claim production ownership only for parts you actually shipped. Volumes below are story-scale so the design has something to push against.

**Story scale:** about 1,200 help articles, 80 policy documents, roughly 2 million child chunks, about 40,000 contacts a month. The product is an agent copilot that drafts a cited reply. A customer-facing bot is allowed only for order status and already-published articles.

**Companion:** [15 LLM Concepts](./llm-15-concepts-cqrs.md) is the model side of the same system.

---

## Two meanings of CQRS

The product name is the Customer Query Resolution System. In system design, CQRS means Command Query Responsibility Segregation: reads and writes are different paths.

| Path | Owns | Model is allowed to |
| --- | --- | --- |
| Query / read | Hybrid search, graph hop, get order, get subscription, get shipment | Call freely inside the step budget |
| Command / write | Refund of invoice INV-8831, advance replacement | Propose. A person confirms. The service executes, and the case stores the citation ids |

---

## The ticket to memorize

Priya, India market, writes that she received an X200 on 2 October under order 18492, the screen cracked when it fell, and Care+ was charged twice. She wants a new phone and the extra money back.

Tools, before any policy search, already know: company-site sale on 2 October 2026, Care+ active, two charges of ₹1,499, second invoice INV-8831 with no extra entitlement, fraud score low. Those facts are filters and reply content. They are not guessed from embeddings.

Gold facts a correct reply must be allowed to use:

- Drop damage is covered by Care+ v4.
- Deductible is ₹2,499.
- Photos are required, and one claim is allowed per 12 months.
- The duplicate charge is refundable to the original payment method.

A first draft that says "free replacement" and "we will refund shipping" is wrong even if it sounds helpful. The deductible sentence contradicts the first claim. No span mentions shipping.

---

## Pipeline

Offline, a policy publish becomes a versioned document. Online, one conversation becomes a context. Evaluation sits on both, because a chunking change is a quality change.

| Stage | What happens | On Priya's ticket |
| --- | --- | --- |
| Ingest | Published articles, versioned policies, known-issue notes, redacted resolved tickets | Care+ publish lands with effective dates |
| Chunk | Structure-aware children and parents; fee and exclusion lines pinned | Deductible sentence is a child of the accidental-damage section |
| Embed | One pinned multilingual model on every child; identifiers also stored raw | Hindi and English customer wording share a space with English SOPs |
| Index | pgvector HNSW, OpenSearch BM25, Postgres graph and ACL | Order, product, subscription, policy version are graph nodes |
| Rewrite | Resolve follow-ups, split multi-intent messages, optional HyDE | "The extra money" becomes a duplicate Care+ charge query |
| Retrieve | Same metadata filter on both indexes, reciprocal rank fusion, optional one-hop graph bias | market=IN, product=X200, policy effective on the purchase date |
| Rerank | Cross-encoder on child chunks; keep 5–8 | Accidental-damage clause outranks generic warranty |
| Shape | Expand to the parent, compress extractively, pin fee and exclusion lines | Parent brings ₹2,499, photos, and the loss/theft exclusion |
| Generate | Cited draft: one resolution per issue, plus proposed commands | Replacement proposal and refund proposal |
| Judge | Entailment against cited spans; weak coverage escalates | "Free replacement" is rejected |

Illustrative p95 budget for one issue, which you state and then measure: rewrite 400 ms, order plus subscription 80 ms in parallel, hybrid search 80 ms, rerank of the top 50 children 150 ms, expand and compress 20 ms, generate 1.2 s, faithfulness 400 ms. Common path near 2.5 seconds. The agent loop, if it uses all three retrieval rounds, stays under 8 seconds.

If retrieval returns nothing, the system asks a clarifying question, escalates, or refuses. It does not fill the gap from model memory.

---

## 01 Chunking

Embedding models score passages, and the generator attends to a bounded window. A whole policy PDF averages the one useful clause with unrelated sections, so nearest-neighbor search misses it. A single sentence often drops the exception that changes the decision, which lives in the next paragraph.

Split on structure first: headings, numbered clauses, FAQ pairs, ticket turns. Prose with no structure falls back to paragraphs, then sentences, into a window of about 256–512 tokens, with 10–20% overlap so a sentence on a boundary survives in both neighbors. Tables stay intact. Every chunk stores a parent id, source offsets, and the heading path. Overlap increases index size and duplicate hits, so you dedupe by parent before generation.

Care+ splits on clause boundaries: eligibility, deductible, exclusions, claim steps. A resolved ticket becomes two linked chunks. The resolution chunk is what you search for "how we fixed this." The problem chunk carries the wording real customers use.

There is no universal chunk size. Change it only when context recall on a labeled ticket set moves. Cutting a fee table in half, or separating an exclusion from the rule it modifies, is a retrieval bug.

**Say:** "I chunk by document structure, overlap only where a clause would be cut, and keep a parent pointer so a precise hit can expand into the section."

## 02 Embedding models

A bi-encoder maps the query and the chunk independently, then compares them with cosine or dot product. Document vectors are computed once. That independence is why search is fast, and why a bi-encoder is weaker than a model that sees both texts together.

Training is contrastive (InfoNCE and its relatives): pull the query toward a relevant passage, push it from negatives. Asymmetric models expect a short query and a long passage. E5 and BGE want an explicit query or passage prefix. Matryoshka models such as text-embedding-3 let you truncate the dimension. Pin the model, the dimension, and the prefix rules in the index name. A model change means a full re-embed and an atomic alias swap. If the index uses inner product to approximate cosine, normalize the vectors.

Customers mix Hindi and English. SOPs are English. One multilingual space covers both, and the rewriter may also emit an English search string so the query sits nearer the policy prose. Order ids, error codes, and GSTIN strings are weak in that geometry. That is the job of hybrid search.

**Say:** "Dense retrieval closes the vocabulary gap. I pin the model version and re-embed the corpus when it changes."

## 03 Vector database

Exact k-nearest neighbor is a scan. Approximate nearest neighbor returns the top k inside a millisecond budget, with a recall target you measure against brute force.

HNSW is a layered small-world graph. Search starts at the top layer and walks greedily toward the query. Build knobs are M (links per node) and efConstruction. The query knob is efSearch: higher finds better neighbors and costs latency. IVF with product quantization compresses huge collections and gives up some recall.

At a few million chunks, Postgres with pgvector keeps vectors next to the metadata you already filter on. Qdrant, Milvus, Weaviate, or OpenSearch kNN earn their place at higher QPS, or when you want a managed hybrid index. Resolve stores child vectors in pgvector and the same chunk ids in OpenSearch for BM25. A blue-green alias such as `chunks-embed-v3` swaps a new model or a new policy publish without downtime. Redis caches embeddings for repeated queries such as "track my order."

The interview trap is the filter interacting with the graph. Post-filtering can return fewer than k hits because neighbors are discarded after the walk. Pre-filtering can miss neighbors if the graph was built on the unfiltered set. Know which your engine does, and test filtered recall on a rare product, not on the whole catalog.

**Say:** "I use ANN for latency, I measure its recall against brute force, and I keep ACL metadata where the filter can actually be enforced."

## 04 Metadata filtering

Similarity is a soft score. Tenant, market, product, visibility, and effective dates are predicates. A chunk that fails the predicate is skipped, however close its vector is.

Every chunk carries tenant, market, product ids, source type, visibility (`public`, `customer`, `agent`, `internal`), status, and an effective date range. The same predicate runs on the vector query and the keyword query before fusion. Customer traffic uses `public` and `customer`. The agent copilot may also include `agent`. Drafts and retired versions stay out. An open case stores a policy-as-of timestamp, so an audit retrieves what was in force when the case started, even after this morning's publish.

Priya's filter is market IN, product includes X200, source published, effective on 2 October 2026, channel company-site, visibility agent. A US warranty and a marketplace-channel exclusion never enter the prompt.

A prompt instruction to "ignore internal notes" is too late if those notes were already retrieved. Filtering is the authorization boundary. Log the filter with the query. A filter that is too tight, because the chat parser picked the wrong product id, looks like an empty knowledge base, and the model may answer from memory. Empty results escalate or clarify.

**Say:** "Tenant, visibility, and effective date are mandatory filters in the data-access layer. The model only sees chunks the caller is allowed to know."

## 05 Query rewriting

Support chat is anaphoric. "And the extra money?" is a useless search string. Rewriting folds the last few turns and facts already fetched (product, order id, market) into a standalone query a stranger could run against the corpus.

A small model resolves pronouns, expands the product name, and drops greetings. Identifiers take a deterministic path: order id, IMEI, and error code are attached verbatim and the model is not allowed to paraphrase them. Log the raw utterance and the rewrite. On risky tickets, retrieve with both and fuse, so a bad rewrite cannot erase the customer's words.

Priya's second turn, "the screen cracked when it fell, and you charged me twice for Care+," becomes two queries: accidental screen damage under Care+ for an India X200 purchased 2 October 2026, and a duplicate Care+ subscription charge. "Twice" and "the extra money" become "duplicate charge."

The rewriter can invent a constraint she never said, such as "free replacement," and then retrieval only finds passages that match the invention. Constrain it to the chat and the tool facts.

**Say:** "I rewrite multi-turn chat into standalone queries, and I keep identifiers verbatim."

## 06 HyDE

Hypothetical Document Embeddings (Gao et al.) attack a style mismatch. Customer questions are short and emotional. Policy passages are long and formal. A fake answer written in the voice of a help article sits closer, in vector space, to the real passage than the raw question does.

The model drafts that passage. You embed the draft and search. You discard the draft. You still embed the original query and fuse the two lists, so a confidently wrong hypothesis can only add candidates. The reranker makes the final call. Skip HyDE when the query is mostly an identifier: BM25 already handles "order 18492" and "E-17." HyDE is an extra model call, so it is reserved for short, vague, semantic questions.

"Phone died after it got wet in the rain" becomes a hypothetical SOP paragraph about liquid ingress, port corrosion, and the Care+ liquid-damage exclusion. The vector lands on the moisture policy even though the customer never said "liquid damage."

Showing that draft to the customer is a hallucination by construction. HyDE output is an internal search key.

**Say:** "HyDE is a retrieval query written in document style. I fuse it with the real query and throw the draft away."

## 07 Query decomposition

One embedding of a multi-intent message averages the intents, and the second issue is under-retrieved. Independent sub-questions run in parallel, each with its own hybrid search, then the contexts are grouped. Dependent questions run in order (least-to-most) when the answer to one is an input to the next. A router decides. "What is the refund window?" stays whole. Cap sub-questions, usually at three. The decomposer may not invent intents. The synthesizer must answer every sub-question or say which one is unresolved.

Priya splits into accidental-damage replacement and a refund of the duplicate Care+ charge. The case is stored as two issue lines so QA can score them separately. "Is the deductible waived because she is unhappy?" is not added.

**Say:** "I decompose only when an intent classifier sees multiple asks, and a missed sub-question stays visible in the draft."

## 08 Hybrid search

BM25 scores term overlap using term frequency, inverse document frequency, and length normalization. It owns order ids, error codes, SKUs, section numbers, and firmware versions. Dense search owns paraphrases, where the customer and the document share a meaning and almost no tokens. Both run under the same metadata filter, then the ranked lists are fused.

Reciprocal rank fusion needs no shared score scale. For each list, a document at 1-based rank \(r\) adds

\[
\frac{1}{k + r}
\]

with \(k\) usually 60. Sum across lists and sort. A document that appears in both lists floats upward. A weighted sum of normalized scores can beat RRF once you have labels to tune the weight. Until then, RRF is the default. Analyzers must not stem or split product codes: AX3000 stays AX3000. SPLADE is an optional third lane, learned sparse expansion inside a lexical index.

"Error E-17 on router AX3000, keeps dropping": BM25 puts the E-17 runbook first; vectors add the generic intermittent-Wi-Fi article; RRF keeps that order. A pure vector index often buries E-17 because the code is a rare token with a weak geometric signal. Order 18492 is found the same way, then confirmed by the order service, which is the system of record. Fusing two lists that were filtered differently can surface another tenant's chunk or a retired policy. Apply the predicate inside each retriever before fusion.

**Say:** "Keyword search owns identifiers and vector search owns paraphrases. I fuse them with RRF under one filter, and I protect product codes from the analyzer."

## 09 Reranking

The bi-encoder never lets query tokens interact with document tokens. A cross-encoder reads the pair and outputs a relevance score. It is too expensive for millions of chunks and cheap enough for a shortlist of 30 to 100. The generator then sees the best 5 to 8.

Score the rewritten query against the child chunk, because the child is the precise unit and usually fits the reranker window. Expand parents after the rerank. Production defaults are pointwise cross-encoders: BGE reranker, Cohere Rerank, or a MiniLM trained on MS MARCO. An LLM listwise rerank is reserved for offline eval or a tiny top-k. ColBERT is the middle path: token vectors stored at index time, late interaction at query time, stronger than a bi-encoder and faster than a full cross-encoder.

On this ticket the shortlist contains the generic warranty, the repair-depot article, and the Care+ accidental-damage clause. Given "replacement after a drop, Care+, X200," the cross-encoder promotes the accidental-damage clause. Reranking a 2,000-token parent dilutes the score and may truncate. A 50-pair cross-encoder is often the second-slowest hop after generation, so it belongs in the latency budget.

**Say:** "I retrieve wide and rerank narrow. Only the top children are expanded and sent to the generator."

## 10 Small-to-big retrieval

Small chunks match precisely and omit the sentence that changes the decision. Large chunks contain that sentence and match poorly. Index and rerank the child. Generate from the parent section, or from a sentence window around the hit. If several children share a parent, include that parent once (auto-merge). Record which child span triggered it, so the citation can highlight a sentence inside the section.

The child "one advanced replacement per 12 months" matches Priya and would support an incomplete answer. The parent also contains the ₹2,499 deductible, the photo requirement, and the exclusion for loss and theft. The generator reads the parent. Expanding every child into a full PDF chapter crowds the prompt. Cap parent size.

**Say:** "Precision comes from searching small chunks. Safety comes from expanding to the parent so the deductible next to the hit is still in context."

## 11 GraphRAG

Some questions are about links: this order, this device, this subscription, this policy version, these exclusions. A vector index retrieves text that sounds relevant. A graph retrieves the records that are actually connected.

For daily tickets, build a typed graph from systems of record. Nodes: Customer, Order, Product, Subscription, Policy, Clause, Symptom, ErrorCode. Edges: ORDER_FOR, SUBSCRIPTION_COVERS, POLICY_APPLIES_TO, CLAUSE_EXCLUDES, ERROR_AFFECTS. At query time, link entities in the utterance, walk one or two hops, and restrict vector search to the policies those hops name.

Microsoft GraphRAG (Edge et al., 2024) is the heavier idea: extract entities from unstructured text, cluster them (Leiden communities), summarize the communities, and answer corpus-level questions from those summaries. That global search is a second product, for "what are people escalating about this week." Local search is the daily agent path. Do not run an LLM entity extractor over raw tickets. It is expensive and it pulls personal data into the graph. Prefer structured records, redact free text, and extract edges from published policies.

Order 18492 links to X200, sold 2 October 2026 on the company site, and to Care+ v4. Policy node `careplus-ad-v4` applies to the X200, excludes loss and theft, and covers drop damage with a deductible. A generic "screen replacement" article from an older warranty cannot outrank that node just because the wording is closer.

**Say:** "I use a small typed graph for order-to-product-to-policy-version, and I reserve community GraphRAG for questions about the whole ticket corpus."

## 12 Context compression

After parent expansion, a section still contains boilerplate and other markets. Those tokens cost money, add latency, and compete with the clause the model should use. Models also use the beginning and end of a long context more reliably than the middle (lost-in-the-middle, Liu et al.), so a deductible buried in noise is easy to miss.

Extractive compression keeps sentences verbatim, with offsets. Abstractive compression summarizes and can drop a negation, which is unacceptable for policy. LLMLingua-style token pruning is reasonable for non-contract text. Order surviving spans with the highest rerank score first. Once a parent is selected, fee, exclusion, and deadline sentences are pinned even if the compressor is unsure.

On the Care+ parent, lines that mention deductible, exclusion, or deadline cannot be dropped. A summary that says "replacement is covered" and omits "after a deductible" is a faithfulness bug introduced after retrieval succeeded.

**Say:** "I compress extractively, pin fee and exclusion sentences, and pass verbatim spans. A summary of a warranty is not a warranty."

## 13 Agentic RAG

A single retrieve-then-generate pass covers a large share of tickets. It fails when the order facts are missing, an exclusion never came back, or a second intent shows up late. An agentic loop plans a search, calls tools, looks at what returned, and stops or tries again. The loop is bounded.

Read tools: `search_knowledge`, `search_similar_tickets`, `get_order`, `get_subscription`, `get_shipment`. Write tools: refund and replacement, behind a human confirm and a policy citation. Example budget: 3 retrieval rounds and a time cap. A grader checks that each sub-question has a cited clause for eligibility, fees, and exclusions. Self-RAG is the same idea in tokens: do I need retrieval, is this passage relevant, is this claim supported. Corrective RAG (CRAG) is the explicit branch when retrieval is weak: clarify or hand off, and do not answer from weights.

On this ticket the loop loads the order and the subscription first, because those facts set the filter. It searches both sub-questions. The grader sees coverage and a missing exclusion section, so round two is specifically "Care+ accidental damage exclusions X200." Round three is unused. The refund button is filled with invoice id and amount. It does not fire inside the loop.

Unbounded loops, tools that both read and write, and a grader that is the same prompt as the generator are the failure mode. Grade against a checklist of clause types and hard-stop at three rounds.

**Say:** "The agent chooses sources and may retrieve again when a required clause is missing. It drafts. A person executes the command."

## 14 Faithfulness

Split the answer into atomic claims. A claim is faithful when the retrieved context entails it. The score is supported claims divided by all claims. Judge each claim against its cited spans only, so an unrelated chunk elsewhere in the prompt cannot launder support. A natural-language inference model or a small judge does the labeling. RAGAS faithfulness is the usual offline version.

A faithful answer can still be wrong if the source document is wrong or retired. Freshness is a metadata bug. An unfaithful answer can be factually true in the world and still be unacceptable in support, because the agent is allowed to say what approved material says.

Money, eligibility, deadlines, and identity fail closed. On a failed claim, regenerate once with that claim forbidden. A second failure drops the claim. If the reply can no longer answer the question, escalate. Citations shown to the agent are the spans the checker used.

Priya's first draft says a free replacement and a shipping refund. The context supports a replacement and states ₹2,499. It says nothing about shipping. Both claims fail. The regenerated reply states the deductible, the photos, and one claim per 12 months. Faithfulness on the sent draft is 4/4. The story target is at least 0.95 overall, and 1.00 on money claims.

**Say:** "Every eligibility or money sentence must be entailed by a cited span. I fail closed, regenerate once, then drop or escalate."

## 15 Context precision and recall

These two scores judge the retriever, before any prose quality is considered.

Context recall is the fraction of gold facts that appear somewhere in the retrieved context. It needs senior-agent labels. On this ticket the gold set is the four facts above. If the deductible parent is missing, recall falls no matter how polished the reply is.

\[
\text{context recall} = \frac{\text{gold facts present in retrieved parents}}{\text{all gold facts}}
\]

Context precision asks whether the retrieved chunks are actually useful, with a penalty when useful chunks rank low. It follows average precision: at each rank that holds a relevant chunk, compute relevant-so-far divided by rank, then average. Raising k usually lifts recall and can hurt precision. Reranking exists to repair precision. Small-to-big exists so the gold fact in the next paragraph counts as retrieved.

\[
\text{context precision} \approx \text{average precision of relevant chunks in the ranked list}
\]

Story targets: context recall at least 0.90, context precision at least 0.70 after rerank. A generator change is the wrong experiment when recall is 0.6. Label gold facts, not a single "relevant document," or the deductible in paragraph two never counts. Also track answer relevancy, citation coverage, a wrong-policy audit (retired or wrong-market clauses cited), agent edit rate, deflection only for the narrow customer-bot intents, CSAT, and handle time. A few hundred labeled tickets rerun in CI whenever chunking, embeddings, fusion, or filters change.

**Say:** "Context recall tells me the facts arrived. Context precision tells me the prompt is mostly those facts. Faithfulness tells me the reply stayed inside them."

---

## Stores

- Object storage plus a documents table: original files, parsed text, version, effective dates. Source of truth for what was published.
- Postgres chunks: child text, parent text, offsets, ACL columns. Filters and parent expansion stay transactional.
- pgvector: child embeddings, HNSW, model version.
- OpenSearch: BM25 on the same chunk ids, codes unstemmed.
- Graph tables: order, product, subscription, policy, clause edges.
- Retrieval log: raw query, rewrite, filters, ranks, claims, verdicts. This is the eval set and every production trace.
- Redis: cache for frequent query embeddings.
- A queue rechunks and re-embeds on policy publish.

If they ask for a stack: a Python FastAPI or Node orchestrator, one strong model for rewrite and generation, a smaller model for compression and the entailment check, Postgres with pgvector, OpenSearch, Redis, and traces in OpenTelemetry, LangSmith, or Phoenix. Fine-tune, if you do it, for format and tool use. Facts that change and must be cited stay in the index.

## Claim check

| Claim | Verdict | Why |
| --- | --- | --- |
| Drop damage is covered by Care+ v4 | Supported | Coverage clause in `careplus-ad-v4` |
| Deductible is ₹2,499 | Supported | Fee sentence in the same parent |
| Photos required, one claim per 12 months | Supported | Sibling sentences in that parent |
| Second Care+ charge refunds to the original method | Supported | Duplicate-charge SOP, plus the billing tool |
| Replacement is free | Rejected | Deductible sentence contradicts it |
| Shipping is refunded too | Rejected | No span mentions shipping |

## Eval targets

| Metric | Question | Story target |
| --- | --- | --- |
| Context recall | Did the gold facts arrive in the retrieved parents? | ≥ 0.90 on senior-agent labels |
| Context precision | Are the chunks in the prompt mostly those facts, ranked high? | ≥ 0.70 after rerank |
| Faithfulness | Is every sent claim entailed by its cited spans? | ≥ 0.95, and 1.00 on money claims |
| Wrong-policy audit | Did a retired or wrong-market clause get cited? | Trend to zero via effective-date filters |
| Agent edit rate | How often a person rewrites the draft before sending? | Falls as recall and faithfulness rise |

## Failures worth telling

1. Pure vector search missed order 18492 until BM25 and the order tool were added.
2. A 2024 one-year warranty outranked current terms until the effective-date filter shipped.
3. The model promised a free replacement while the deductible lived in a parent the child retriever had not expanded. Small-to-big plus the faithfulness guard closed it.
4. An India GST article was eligible for a US chat until market became a hard filter.
5. The agent loop searched "be more helpful" until the time budget. The grader became a checklist of clause types, with a hard stop at three rounds.

## Privacy

Resolved tickets are redacted before chunking. Phone numbers, email, addresses, and payment tokens never enter the embedding store or the graph. The raw ticket stays in the case system, under that system's access control. An embedding of a secret is still a secret if the text is stored beside it.

## Ninety seconds

"I designed a customer query resolution system for electronics support. The hard part was citing the right policy version, so I treated the language model as the last step. Policies are chunked by clause into children and parents, embedded with a pinned multilingual model, and indexed in pgvector and in BM25. On a ticket I load the order and subscription first, rewrite the chat into standalone queries, and split multi-issue messages. Both indexes use the same filter for market, product, visibility, and effective date, and reciprocal rank fusion merges them. A cross-encoder keeps the best children, I expand those to parent sections so deductibles and exclusions survive, and I compress extractively. The draft is a set of cited claims. Anything about money or eligibility that the spans do not entail is regenerated or dropped. Refunds and replacements are commands a person confirms. I evaluate context recall, context precision, and faithfulness on tickets labeled by senior agents. The quality moves I would defend came from hybrid search, metadata, and parent chunks."

## Drill answers

**Why retrieve at all, instead of stuffing the manual in the prompt or fine-tuning?** Policies change weekly, manuals do not fit a context window, and a fine-tune does not cite the clause it used. Retrieval keeps the answer on the published version and gives the agent a span to check.

**What chunk size?** Start from document structure. For leftover prose, try 256–512 tokens with modest overlap, then compare context recall. Report the measurement.

**Bi-encoder versus cross-encoder?** The bi-encoder embeds each side alone, so document vectors are precomputed and search is a nearest-neighbor lookup. The cross-encoder scores the pair jointly and rescores a shortlist. Retrieve with the first, keep the best with the second.

**Walk through RRF.** Rank \(r\) contributes \(1/(60+r)\) from that list. Sum and sort. No score normalization. A document in both lists floats upward. Filter inside each list before you fuse.

**The bot promised a free replacement. Where did the design fail?** Either the deductible never arrived (recall, small-to-big, or a filter) or it arrived and the generator ignored it (faithfulness). Read the trace: filter, fused ranks, parent expansion, cited spans, claim verdicts.

**"And the price?"** Query rewriting. The previous turn named the plan. The search string becomes "Pro plan monthly price, market IN." Search never sees the bare follow-up.

**When do you skip HyDE and the agent loop?** Skip HyDE for identifier-heavy queries and whenever the extra model call breaks the latency budget. Skip the loop when the first graded retrieval already covers eligibility, fees, and exclusions for a single intent. Most tickets stay on the single-pass path.

**Faithfulness versus context recall?** Recall asks whether the gold facts were retrieved, and it needs labels. Faithfulness asks whether claims in this answer are entailed by the retrieved text, and it does not need a gold answer. You want both.

**Where is Command Query Responsibility Segregation?** The product name is the Customer Query Resolution System. Architecturally, reads are retrieval plus order and subscription lookups. Writes are refund and replacement commands, executed after a person confirms, with a citation attached. The model drafts. It does not commit the command.

**A policy was updated this morning. What happens to an open case?** New chats filter to the version in force now. The open case stores policy-as-of and keeps retrieving the version that applied when the case started, so the audit matches what the agent was allowed to say.
