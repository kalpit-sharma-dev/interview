# 15 RAG Concepts — Mobile and Internet Banking

> Retrieval-augmented generation for a Customer Query Resolution System. Most bad support answers are retrieval failures. A stronger model cannot cite a reversal timeline that never entered the prompt.

Use this as an interview script. Each concept has the mechanism, the way it shows up on one banking ticket, a sentence you can say aloud, and the follow-up that usually comes next.

**Companion:** [15 LLM Concepts](./llm-15-concepts-cqrs.md) is the model that reads these spans and writes the draft.

---

## How to claim the project

Resolve is a Customer Query Resolution System for a retail bank's **mobile banking app** and **internet banking** portal. Call the bank Harbor Bank in the story so the name is obviously fictional. Agents were searching about 1,400 help articles and 90 operations procedures by hand: IMPS and UPI dispute SOPs, NEFT cut-offs, card-fee schedules, payee cooling rules, KYC refresh steps, and device-binding failures. New hires took weeks to learn which version applied to which channel.

The system drafts a cited reply for the contact-center agent and for the in-app secure message queue. A narrow customer-facing bot answers only published articles and payment-status lookups. It does not open disputes or move money.

Present Resolve as a system you designed and can defend. Claim production ownership only for parts you actually shipped. The volumes below are story-scale so the design has something to push against:

- About 50,000 contacts a month across the app, the portal, and the assisted channel.
- About 1,400 articles and 90 versioned procedures.
- About 2.5 million child chunks after structure-aware splitting.
- Retail India book: savings, salary, and debit cards. Credit cards, NRI, and corporate net banking are separate tenants and must not leak into this index.

There is a second meaning of CQRS that interviewers will hear. Command Query Responsibility Segregation splits reads from writes.

| Path | Owns | Model is allowed to |
| --- | --- | --- |
| Query / read | Hybrid search, one-hop graph, get account, get payment, get card fee postings | Call freely inside the step budget |
| Command / write | Raise an IMPS trace, refund a duplicate card fee, block a card, add a dispute case | Propose. A person confirms. The payment or cards service executes. The case stores the citation ids |

Reads can be wrong and retried. Writes move money, change a card state, or create a regulated complaint record. The language model drafts. It does not commit the command.

---

## The ticket to memorize

Meera, full-KYC resident savings customer, uses the mobile app. On 2 October 2026 at 14:22 IST she sent ₹25,000 by IMPS to her landlord. The app showed Success. The landlord says the money never arrived.

Known from tools, before any policy search:

- Account suffix `18492`, product savings, segment resident retail, channel mobile app.
- IMPS RRN `628418492012`, amount ₹25,000, remitter debit posted, beneficiary-bank credit flag still open after the reconciliation cycle.
- Payee was added 40 days ago, so the cooling-period rule does not apply.
- Daily IMPS limit for this account on the mobile app is ₹5,00,000. The transfer is inside the limit.
- Fraud score is low. There is no hold.
- Internet banking, which she also opened, shows the debit-card annual fee posted twice on 1 October: ₹499 for card ending `4412`, and a second ₹499 under reference `FEE-8831` with no second card on the account.

She asks for two things in one message: "Please put the 25,000 back, the landlord did not get it. Also you charged my card fee twice, I want the extra money back."

Gold facts a correct reply must be allowed to use:

1. An IMPS debit with no beneficiary credit is eligible for a trace under procedure `imps-cnr-v4` (credit not received), effective 1 April 2026.
2. If settlement confirms the credit failed, the principal ₹25,000 is credited back by the next working day (T+1). The procedure does not promise same-day reversal.
3. A goodwill interest credit is a separate clause and is not part of the standard trace.
4. A second annual debit-card fee with no second card is a billing error. Procedure `card-fee-dup-v2` refunds ₹499 to the savings account after an agent confirms the posting.

A draft that says "we have refunded ₹25,000 instantly, with interest, and we will also reverse charges at the landlord's bank" is wrong. The SOP promises a trace and a T+1 principal credit after confirmation. It says nothing about the other bank's charges. Interest is a different clause the model must not invent.

---

## Pipeline

Offline, a procedure publish becomes a versioned document with an effective window and a channel list. Online, one conversation becomes a context. Evaluation sits on both, because a chunking change is a quality change.

| Stage | What happens | On Meera's ticket |
| --- | --- | --- |
| Ingest | Published articles, versioned procedures, known-issue notes, redacted resolved contacts | `imps-cnr-v4` lands with effective dates and channels mobile + internet |
| Chunk | Structure-aware children and parents. Fee, timeline, and exclusion lines are pinned | "T+1 principal credit" is a child of the credit-not-received section |
| Embed | One pinned multilingual model on every child. RRNs and account suffixes are also stored raw | Hindi and English customer wording share a space with English SOPs |
| Index | pgvector HNSW, OpenSearch BM25, Postgres for the graph and the ACL | Account, card, payment, channel, and procedure version are graph nodes |
| Rewrite | Resolve follow-ups, split multi-intent messages, optional HyDE | "The extra money" becomes a duplicate debit-card annual fee query |
| Retrieve | Same metadata filter on both indexes, reciprocal rank fusion, optional one-hop graph bias | segment=resident-retail, product=savings, channel includes mobile, procedure effective on 2 Oct 2026 |
| Rerank | Cross-encoder on child chunks. Keep 5–8 | Credit-not-received clause outranks generic "IMPS limits" and "how to add a payee" |
| Shape | Expand to the parent, compress extractively, pin timeline and exclusion lines | Parent brings T+1, the "no automatic interest" line, and the fraud-hold exception |
| Generate | Cited draft: one resolution per issue, plus proposed commands | Trace proposal and fee-refund proposal |
| Judge | Entailment against cited spans. Weak coverage escalates | "Instant refund with interest" is rejected |

Illustrative p95 budget for one issue, which you state and then measure: rewrite 400 ms, account plus payment read 80 ms in parallel, hybrid search 80 ms, rerank of the top 50 children 150 ms, expand and compress 20 ms, generate 1.2 s, faithfulness 400 ms. Common path near 2.5 seconds. The agent loop, if it uses all three retrieval rounds, stays under 8 seconds. Payment-status reads come from the system of record. The index is not asked to know whether RRN `628418492012` has settled.

If retrieval returns nothing, the system asks a clarifying question, escalates, or refuses. It does not fill the gap from model memory. In banking, an empty retrieval on a money question is a handoff, not a guess.

---

## 01 Chunking

**What an interviewer is testing.** Can you explain why the unit of retrieval changes what the model is able to cite?

Embedding models score passages, and the generator attends to a bounded window. A whole IMPS procedure PDF averages the T+1 reversal clause with payee setup, limits, and branch escalation, so nearest-neighbor search misses the one sentence that decides the case. A single sentence often drops the exception that changes the decision, which lives in the next paragraph: "unless a fraud hold is open" or "interest is not automatic."

**How it works.** Split on structure first: headings, numbered clauses, FAQ pairs, and turns inside a resolved contact. Prose with no structure falls back to paragraphs, then sentences, into a window of about 256–512 tokens, with 10–20% overlap so a sentence on a boundary survives in both neighbors. Tables stay intact. A fee schedule or a limit table cut in half retrieves the row and loses the column header, which is how a model quotes ₹499 against the wrong card product.

Every chunk stores a parent id, source offsets, the heading path, the procedure version, and the effective window. Overlap increases index size and duplicate hits, so retrieval dedupes by parent before generation. Child chunks are what you search. Parent sections are what you later show the model. That split is concept 10. You design the ids here so the expansion is possible.

**In the banking system.** `imps-cnr-v4` splits on clause boundaries: eligibility, timeline, exclusions, evidence the customer must not be asked to re-upload, and the command the agent is allowed to raise. `card-fee-dup-v2` splits into "what counts as a duplicate posting," "refund destination," and "what is not refundable" (forex markup, ATM operator charges, EMI interest). A resolved contact becomes two linked chunks. The resolution chunk is what you search for "how we closed a credit-not-received case." The problem chunk carries the wording real customers use, including Hindi and the phrase "paisa kat gaya."

There is no universal chunk size. Change it only when context recall on a labeled contact set moves. Cutting the T+1 sentence away from the fraud-hold exception is a retrieval bug you will feel as a hallucinated instant refund.

**Say:** "I chunk by procedure structure, overlap only where a clause would be cut, and keep a parent pointer so a precise hit can expand into the section that holds the timeline and the exclusion."

---

## 02 Embedding models

**What an interviewer is testing.** Do you know what a bi-encoder can and cannot see?

A bi-encoder maps the query and the chunk independently, then compares them with cosine or dot product. Document vectors are computed once at index time. That independence is why search is fast at a few million chunks, and why a bi-encoder is weaker than a model that sees both texts together. The cross-encoder in concept 09 is that second model. You do not run it on the whole corpus.

**How it works.** Training is contrastive (InfoNCE and its relatives): pull the query toward a relevant passage, push it from negatives. In-batch negatives are the cheap default. Hard negatives are other IMPS articles that share the words "transfer" and "failed" and are the wrong procedure. Asymmetric models expect a short query and a long passage. E5 and BGE want an explicit query or passage prefix. If you embed the corpus with the passage prefix and the query with no prefix, neighbors drift and recall falls with no index error.

Matryoshka models such as text-embedding-3 let you truncate the dimension. Pin the model, the dimension, and the prefix rules in the index name, for example `chunks-embed-v3`. A model change means a full re-embed and an atomic alias swap. If the index uses inner product to approximate cosine, normalize the vectors. Mixed normalized and raw vectors silently rank the longest chunks first.

**In the banking system.** Customers mix Hindi and English in one message. Procedures are English. One multilingual space covers both, and the rewriter may also emit an English search string so the query sits nearer the SOP prose. "Landlord ko nahi mila" and "beneficiary not credited" should land on the same child. Exact tokens still fail here: RRN `628418492012`, account suffix `18492`, reference `FEE-8831`, and IFSC codes are sparse facts with a weak geometric signal. That is why hybrid search exists. Do not expect the embedding model to add the rupees or to know whether the IMPS has settled. Settlement is a tool fact.

**Say:** "Dense retrieval closes the vocabulary gap between a customer's words and a procedure's words. I pin the model version in the index name and re-embed the corpus when that version changes."

---

## 03 Vector database

**What an interviewer is testing.** Can you talk about approximate search without pretending it is exact, and do you know how filters interact with the graph?

Exact k-nearest neighbor is a scan. Approximate nearest neighbor returns the top k inside a millisecond budget, with a recall target you measure against brute force on a sample. The usual structure is HNSW, a layered small-world graph. Search starts at the top layer and walks greedily toward the query.

**How it works.** Build knobs are M (links per node) and efConstruction. The query knob is efSearch: higher finds better neighbors and costs latency. You raise efSearch before you raise k, because a larger k with a shallow walk just returns more mediocre neighbors. IVF with product quantization compresses huge collections and gives up some recall. At a few million chunks, Postgres with pgvector keeps vectors next to the metadata you already filter on: channel, segment, product, visibility, effective dates. Qdrant, Milvus, Weaviate, or OpenSearch kNN earn their place at higher QPS, or when you want a managed hybrid index.

**In the banking system.** Resolve stores child-chunk vectors in pgvector and the same chunk ids in OpenSearch for BM25. A blue-green alias swaps a new embedding version or a new procedure publish without downtime. Internet banking and the mobile app read the same alias. Redis caches embeddings for repeated queries such as "what is my IMPS limit" and "how do I reset internet banking password." It does not cache personalized payment status. Two customers asking "where is my transfer" are not the same query once the RRN differs.

The interview trap is the filter interacting with the graph. Post-filtering can return fewer than k hits because neighbors are discarded after the walk. A rare product such as a specific salary-account variant can look like an empty knowledge base. Pre-filtering can miss neighbors if the graph was built on the unfiltered set and the allowed nodes are not linked to each other. Know which your engine does, and test filtered recall on salary accounts and on internet-banking-only procedures, not on the whole catalog.

**Say:** "I use ANN for latency, I measure its recall against brute force, and I keep chunk text and ACL metadata in the same store that can enforce a channel and segment filter."

---

## 04 Metadata filtering

**What an interviewer is testing.** Do you treat entitlements as predicates, or as a sentence in the prompt?

Similarity is a soft score. Who the customer is, which channel they used, which product they hold, and which procedure was in force on the transaction date are hard constraints. A chunk that fails the predicate is skipped, however close its vector is.

**How it works.** Every chunk carries tenant, segment, product ids, channel (`mobile`, `internet`, `assisted`, `branch`), source type, visibility (`public`, `customer`, `agent`, `internal`), status, and an effective date range. The repository applies the same predicate to the vector query and the keyword query before fusion. Customer-facing traffic on the app and the portal uses visibility in (`public`, `customer`). The agent copilot may also include `agent`. Drafts, retired versions, and internal fraud playbooks stay out.

For a case opened last week, the effective-date predicate uses the case's policy-as-of timestamp, which for a payment dispute is the transaction timestamp, not "now." An audit, including an ombudsman file, must reconstruct what the agent was allowed to say about that IMPS on that day. Log the filter with the query. A filter that is too tight, because the chat parser picked credit card instead of debit card, looks like "the knowledge base has nothing," and the model may answer from memory.

A prompt instruction to hide internal notes is too late if those notes were already retrieved. Filtering is the authorization boundary. Another customer's statement chunk is another customer's data. The predicate includes the account id from the authenticated session, not an account id the model extracted from free text.

**In the banking system.** Meera's filter is segment resident-retail, product includes savings and the debit card on that account, channel includes mobile (the payment) and internet (the fee she noticed in the portal), source published, procedure effective on 2 October 2026, visibility agent for the copilot. An NRI remittance article, a corporate net-banking limit, and a 2024 SOP that promised reversal in three days never enter the prompt. The mobile app and internet banking share some procedures and differ on others: device binding, MPIN versus password, and session timeout are channel-specific. The filter carries the channel of the transaction being discussed, not only the channel of the current chat. She is in the app now, talking about an app payment and a fee she saw in internet banking. Both channels are in scope. A branch-only waiver grid is not.

**Say:** "I treat segment, channel, visibility, and effective date as mandatory filters in the data-access layer. The model only sees procedures the caller is allowed to know, for the product and the day of the transaction."

---

## 05 Query rewriting

**What an interviewer is testing.** Can you turn a messy banking chat into a search string without inventing a promise?

Support chats are anaphoric. The follow-up "and the extra money?" is a useless search string. It might mean the IMPS amount, a charge at the other bank, or the second card fee. Rewriting folds conversation state and known account facts into a standalone query that could be handed to a stranger with the corpus.

**How it works.** A small, fast model receives the last few turns plus structured facts already fetched (product, account suffix, channel, RRN if present) and emits one or more search queries. It resolves pronouns, names the rail (IMPS, UPI, NEFT), and drops greetings. Identifiers take a deterministic path: RRN, UTR, UPI transaction id, account suffix, and card last4 are attached verbatim. The model is not allowed to paraphrase them or to "fix" a digit. Log the raw utterance and the rewrite. On money conversations, retrieve with both and fuse, so a bad rewrite cannot erase the customer's words.

**In the banking system.** Meera's message becomes two standalone queries. One is "IMPS ₹25,000 on 2 October 2026, RRN 628418492012, mobile app, debit posted, beneficiary not credited, resident savings." The other is "duplicate debit card annual fee ₹499, reference FEE-8831, card 4412, no second card, seen in internet banking." "Put the 25,000 back" becomes a credit-not-received query. "The extra money" becomes the duplicate fee, because the tool payload shows two fee postings and she said "card fee twice." The rewriter must not add "instant" or "with interest." Those words are not in the chat or the tools. If it adds them, retrieval goes looking for a waiver article and the trace SOP drops in rank.

**Say:** "I rewrite multi-turn banking chat into standalone search queries, and I keep RRNs and fee references verbatim so the rewriter cannot paraphrase an identifier into something plausible and wrong."

---

## 06 HyDE

**What an interviewer is testing.** Do you know Hypothetical Document Embeddings as a retrieval trick, and do you know when it is dangerous in payments?

HyDE (Gao et al.) attacks a style mismatch. Customer questions are short and emotional. Procedures are long and formal. A fake answer written in the voice of an SOP sits closer, in vector space, to the real passage than the raw question does.

**How it works.** The model drafts a passage that would answer the question if it were a help-center article. You embed that draft and search. You discard the draft. You still embed the original query and fuse the two lists, so a confidently wrong hypothesis can only add candidates. The reranker makes the final call. Skip HyDE when the query is mostly an identifier: BM25 already handles an RRN, a UTR, and `FEE-8831`. HyDE costs a model call on the latency path, so it is reserved for short, vague, semantic questions. Showing the draft to the customer is a hallucination by construction. In banking that draft might say "your money has been reversed," which is an action that has not happened.

**In the banking system.** "Paisa kat gaya, landlord ko nahi mila" becomes a hypothetical SOP paragraph about an IMPS debit at the remitter, a missing credit flag at the beneficiary bank, the reconciliation cycle, and a T+1 principal credit. That vector lands on `imps-cnr-v4` even though the customer never said "credit not received" or "T+1." You do not show her that paragraph. A second vague question, "the app kicked me out while paying," can use HyDE to reach the mobile session-timeout article. An RRN pasted alone does not need HyDE.

**Say:** "HyDE is a retrieval query written in procedure style. It is discarded after search. I fuse it with the real query so a wrong hypothesis can only add candidates, and the reranker makes the final call."

---

## 07 Query decomposition

**What an interviewer is testing.** Can you stop one embedding from averaging two banking intents into a mush?

One message often contains several intents. A single embedding of the whole message averages them, and the fee issue is under-retrieved because the IMPS story is longer. Decomposition searches each intent and stitches the contexts together before generation.

**How it works.** Independent sub-questions run in parallel: separate hybrid searches, then a grouped context. Dependent sub-questions run in order when the answer to one is an input to the next. Example of a dependent pair: "is this payee inside the cooling period?" must be answered from the payee-added timestamp before you search the cooling-period procedure as if it applies. A router decides. "What is the NEFT cut-off?" stays whole. Cap sub-questions, usually at three. The decomposer may not invent intents. "Should we waive the fee because she is worried about rent?" is not a third question. The synthesizer must answer every sub-question or explicitly say which one is unresolved.

**In the banking system.** Meera splits into an IMPS credit-not-received trace for RRN `628418492012`, and a refund of duplicate annual fee `FEE-8831`. Each search has its own filter hints. The payment search is channel mobile, product savings, effective on 2 October. The fee search is product debit card, channel internet (where the posting was displayed) and mobile (where the card is managed). The draft is a two-part resolution. The case is stored as two issue lines so QA can score them separately. A failed IMPS does not automatically make a card fee refundable, and a fee refund does not close the trace.

**Say:** "I decompose only when an intent classifier sees multiple asks. Each sub-question retrieves on its own, and the answer is structured so a missed sub-question is visible to the agent."

---

## 08 Hybrid search

**What an interviewer is testing.** Can you walk through reciprocal rank fusion and explain why payments need keywords?

BM25 scores exact term overlap, with term frequency, inverse document frequency, and length normalization. It owns RRNs, UTRs, UPI transaction ids, IFSC codes, account suffixes, fee references, procedure ids, and section numbers. Dense search owns paraphrases: "landlord did not get it" and "beneficiary not credited." Hybrid search runs both under the same metadata filter and fuses the ranked lists.

**How it works.** Reciprocal rank fusion needs no shared score scale. For every list, a document at 1-based rank \(r\) adds

\[
\frac{1}{k + r}
\]

with \(k\) usually 60. Sum across lists and sort. A document that appears in both lists floats upward. A weighted sum of normalized scores can beat RRF once you have a labeled set to tune the weight. Until then, RRF is the default. Analyzers must not stem or split payment codes. `SBIN0001234` has to stay one token. `628418492012` must not be broken into a number the analyzer treats as a quantity. Learned sparse models such as SPLADE are an optional third lane if you need semantic expansion inside a lexical index.

Fusing two lists that were filtered differently can surface another segment's procedure or a retired timeline. The predicate is applied in each retriever before fusion. The system of record, not the index, confirms that the RRN exists and what the settlement flag is. Search finds the procedure. The payment service finds the payment.

**In the banking system.** "RRN 628418492012, landlord did not get 25,000" — BM25 locks the RRN and any known-issue note that names it. Vectors add the credit-not-received clause from the paraphrase. RRF keeps both. A pure vector index often buries the RRN because it is a rare token. The same pattern applies to UPI: a 12-digit NPCI transaction id is a BM25 problem, and "UPI showed pending and then failed" is a vector problem. Order of operations on a UPI timeout article versus an IMPS article matters, because the timelines differ. The rail comes from the payment tool, and it is part of the filter, so a UPI procedure cannot win on wording alone when the tool says IMPS.

**Say:** "Keyword search owns payment identifiers and vector search owns paraphrases. I fuse them with reciprocal rank fusion under one metadata filter, and I protect RRNs and IFSC codes from the analyzer."

---

## 09 Reranking

**What an interviewer is testing.** Why retrieve 50 chunks and show the model only a handful?

The bi-encoder never lets query tokens interact with document tokens. A cross-encoder reads them together and outputs a relevance score. It is too expensive to run on millions of chunks and cheap enough to run on a shortlist of 30 to 100. The generator then sees the best 5 to 8, which cuts distraction and the chance that a limit article outtalks a reversal article.

**How it works.** Candidates come from hybrid search. The cross-encoder scores the rewritten query against the child chunk, because the child is the precise unit and usually fits the reranker window. Parents are expanded after the rerank. Pointwise cross-encoders (BGE reranker, Cohere Rerank, a MiniLM trained on MS MARCO) are the production default. An LLM listwise reranker is more expensive and reserved for offline evaluation or a tiny top-k. ColBERT is the middle path: token vectors stored at index time, late interaction at query time, stronger than a bi-encoder and faster than a full cross-encoder.

Reranking a 2,000-token parent dilutes the score and may truncate the timeline sentence. Rerank the child that matched, then expand. Budget the latency. A 50-pair cross-encoder is often the second-slowest hop after generation.

**In the banking system.** Hybrid search returns the generic IMPS overview, the payee-setup article, the mobile daily-limit table, and the credit-not-received clause. The cross-encoder, given "IMPS debit posted, beneficiary not credited, RRN present, no fraud hold," promotes the credit-not-received clause and the T+1 sentence over "how to add a payee." For the fee issue, it promotes the duplicate-annual-fee clause over the forex-markup article, because the query says annual fee and a second posting with no second card.

**Say:** "I retrieve wide and rerank narrow. The cross-encoder sees the query and each child chunk together, and only the top of that list is expanded and sent to the generator."

---

## 10 Small-to-big retrieval

**What an interviewer is testing.** How do you stop a precise hit from hiding the sentence that forbids the promise?

Small chunks match precisely and omit the sentence that changes the decision. Large chunks contain that sentence and match poorly, because the embedding is an average of timelines, exclusions, and branch steps. Small-to-big indexes the small unit and generates from the larger unit it belongs to.

**How it works.** Child chunks are sentences or short windows with a parent id. Search and rerank operate on children. Before generation, each selected child is replaced by its parent section, or by a sentence window around the hit. If several children share a parent, that parent is included once (auto-merge) and the duplicate children are dropped. The prompt records which child span triggered the parent so the citation can point at a sentence inside a section. Cap parent size. Expanding every child into the full payments manual recreates the original problem.

**In the banking system.** The child "principal is credited back on T+1 after settlement confirms failure" matches Meera's request and would support an incomplete answer if it were the only text in the prompt. The parent section also contains the fraud-hold exception, the line that interest is not part of the standard trace, and the evidence the agent must attach (RRN, debit timestamp, beneficiary IFSC). The generator reads the parent. The citation highlight stays on the T+1 span plus the no-interest span. On the fee side, the child "second annual fee with no second card" expands to the parent that says the refund goes to the savings account, not as a card-network chargeback, and that ATM operator charges are out of scope.

**Say:** "Precision comes from searching small chunks. Safety comes from expanding to the parent section so a timeline, an exclusion, or a refund destination stored next to the hit is still in context."

---

## 11 GraphRAG

**What an interviewer is testing.** When is a graph the right index, and when is community summarization a different product?

Some questions are about links: this account, this card, this payment, this channel, this procedure version, these exclusions. A vector index retrieves text that sounds relevant. A graph retrieves the records that are actually connected.

**How it works.** For contact resolution, build a typed graph mostly from systems of record. Use the LLM to extract edges only from published procedures, not from raw chats. Nodes include Customer, Account, Card, Payment, Payee, Channel, Procedure, Clause, Rail (IMPS, UPI, NEFT). Edges include ACCOUNT_HOLDS, CARD_ON, PAYMENT_FROM, PAYMENT_ON_RAIL, PROCEDURE_APPLIES_TO, CLAUSE_EXCLUDES, CHANNEL_OFFERS. At query time, link entities in the utterance to nodes the tools already resolved, walk one or two hops, and restrict vector search to the procedures those hops name.

Microsoft GraphRAG (Edge et al., 2024) adds a heavier path: extract entities from unstructured text, cluster them with Leiden communities, summarize the communities, and answer corpus-level questions from those summaries. That global search is a second product, for "what are people escalating about on UPI this week." Local search is the daily agent path. Building a full LLM-extracted graph over raw contacts is expensive and drags account numbers and card data into the graph. Prefer structured records from the core, the card system, and the payment switch. Redact free text.

**In the banking system.** Account `18492` links to a resident savings product, to debit card `4412`, and to payment RRN `628418492012` on rail IMPS, channel mobile, at 14:22 on 2 October 2026. Procedure node `imps-cnr-v4` applies to that rail and channel and has an exclusion edge for payments under an open fraud hold. The fee node `FEE-8831` links to the same card with a duplicate-posting flag and to `card-fee-dup-v2`. The retriever is biased toward those two procedure nodes. A generic "refund my money" article from the card-chargeback SOP cannot outrank the IMPS procedure just because the wording is closer. A UPI community summary might tell operations that session timeouts spiked after a release. It is not what Meera's agent reads.

**Say:** "I use a small typed graph for connections the vector index cannot see — account to card to payment to the procedure version in force — and I reserve community-level GraphRAG for questions about the whole contact corpus."

---

## 12 Context compression

**What an interviewer is testing.** How do you shorten a procedure without dropping a negation?

After small-to-big expansion, a section still contains branch steps, other channels, and unrelated rails. Those tokens cost money, add latency, and compete with the clause the model should use. Models use the beginning and end of a long context more reliably than the middle (lost-in-the-middle, Liu et al.), so a T+1 line buried in noise is easy to miss, and a "not" is even easier.

**How it works.** Extractive compression keeps sentences the question needs, copied verbatim with their offsets. Abstractive compression summarizes a chunk and can drop a negation, so "interest is not automatic" becomes "interest is available." That is unacceptable for a payments procedure. Token-pruning methods such as LLMLingua are a third option when the text is not a customer-impacting rule, for example a long known-issue narrative. Order the surviving spans with the highest rerank score first. Always keep timeline, amount, exclusion, and destination sentences once their parent was selected, even if the compressor is unsure.

**In the banking system.** The full IMPS manual chapter is far larger than the credit-not-received section. Compression may keep the eligibility sentence, the T+1 sentence, the fraud-hold exception, and the no-automatic-interest sentence, and drop NEFT cut-off tables that rode along. Those four categories are pinned: timeline, amount, exclusion, destination. On the fee parent, "refund to the savings account" and "not a card-network chargeback" are pinned. A summary that says "the fee will be reversed" and omits the destination and the agent-confirm step is a faithfulness bug introduced after retrieval succeeded.

**Say:** "I compress extractively, keep timeline and exclusion sentences by rule, and pass verbatim spans with citations. A summary of a payments procedure is not the procedure."

---

## 13 Agentic RAG

**What an interviewer is testing.** How do you let the model look things up again without letting it pay anyone?

A single retrieve-then-generate pass is right for "what is the NEFT cut-off?" and wrong for Meera. The payment flag, the fee posting, and an exclusion can each be missing on the first pass. An agentic loop lets a controller plan a search, call tools, look at what came back, and stop or try again. The loop is bounded.

**How it works.** Tools are narrow. Read tools: `search_knowledge`, `search_similar_contacts`, `get_account`, `get_payment`, `get_card_fees`, `get_payee`. Write tools: `raise_imps_trace`, `refund_card_fee`, `block_card`, `open_complaint`. Writes sit behind an agent confirmation plus a procedure citation. The controller has a step budget (for example 3 retrieval rounds), a time budget, and a grader that checks whether each sub-question has a cited clause covering eligibility, timeline, amount, and exclusions. Self-RAG style reflection — do I need retrieval, is this passage relevant, is this claim supported — is the same idea baked into tokens. Corrective RAG adds an explicit branch when the retrieved set is weak: ask a clarifying question or hand off, and do not fill the gap from model memory.

Fetch the payment and the fee postings before any procedure search, because those facts set the metadata filter and the rail. Never let the loop search "be more helpful" as a query. The grader is a checklist of clause types, not a second copy of the generator prompt.

**In the banking system.** The loop calls `get_payment(628418492012)` and `get_card_fees(18492)` first. It learns the rail is IMPS, the credit flag is open, fraud score is low, and `FEE-8831` is a second annual fee. It searches the two sub-questions. The grader notices the first pass has the T+1 line and is missing the exclusion section, so the second query is specifically "IMPS credit not received exclusions, fraud hold, interest." Round three is unused. The trace tool and the fee-refund tool are offered to the human as buttons, with RRN, amount, and citation ids filled in. They do not fire inside the loop. Blocking the card is not proposed, because nothing in the evidence says the card is compromised.

**Say:** "The agent chooses sources and may retrieve again when a required clause is missing. It stops on a step budget. It can draft a trace or a fee refund, and a person executes the command."

---

## 14 Faithfulness

**What an interviewer is testing.** Can you separate "the sentence is true in the world" from "the sentence is supported by the spans we retrieved"?

Faithfulness is support, claim by claim. Split the answer into atomic claims. A claim is faithful when the retrieved context entails it. The score is supported claims divided by all claims. A faithful answer can still be wrong if the source procedure is wrong. An unfaithful answer can be factually true and still unacceptable in a bank, because the agent is allowed to say what the approved procedure says, not what the model remembers from the internet.

**How it works.** Generation emits claims with citation ids pointing at chunk spans. A checker scores each claim against its cited spans only, so an unrelated chunk elsewhere in the prompt cannot launder support. Natural-language inference models, or a small judge model, do the labeling. RAGAS faithfulness is the common offline version of this. Claims about money, timelines, eligibility, and identity fail closed. On a failed claim, regenerate once with that claim marked forbidden. A second failure removes the claim and, if the reply can no longer answer the question, escalates to a person. Citations shown to the agent are the spans the checker used.

Judging faithfulness against the model's world knowledge rewards confident uncited answers. A faithful quote of a retired "three-day reversal" SOP is a document-lifecycle bug, which metadata filtering is there to prevent. Track freshness separately.

**In the banking system.** A first draft says "We have refunded ₹25,000 instantly with interest, and we will reverse the landlord's bank charges." The context supports a trace and a T+1 principal credit after settlement confirms failure. It says interest is not part of the standard trace. It says nothing about the other bank's charges. Those claims fail. The regenerated reply says: the RRN is eligible for a trace, the principal comes back on T+1 if settlement confirms the credit failed, interest is not included, and the duplicate ₹499 fee can be refunded to the savings account after the agent confirms `FEE-8831`. Faithfulness on the sent draft is 4/4. Story target: at least 0.95 overall, and 1.00 on amount and timeline claims.

**Say:** "Every amount or timeline sentence must be entailed by a cited span. Faithfulness is that ratio. I fail closed on money and dates, and I regenerate or escalate."

---

## 15 Context precision and recall

**What an interviewer is testing.** Can you tell a retrieval problem from a writing problem?

These two scores judge the retriever, before any prose quality is considered. Context precision is the fraction of retrieved chunks that are actually useful, with a penalty when useful chunks rank low. Context recall is the fraction of facts required to answer that appear somewhere in the retrieved context. Recall needs a labeled gold answer. Precision can be judged from the query, the chunks, and a relevance label.

**How it works.** On a golden set, senior agents mark the spans a correct reply must be allowed to rely on. Context recall is covered gold facts over all gold facts:

\[
\text{context recall} = \frac{\text{gold facts present in retrieved parents}}{\text{all gold facts}}
\]

Context precision follows an average-precision pattern. At each rank that holds a relevant chunk, compute relevant-so-far over rank, then average:

\[
\text{context precision} \approx \text{average precision of relevant chunks in the ranked list}
\]

Raising k usually lifts recall and can hurt precision. Reranking exists to repair precision. Small-to-big exists so the gold fact in the next paragraph counts as retrieved. A generator change is the wrong experiment when recall is low. A fluent model cannot cite a T+1 clause that never arrived. Label gold facts, not a single "relevant document," or the no-interest sentence in paragraph two never counts.

**In the banking system.** The gold facts on Meera's contact are the four listed at the top of this note. If the parent that holds "interest is not automatic" is missing, context recall falls no matter how polished the apology is. The eval set is a few hundred real contacts labeled once, then rerun in CI whenever chunking, embeddings, fusion, or filters change. Include adversarial cases: Hindi plus an RRN, a fee reference that looks like an RRN, a mobile chat about an internet-banking posting, a transaction from last month after the procedure changed, and an NRI customer who must not receive the resident SOP.

Story targets: context recall at least 0.90, context precision at least 0.70 after rerank. Also track citation coverage, wrong-procedure audit (retired timeline, wrong rail, wrong segment), agent edit rate, deflection only for the narrow status bot, CSAT, and handle time. Deflection on money-movement intents is not a success metric.

**Say:** "I separate retrieval metrics from answer metrics. Context recall tells me the facts arrived. Context precision tells me the prompt is mostly those facts. Faithfulness tells me the reply stayed inside them."

---

## Stores

| Store | Holds | Why it is separate |
| --- | --- | --- |
| Object storage + documents table | Original procedures, parsed text, version, effective dates, channels | Source of truth for what was published |
| Postgres chunks | Child text, parent text, offsets, ACL columns | Filters and parent expansion stay transactional |
| pgvector | Child embeddings, HNSW, model version | Dense nearest neighbor next to the metadata |
| OpenSearch | BM25 on the same chunk ids, unstemmed RRNs, UTRs, IFSCs | Exact match for payment identifiers |
| Graph tables | Account, card, payment, payee, channel, procedure, clause edges | Connections similarity search cannot represent |
| Core banking and payment switch | Balances, postings, settlement flags | Systems of record. The index does not copy them into vectors |
| Retrieval log | Raw query, rewrite, filters, ranks, claims, verdicts | The eval set and every production trace |
| Redis | Embeddings for repeated public queries | Not for personalized payment status |

Stack you can name if asked: a Python FastAPI or Node orchestrator, one strong model for the draft, a smaller model for rewriting and the entailment check, Postgres with pgvector, OpenSearch, Redis, and a queue that rechunks and re-embeds when a procedure is published. Traces go to OpenTelemetry, LangSmith, or Phoenix. Fine-tune, if you do it, for format and tool use. Amounts, timelines, and eligibility stay in the index and in the payment tools.

## Claim check

| Claim | Verdict | Why |
| --- | --- | --- |
| RRN 628418492012 is eligible for an IMPS credit-not-received trace | Supported | Eligibility clause in `imps-cnr-v4`, payment tool shows debit and open credit flag, fraud score low |
| Principal ₹25,000 comes back on T+1 if settlement confirms failure | Supported | Timeline sentence in the same parent |
| Interest is not part of the standard trace | Supported | Exclusion sentence in that parent |
| Duplicate annual fee ₹499 under FEE-8831 refunds to the savings account after agent confirm | Supported | `card-fee-dup-v2` plus the fee tool showing no second card |
| Instant refund tonight, with interest | Rejected | Timeline and exclusion contradict "instant" and "with interest" |
| Landlord's bank charges will be reversed too | Rejected | No span mentions another bank's charges |

## Latency budget for one issue

| Hop | Budget | Notes |
| --- | --- | --- |
| Rewrite / decompose | 400 ms | Skipped when the utterance is already one clean question |
| Account + payment + fee read | 80 ms | Parallel, and they set the filter and the rail |
| Hybrid search | 80 ms | Both indexes, same predicate |
| Rerank top 50 | 150 ms | Cross-encoder on child text |
| Parent expand + compress | 20 ms | Rules pin timeline, amount, exclusion, destination |
| Generate | 1.2 s | Structured claims plus the reply |
| Faithfulness | 400 ms | Fail closed on amounts and dates |

Illustrative p95 near 2.5 seconds for the common path, under 8 seconds when the agent loop uses all three retrieval rounds. These are budgets you state, then measure.

## Failures worth telling

1. Pure vector search missed RRN `628418492012` until BM25 and the payment tool were added. The model then described a generic IMPS failure and invented a same-day reversal.
2. A 2024 procedure that said "reversal within three working days" outranked `imps-cnr-v4` until the effective-date filter used the transaction timestamp.
3. The model promised interest because the "not automatic" sentence lived in the parent the child retriever had not expanded. Small-to-big plus the faithfulness guard closed it.
4. An NRI inward-remittance article was eligible for a resident savings chat until segment became a hard filter. The sentences looked similar: money arrived, money did not arrive.
5. A mobile-app session-timeout article outranked the IMPS procedure because the customer said "the app." Channel on the payment, not only channel of the chat, had to be a filter field.
6. The agent loop searched "be more helpful to the customer" until the time budget. The grader became a checklist of clause types — eligibility, timeline, amount, exclusion — and a hard stop at three rounds.

## Privacy and PCI

Resolved contacts are redacted before chunking. Account numbers are stored as a suffix in the index only when a procedure example needs one, and real customer suffixes never enter the embedding text. Full PAN, Aadhaar, card numbers, CVV, MPIN, internet-banking passwords, and OTPs never enter the embedding store, the graph, or the prompt. Card data in a tool payload is last4 plus a card token. The raw contact stays in the case system, which has its own access control and retention. An embedding of a secret is still a secret if the text is stored beside it. Traces that include a prompt are treated as customer data.

The customer bot may quote a published article and a payment status for the authenticated account. It may not quote agent-only steps, fraud-hold criteria, or another account's posting.

## Ninety seconds

"I designed a customer query resolution system for mobile banking and internet banking. The hard part was citing the right procedure version for the rail and the channel, so I treated the language model as the last step. Procedures are chunked by clause into children and parents, embedded with a pinned multilingual model, and indexed in pgvector and in BM25. On a contact I load the account, the payment, and the fee postings first, rewrite the chat into standalone queries, and split a trace request from a fee dispute. Both indexes use the same filter for segment, product, channel, visibility, and effective date, and reciprocal rank fusion merges them. A cross-encoder keeps the best children, I expand those to parent sections so timelines and exclusions survive, and I compress extractively. The draft is a set of cited claims. Anything about an amount or a date that the spans do not entail is regenerated or dropped. Traces and fee refunds are commands a person confirms. I evaluate context recall, context precision, and faithfulness on contacts labeled by senior agents. The quality moves I would defend came from hybrid search, metadata, and parent chunks."

## If they interrupt

**Why retrieve at all, instead of putting the payments manual in the prompt or fine-tuning?** Procedures change, manuals do not fit a context window, and a fine-tune does not cite the clause or the effective date. Retrieval keeps the answer on the version in force for that transaction and gives the agent a span to check.

**What chunk size?** Start from document structure. For leftover prose, try 256–512 tokens with modest overlap, then compare context recall on labeled contacts. Report the measurement.

**Bi-encoder versus cross-encoder?** The bi-encoder embeds each side alone, so procedure vectors are precomputed and search is a nearest-neighbor lookup. The cross-encoder scores a query-chunk pair jointly and rescores a shortlist. Retrieve with the first, keep the best with the second.

**Walk through reciprocal rank fusion.** Rank \(r\) contributes \(1/(60+r)\) from that list. Sum and sort. No score normalization. A chunk in both lists floats upward. Filter inside each list before you fuse.

**The bot promised an instant refund with interest. Where did the design fail?** Either the timeline and the no-interest sentence never arrived (recall, small-to-big, or a filter), or they arrived and the generator ignored them (faithfulness). Read the trace: filter, rail, fused ranks, parent expansion, cited spans, claim verdicts.

**How do you handle "and the extra money?"** Query rewriting, using the fee tool. Two ₹499 postings and the words "card fee twice" become a standalone query for `FEE-8831`, not a second search for the IMPS amount.

**When do you skip HyDE and the agent loop?** Skip HyDE for RRN- and UTR-heavy queries. Skip the loop when the first graded retrieval already covers eligibility, timeline, amount, and exclusions for a single intent. Most "what is my limit" questions stay on the single-pass path.

**Faithfulness versus context recall?** Recall asks whether the gold facts were retrieved. It needs labels. Faithfulness asks whether claims in this answer are entailed by the retrieved text. It does not need a gold answer. You want both.

**Where does Command Query Responsibility Segregation show up?** The product is the Customer Query Resolution System. Architecturally, reads are retrieval plus account, payment, and fee lookups. Writes are the trace and the fee refund, executed after a person confirms, with citation ids stored on the case.

**A procedure was updated this morning. What about an open case?** New chats filter to the version in force now. An open dispute stores policy-as-of as the transaction timestamp and keeps retrieving the version that applied then, so the file matches what the agent was allowed to say.
