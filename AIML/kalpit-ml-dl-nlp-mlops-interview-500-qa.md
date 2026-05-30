# Kalpit Sharma — 500+ ML / DL / NLP / MLOps Interview Q&A

> **Profile:** AVP HDFC Bank · 13+ yrs · AI Skin (agents, MCP, RAG) · Golang + Python · M.Tech AI/ML & DE IIT Jodhpur · Banking + platform scale
>
> **Use with:** [Personalized guide](./kalpit-sharma-interview-guide.md) · [GenAI prep](./agentic-genai-engineer-interview-prep.md) · [Coding practice](./agentic-genai-engineer-coding-practice.md)

Questions reflect **2025–2026 interview market**: production RAG/agents, MLOps, evals, regulated enterprise, GCP/Azure, cost-aware LLM systems.

**Total Q&A pairs: 783**

---

## How to study

1. **Week 1–2:** ML Fundamentals + Deep Learning (sections 1–2)
2. **Week 3:** NLP + LLM/GenAI (sections 3–4)
3. **Week 4:** MLOps + Data Engineering (sections 5–6)
4. **Daily:** 30 random questions — answer aloud without reading
5. **Banking roles:** Extra focus section 7

---

## Machine Learning Fundamentals

### Q1. What is the bias-variance tradeoff?

**A:** Bias is error from overly simple models; variance is error from sensitivity to training data. High bias underfits; high variance overfits. Goal: minimize total error via model complexity, regularization, and more data.

### Q2. Explain precision vs recall.

**A:** Precision = TP/(TP+FP) — how many predicted positives are correct. Recall = TP/(TP+FN) — how many actual positives you find. Use precision when false positives are costly (spam); recall when false negatives are costly (fraud).

### Q3. What is cross-validation and why use it?

**A:** Split data into k folds; train on k-1, validate on 1; rotate. Reduces variance in performance estimates vs single holdout. Use stratified k-fold for classification imbalance.

### Q4. L1 vs L2 regularization?

**A:** L1 (Lasso) adds |w| penalty → sparse features. L2 (Ridge) adds w² penalty → smaller weights, multicollinearity help. Elastic Net combines both.

### Q5. What causes data leakage?

**A:** Using future or target-derived information in training: target encoding on full data, scaling before split, duplicate near-duplicates across train/test, leaky features.

### Q6. How do you handle class imbalance?

**A:** Class weights, resampling (SMOTE cautiously), threshold tuning, proper metrics (PR-AUC, F1), stratified splits, cost-sensitive learning.

### Q7. ROC-AUC vs PR-AUC?

**A:** ROC plots TPR vs FPR; can be optimistic with imbalance. PR-AUC plots precision vs recall; often better for rare positive class.

### Q8. What is gradient descent?

**A:** Iterative optimization: update parameters opposite to loss gradient. Variants: SGD, mini-batch, Adam (adaptive learning rates).

### Q9. Batch norm purpose?

**A:** Normalize layer inputs per mini-batch; stabilizes training, allows higher LR, mild regularization. At inference use running statistics.

### Q10. Dropout?

**A:** Randomly zero neurons during training; prevents co-adaptation. Scale activations at inference. Typical p=0.2–0.5.

### Q11. Random forest vs gradient boosting?

**A:** RF: bagged trees, parallel, robust defaults. GBM: sequential trees correct residuals; often higher accuracy but more tuning and overfit risk.

### Q12. Feature importance in tree models?

**A:** Mean decrease in impurity or permutation importance. Check stability across folds; don't confuse correlation with causation.

### Q13. What is calibration?

**A:** Predicted probabilities match observed frequencies. Use Platt scaling or isotonic regression post-model for decision thresholds.

### Q14. MLE vs MAP?

**A:** MLE maximizes likelihood. MAP adds prior → Bayesian regularization. MAP helps with small data.

### Q15. Type I vs Type II error?

**A:** Type I: false positive. Type II: false negative. In banking fraud, FN (missed fraud) often costlier than FP.

### Q16. Central Limit Theorem relevance?

**A:** Sample means approximate normal distribution for large n — underlies many statistical tests and confidence intervals.

### Q17. When is linear regression inappropriate?

**A:** Strong nonlinear relationships, heavy outliers without robust loss, categorical outcomes (use logistic), heteroscedasticity without correction.

### Q18. Explain logistic regression.

**A:** Models log-odds as linear in features; sigmoid maps to probability. Interpret coefficients as log-odds changes; use for baseline classification.

### Q19. What is multicollinearity?

**A:** Correlated features inflate variance of coefficients. Detect via VIF; fix with removal, PCA, or regularization.

### Q20. Holdout vs validation vs test?

**A:** Train: fit parameters. Validation: tune hyperparameters. Test: final unbiased estimate once. Never tune on test.

### Q21. What is a confusion matrix?

**A:** Table of TP, FP, TN, FN. Foundation for metrics; inspect per-class errors in multi-class problems.

### Q22. One-hot vs label encoding?

**A:** One-hot for nominal categories without order. Label encoding only when ordinality matters or for tree models that handle categories natively.

### Q23. Missing data strategies?

**A:** MCAR/MAR/MNAR analysis; impute (mean/median/KNN), model-based, or missing indicators; domain rules in banking often prefer explicit 'unknown' category.

### Q24. Outlier handling?

**A:** Investigate first — fraud or data bug? Winsorize, robust scalers, tree models, or separate anomaly models.

### Q25. What is feature scaling and when needed?

**A:** Standardization/zero-mean unit variance needed for distance-based models, neural nets, regularized linear models. Trees often don't need it.

### Q26. Curse of dimensionality?

**A:** Data sparsity grows exponentially with dimensions; distance metrics become less meaningful; need more data or dimensionality reduction.

### Q27. PCA use case?

**A:** Linear dimensionality reduction; decorrelate features; visualization; speed. Limitation: linear only; interpretability loss.

### Q28. Hypothesis testing p-value?

**A:** Probability of observing data at least as extreme if null true. Misused as 'effect size'; always report effect size and CI.

### Q29. Confidence interval interpretation?

**A:** 95% CI means procedure captures true parameter 95% of repeated samples — not '95% probability parameter in interval' for single interval.

### Q30. Bagging vs boosting?

**A:** Bagging reduces variance averaging independent models (RF). Boosting reduces bias sequentially weighting hard examples (XGBoost, LightGBM).

### Q31. Learning rate role?

**A:** Step size in gradient updates. Too high diverges; too slow trains forever. Schedules: step decay, cosine, warmup.

### Q32. Early stopping?

**A:** Stop training when validation metric worsens; prevents overfitting; saves compute.

### Q33. What is transfer learning?

**A:** Reuse pretrained model weights; fine-tune on target task with less data. Standard in NLP/CV since transformers.

### Q34. Ensemble methods benefit?

**A:** Combine diverse models to reduce variance and improve robustness; cost: latency and complexity.

### Q35. Model selection criteria?

**A:** Business metric first, then statistical; penalize complexity (AIC/BIC) or use nested CV; consider deployment constraints.

### Q36. What is SHAP?

**A:** Shapley-based feature attribution for individual predictions; unified local interpretability; watch correlated features.

### Q37. Correlation vs causation?

**A:** Correlation measures association; causation requires experimental design or causal inference (DAGs, IV, RCT).

### Q38. Stationarity in time series?

**A:** Statistical properties constant over time. Many models assume it; use differencing, transforms, or specialized models if non-stationary.

### Q39. ARIMA when to use?

**A:** Univariate classical forecasting; needs stationarity; baseline for simple series before deep learning.

### Q40. Cold start problem?

**A:** No history for new users/items; use content features, popularity defaults, or hybrid models.

### Q41. Exploration vs exploitation?

**A:** Multi-armed bandits balance trying new actions vs best known; used in recommendations and A/B testing.

### Q42. What is A/B testing for ML?

**A:** Randomized experiment comparing model variants; need power analysis, guard metrics, and duration to account for seasonality.

### Q43. Simpson's paradox?

**A:** Aggregate trend reverses when stratified — always check segments (e.g., customer cohorts).

### Q44. Survivorship bias in data?

**A:** Only observing entities that 'survived' — e.g., active accounts only; skews churn and risk models.

### Q45. Label noise impact?

**A:** Degrades boundary learning; use robust loss, cleaning, semi-supervised techniques, or higher-quality labeling investment.

### Q46. Active learning?

**A:** Model selects samples for human labeling to maximize information per label cost.

### Q47. Semi-supervised learning?

**A:** Train with small labeled + large unlabeled data — pseudo-labeling, consistency regularization.

### Q48. Self-supervised learning?

**A:**  Pretext tasks from unlabeled data (mask prediction, contrastive) — foundation of modern LLM pretraining.

### Q49. Federated learning?

**A:** Train across decentralized data without centralizing raw data — privacy-sensitive banking use cases with constraints.

### Q50. Concept drift?

**A:** P(X,y) changes over time; monitor metrics, retrain triggers, champion-challenger.

### Q51. Covariate shift?

**A:** P(X) changes but P(y|X) stable; importance weighting or retrain features.

### Q52. Prior probability shift?

**A:** P(y) changes; recalibrate thresholds.

### Q53. What is a baseline model?

**A:** Simple heuristic (majority class, mean prediction) or logistic regression — beat this before claiming ML value.

### Q54. How to estimate sample size needs?

**A:** Power analysis for A/B tests; learning curves for ML; rule of thumb insufficient — simulate.

### Q55. Nested cross-validation?

**A:** Outer loop for performance estimate, inner for hyperparameter tuning — unbiased but expensive.

### Q56. Why stratify splits?

**A:** Preserve class proportions in train/val/test — critical for imbalanced banking fraud.

### Q57. Hashing trick?

**A:** Map high-cardinality categories to fixed buckets — memory efficient streaming; collision tradeoff.

### Q58. Target encoding pitfalls?

**A:** Leakage if computed on full dataset — use CV-encoded means or regularized target encoding.

### Q59. WoE in credit risk?

**A:** Weight of Evidence transforms categorical bins for logistic scorecards — interpretable, regulatory familiarity.

### Q60. KS statistic in credit?

**A:** Max separation between cumulative distributions of good/bad — common in scorecard validation.

### Q61. Gini vs AUC?

**A:** Gini = 2*AUC-1 for binary classifiers; both rank-based discrimination metrics.

### Q62. Population stability index (PSI)?

**A:** Measures score distribution shift between train and deploy — monitoring standard in banking.

### Q63. Champion-challenger deployment?

**A:** Production champion model; challenger receives shadow traffic for comparison before promotion.

### Q64. What is model risk management?

**A:** Framework (SR 11-7 style): development standards, validation, governance, documentation for models in banks.

### Q65. Fairness metrics?

**A:** Demographic parity, equalized odds, calibration by group — choose per legal/ethics context; never optimize accuracy alone.

### Q66. Explainability regulatory need?

**A:** Credit and some AI decisions require adverse action reasons — use interpretable models or post-hoc explanations with caveats.

### Q67. Sigmoid function?

**A:** σ(x)=1/(1+e^-x); outputs (0,1) probability; saturates → vanishing grad deep.

### Q68. Softmax?

**A:** Normalize logits to simplex — multi-class probabilities.

### Q69. Entropy in ML?

**A:** Measure uncertainty; cross-entropy loss; decision trees use gain.

### Q70. Information gain?

**A:** Split reduces entropy — tree building criterion.

### Q71. Gini impurity?

**A:** Alternative tree split metric — faster compute than entropy.

### Q72. K-means?

**A:** Clustering minimize within-cluster variance; choose k via elbow/silhouette.

### Q73. DBSCAN?

**A:** Density clustering arbitrary shapes; noise points.

### Q74. Hierarchical clustering?

**A:** Dendrogram; no preset k; costly large n.

### Q75. PCA whitening?

**A:** Decorrelate and scale variances — some neural preprocess.

### Q76. t-SNE vs UMAP?

**A:** Nonlinear dim reduction visualization; UMAP preserves more global structure.

### Q77. Isolation forest?

**A:** Anomaly detection random partitions — short path length anomalies.

### Q78. One-class SVM?

**A:** Boundary around normal class — anomaly detection.

### Q79. Local Outlier Factor?

**A:** Density-based local anomaly score.

### Q80. SMOTE?

**A:** Synthetic oversample minorities — watch overfitting near boundary.

### Q81. Grid search?

**A:** Exhaustive hyperparameter — expensive.

### Q82. Random search?

**A:** Often better than grid high dims — Bergstra paper.

### Q83. Bayesian optimization?

**A:** Model surrogate for expensive eval — Optuna.

### Q84. Learning curves?

**A:** Plot train/val metric vs data size — diagnose bias/variance.

### Q85. Calibration plot?

**A:** Reliability diagram predicted vs observed.

### Q86. Q-Q plot?

**A:** Check normality residuals.

### Q87. Heteroscedasticity?

**A:** Non-constant variance — transform or robust regression.

### Q88. Autocorrelation time series?

**A:** ARIMA needs; LSTM/transformer alternative.

### Q89. Seasonality?

**A:** SARIMA seasonal component; Fourier features.

### Q90. Prophet?

**A:** Facebook forecasting additive model — business series.

### Q91. Causal impact?

**A:** Bayesian structural time series — measure intervention.

### Q92. Difference-in-differences?

**A:** Causal panel method — policy evaluation.

### Q93. A/B sequential testing?

**A:** Peek inflates false positive — use sequential methods or fixed horizon.

### Q94. Multi-armed bandit epsilon-greedy?

**A:** Explore epsilon; exploit best arm.

### Q95. Thompson sampling?

**A:** Bayesian bandit — sample from posterior.

### Q96. Contextual bandit?

**A:** Features per arm — personalization.

### Q97. Matrix factorization?

**A:** Collaborative filtering latent factors.

### Q98. Neural collaborative filtering?

**A:** Deep learning on user-item interactions.

### Q99. Wide and Deep?

**A:** Google memorization + generalization — recommender.

### Q100. Click-through rate prediction?

**A:** Logistic regression baseline; deep crosses — ads/banking offers.

### Q101. Lift chart?

**A:** Marketing model targets top deciles — cumulative lift.

### Q102. Gains chart?

**A:** Similar — cumulative capture rate.

### Q103. Cap curve?

**A:** Cumulative positives vs population — credit marketing.

### Q104. Hazard model?

**A:** Survival analysis time-to-event — churn.

### Q105. Cox proportional hazards?

**A:** Semi-parametric survival — interpret coefficients.

### Q106. Quantile regression?

**A:** Predict conditional quantiles — risk ranges.

### Q107. Huber loss?

**A:** Robust regression less sensitive outliers.

### Q108. Hinge loss?

**A:** SVM classification margin maximization.

### Q109. Support vectors?

**A:** Points on margin boundary — kernel trick nonlinear.

### Q110. Kernel trick?

**A:** Implicit high-dim space — RBF polynomial kernels.

### Q111. Naive Bayes?

**A:** Feature independence assumption — fast text baseline.

### Q112. LDA generative?

**A:** Not topic LDA — Linear Discriminant Analysis classification.

### Q113. QDA?

**A:** Quadratic discriminant — different cov per class.

### Q114. Ensemble stacking?

**A:** Meta-learner combines base models.

### Q115. Blending?

**A:** Holdout blend predictions — simpler stacking.

### Q116. OOF predictions?

**A:** Out-of-fold for stacking avoid leakage.

### Q117. Time series cross-validation?

**A:** Rolling origin — respect temporal order.

### Q118. Grouped CV?

**A:** Keep group entities same fold — customer level.

### Q119. Leakage from customer duplicates?

**A:** Same customer train and test — inflate metrics.

### Q120. Parameter vs hyperparameter?

**A:** Learned weights vs set before training (LR, depth).

### Q121. Epoch vs iteration?

**A:** Full pass data vs one batch update.

### Q122. Mini-batch size tradeoff?

**A:** Large: stable grad, memory. Small: noise regularizes.

### Q123. Weight tying?

**A:** Share parameters — input output embeddings reduce params.

### Q124. Attention is all you need paper?

**A:** 2017 Vaswani — transformer foundation.

### Q125. BERT base vs large?

**A:** Layers/hidden size — accuracy vs cost.

### Q126. GPT-3 few-shot?

**A:** In-context learning emergence at scale.

---

## Deep Learning

### Q127. ReLU vs sigmoid?

**A:** ReLU avoids vanishing gradient, faster compute. Sigmoid saturates — mainly output gates in LSTM or binary output.

### Q128. Vanishing/exploding gradients?

**A:** Deep nets multiply gradients; vanishing stops learning early layers. Fixes: ReLU, residual connections, LayerNorm, gradient clipping, proper init.

### Q129. What are residual connections?

**A:** y = F(x) + x — skip connections ease gradient flow; enabled very deep networks (ResNet).

### Q130. CNN vs RNN vs Transformer?

**A:** CNN: local patterns, images. RNN: sequences (largely superseded). Transformer: self-attention, parallelizable, SOTA NLP/Vision.

### Q131. Kernel size intuition?

**A:** Larger receptive field per layer; 3x3 stacks common; dilated convs expand field without more params.

### Q132. Pooling purpose?

**A:** Downsample spatial dims, translation invariance, reduce compute. Max vs average pooling.

### Q133. Transfer learning in CV?

**A:** ImageNet pretrained backbones + fine-tune head; freeze early layers with small data.

### Q134. Data augmentation for images?

**A:** Flip, crop, color jitter — improves generalization; don't augment test.

### Q135. What is attention mechanism?

**A:** Weighted sum of values where weights depend on query-key similarity — focuses on relevant inputs.

### Q136. Self-attention complexity?

**A:** O(n²) in sequence length — bottleneck for long contexts; mitigations: sparse attention, sliding window, linear attention.

### Q137. Multi-head attention?

**A:** Parallel attention heads capture different relationship types; concat + project.

### Q138. Positional encoding why?

**A:** Attention is permutation-invariant; add position info via sinusoidal or learned embeddings.

### Q139. LayerNorm vs BatchNorm?

**A:** LayerNorm normalizes across features per token — standard in transformers. BatchNorm across batch — common in CNNs.

### Q140. Adam optimizer?

**A:** Adaptive LR per parameter using momentum and second moments; default for many DL tasks; watch weight decay decoupling.

### Q141. Weight decay?

**A:** L2 penalty on weights; in AdamW decoupled from gradient update — improves generalization.

### Q142. Learning rate warmup?

**A:** Gradually increase LR early training — stabilizes transformer training.

### Q143. Mixed precision training?

**A:** FP16/BF16 compute with FP32 master weights — faster on GPUs; loss scaling prevents underflow.

### Q144. What is CUDA in your stack?

**A:** NVIDIA parallel computing platform; PyTorch/TensorFlow use GPU kernels — you listed CUDA experience with TF/PyTorch.

### Q145. GPU memory optimization?

**A:** Gradient checkpointing, smaller batch, mixed precision, gradient accumulation, model parallelism for huge models.

### Q146. What is a transformer block?

**A:** Multi-head self-attention + FFN + residuals + LayerNorm — repeated L times.

### Q147. Encoder-only vs decoder-only?

**A:** Encoder (BERT): bidirectional context — understanding. Decoder (GPT): causal — generation. Encoder-decoder (T5): seq2seq.

### Q148. Masked language modeling?

**A:** BERT pretraining predicts masked tokens — bidirectional context learning.

### Q149. Causal language modeling?

**A:** GPT predicts next token — autoregressive generation.

### Q150. Teacher forcing?

**A:** During RNN training feed ground truth previous token — exposure bias at inference.

### Q151. Seq2seq with attention?

**A:** Encoder summarizes input; decoder attends over encoder states — pre-transformer MT standard.

### Q152. BLEU score?

**A:** N-gram overlap MT metric — crude; still used; prefer human eval + chrF for modern systems.

### Q153. Perplexity?

**A:** exp(cross-entropy) per token — lower better; intrinsic LM metric; not always aligned with downstream task.

### Q154. Cross-entropy loss?

**A:** Negative log likelihood of true class/token — standard classification and LM objective.

### Q155. Focal loss?

**A:** Down-weights easy examples — helps extreme imbalance object detection.

### Q156. Contrastive learning?

**A:** Pull similar embeddings together, push dissimilar apart — SimCLR, CLIP foundations.

### Q157. CLIP?

**A:** Image-text contrastive pretraining — zero-shot image classification via prompts.

### Q158. Vision Transformer (ViT)?

**A:** Patchify image → token sequence → transformer — needs large data or pretrain.

### Q159. Object detection families?

**A:** Two-stage (Faster R-CNN) vs one-stage (YOLO) — speed/accuracy tradeoff.

### Q160. Segmentation U-Net?

**A:** Encoder-decoder with skip connections for pixel-wise prediction — medical imaging classic.

### Q161. GAN training challenges?

**A:** Mode collapse, instability — careful architecture (DCGAN), WGAN, or use diffusion instead.

### Q162. Diffusion models intuition?

**A:** Learn to reverse noise process — stable high-quality generation; DALL-E 3, Stable Diffusion lineage.

### Q163. LoRA fine-tuning?

**A:** Low-rank adapters on attention weights — train few params, efficient GPU memory.

### Q164. QLoRA?

**A:** Quantized base weights + LoRA — fine-tune large models on consumer GPUs.

### Q165. Full fine-tune vs adapter?

**A:** Full: max flexibility, costly. Adapter/LoRA: cheaper, multiple tasks swappable — enterprise norm.

### Q166. Knowledge distillation?

**A:** Small student mimics large teacher soft outputs — deploy cheaper models.

### Q167. Quantization INT8?

**A:** Reduce weight precision for inference speed — post-training or quantization-aware training.

### Q168. ONNX / TorchScript?

**A:** Export formats for production inference outside training framework.

### Q169. Triton inference server?

**A:** NVIDIA multi-framework serving — dynamic batching, model ensemble.

### Q170. Torch compile / graph optimization?

**A:** Fuse ops reduce Python overhead — production latency wins.

### Q171. Overfitting in deep nets?

**A:** More data, augmentation, dropout, early stopping, regularization, simpler architecture.

### Q172. Underfitting signs?

**A:** High train and val error — increase capacity, train longer, better features.

### Q173. Dead ReLU neurons?

**A:** Neurons always zero — lower LR, Leaky ReLU, proper init.

### Q174. He vs Xavier init?

**A:** He for ReLU (variance 2/fan_in); Xavier for tanh/sigmoid — maintains activation variance.

### Q175. Gradient clipping?

**A:** Cap gradient norm — prevents explosion especially RNNs and large transformers.

### Q176. Spectral normalization?

**A:** Stabilize GAN discriminator Lipschitz constraint.

### Q177. Autoencoder use?

**A:** Unsupervised compression; anomaly detection if reconstruction error high on outliers.

### Q178. VAE?

**A:** Probabilistic encoder-decoder with KL regularization — generative, smooth latent space.

### Q179. Sequence padding and packing?

**A:** Handle variable lengths efficiently in PyTorch packed sequences — avoid padding compute waste.

### Q180. CTC loss?

**A:** Alignment-free speech recognition training — maps audio to text without frame alignment.

### Q181. WER metric?

**A:** Word Error Rate for ASR — (S+D+I)/N.

### Q182. Image normalization?

**A:** Per-channel mean/std (ImageNet norms) — match pretrain stats when transfer learning.

### Q183. Handling imbalanced detection?

**A:** Focal loss, oversampling hard negatives, anchor matching tweaks.

### Q184. Multi-task learning?

**A:** Shared backbone predicts multiple heads — regularization when tasks related.

### Q185. Neural architecture search?

**A:** Automated architecture discovery — costly; mostly research or large orgs.

### Q186. Federated learning challenges?

**A:** Non-IID data, communication cost, security aggregation.

### Q187. Federated averaging?

**A:** Clients train locally; server averages weights — FedAvg baseline.

### Q188. Differential privacy in training?

**A:** Add noise to gradients — privacy guarantee with utility tradeoff.

### Q189. Homomorphic encryption inference?

**A:** Compute on encrypted data — extreme cost; niche banking research.

### Q190. Edge deployment constraints?

**A:** Model size, latency, offline — distill, quantize, mobile-optimized architectures.

### Q191. TPU vs GPU?

**A:** TPU optimized for large matrix ops on GCP; GPU more general; pick per framework and cloud.

### Q192. XLA?

**A:** Accelerated linear algebra compiler — TensorFlow/JAX optimization.

### Q193. JAX vs PyTorch?

**A:** JAX: functional, compile, research. PyTorch: imperative, industry default for DL production training.

### Q194. TensorFlow 2.x mode?

**A:** Eager + tf.function graphs; Keras API; still seen in enterprise legacy.

### Q195. Keras Sequential vs Functional API?

**A:** Functional supports multi-input/output, shared layers — needed for complex nets.

### Q196. Custom training loop when?

**A:** Need fine control: GANs, RL, gradient accumulation, multi-loss — PyTorch standard pattern.

### Q197. torch.nn.Module lifecycle?

**A:** forward() defines graph; train()/eval() toggles dropout/batchnorm; state_dict for checkpoints.

### Q198. DistributedDataParallel?

**A:** Multi-GPU training replicate model, sync gradients — scale training.

### Q199. Scaling laws?

**A:** Loss power law vs compute/data/params — guides training budget.

### Q200. Chinchilla?

**A:** Optimal tokens per param — train smaller longer.

### Q201. Mixture of Experts?

**A:** Sparse activate subset experts — reduce compute per token.

### Q202. MoE routing?

**A:** Gating network picks experts — load balancing challenge.

### Q203. Flash Attention?

**A:** IO-aware exact attention faster — standard training 2024+.

### Q204. Rotary embeddings RoPE?

**A:** Relative position encoding GPT-NeoX Llama.

### Q205. ALiBi?

**A:** Attention linear biases — extrapolate length.

### Q206. Grouped-query attention?

**A:** Share KV heads — faster inference Llama.

### Q207. KV cache inference?

**A:** Store keys values autoregressive — memory grows sequence.

### Q208. Speculative decoding?

**A:** Draft model proposes; target verifies — faster inference.

### Q209. Continuous batching vLLM?

**A:** Dynamic batch requests — serving throughput.

### Q210. PagedAttention?

**A:** Non-contiguous KV memory — vLLM efficiency.

### Q211. LoRA rank r?

**A:** Low rank matrices — r trades capacity vs params.

### Q212. Inference batching padding waste?

**A:** Variable length sequences — packing mitigates.

### Q213. Torch compile?

**A:** PyTorch 2 graph optimization.

### Q214. CUDA out of memory fix?

**A:** Smaller batch, grad accum, checkpoint, clear cache.

### Q215. Deterministic training?

**A:** Set seeds; cudnn deterministic — reproducibility debug.

### Q216. Mixed precision BF16 vs FP16?

**A:** BF16 same exponent range FP32 — A100+ friendly.

### Q217. Loss NaN debugging?

**A:** LR too high, bad init, explode grad — clip reduce LR.

### Q218. Mode collapse GAN?

**A:** Generator limited diversity — Wasserstein fixes partial.

### Q219. Inception score?

**A:** GAN eval quality diversity — outdated somewhat.

### Q220. FID score?

**A:** Fréchet distance feature stats — image generation eval.

### Q221. Perceptual loss?

**A:** Deep features similarity — super resolution.

### Q222. Style transfer?

**A:** Content + style loss different layers.

### Q223. Transfer learning head freeze?

**A:** Freeze backbone train classifier — small data.

### Q224. Discriminative fine-tuning ULMFiT?

**A:** Different LR per layer — NLP classic.

### Q225. ULMFiT?

**A:** Universal language model fine-tuning pre-transformer SOTA approach.

---

## NLP & Text

### Q226. What is tokenization?

**A:** Split text into units (words, subwords). BPE/WordPiece/SentencePiece handle OOV via subword units — standard for LLMs.

### Q227. BPE algorithm?

**A:** Iteratively merge frequent character pairs — balances vocab size and coverage.

### Q228. Word2Vec CBOW vs Skip-gram?

**A:** Predict context from word (CBOW) or word from context (Skip-gram). Skip-gram better rare words.

### Q229. GloVe?

**A:** Global co-occurrence matrix factorization embeddings — static vectors.

### Q230. Static vs contextual embeddings?

**A:** Static (Word2Vec) one vector per word. Contextual (BERT) same word different vectors by sentence — essential for polysemy.

### Q231. BERT architecture?

**A:** Transformer encoder, MLM pretraining, [CLS] for classification, token embeddings for NER.

### Q232. BERT fine-tuning best practices?

**A:** Small LR (2e-5), few epochs, class weights, max length tuning, discriminative LR for layers.

### Q233. GPT vs BERT?

**A:** GPT: decoder causal LM — generate. BERT: encoder — understand. Different pretraining objectives.

### Q234. T5 framework?

**A:** Text-to-text — all NLP as string generation — unified fine-tuning.

### Q235. Named Entity Recognition approaches?

**A:** BIO tagging with CRF or transformer token classification; domain gazetteers in banking for PII/entities.

### Q236. Part-of-speech tagging?

**A:** Sequence labeling; less standalone now — subsumed by LLMs.

### Q237. Dependency parsing?

**A:** Grammatical structure; used in advanced NLP pipelines; LLMs implicit.

### Q238. Text classification baseline?

**A:** TF-IDF + logistic regression or small fine-tuned BERT — always benchmark.

### Q239. Sentiment analysis challenges?

**A:** Sarcasm, domain shift, aspect-based sentiment, multilingual.

### Q240. Topic modeling LDA?

**A:** Unsupervised document topics — interpretable; LLM clustering alternative.

### Q241. Information retrieval vs RAG?

**A:** IR returns documents; RAG conditions generation on retrieved docs — reduces hallucination.

### Q242. BM25?

**A:** Sparse lexical retrieval — strong baseline; combine with dense in hybrid search.

### Q243. Dense retrieval?

**A:** Embed query and docs; cosine similarity — semantic match beyond keywords.

### Q244. Bi-encoder vs cross-encoder?

**A:** Bi-encoder: fast retrieval. Cross-encoder: rerank top-k with joint encoding — higher accuracy, slower.

### Q245. ColBERT?

**A:** Late interaction — token-level similarity — efficient reranking middle ground.

### Q246. Embedding model selection?

**A:** Benchmark on your domain; consider dimension, latency, multilingual, license.

### Q247. Semantic similarity metrics?

**A:** Cosine on embeddings; STS benchmarks; not sufficient alone for RAG quality.

### Q248. Text chunking strategies?

**A:** Fixed size, sentence, semantic, document structure-aware — critical RAG lever.

### Q249. Handling tables in RAG?

**A:** HTML/markdown tables, specialized parsers, row-level chunking, table-aware models.

### Q250. Multilingual NLP?

**A:** mBERT, XLM-R, or multilingual embeddings; evaluate per locale; banking India may need Hindi-English.

### Q251. Transliteration issues?

**A:** Normalize Unicode, handle code-mixing in Indian languages.

### Q252. Coreference resolution?

**A:** Link pronouns to entities — dialogue systems; LLMs partially handle.

### Q253. Summarization extractive vs abstractive?

**A:** Extractive: select sentences. Abstractive: generate — LLMs default abstractive with hallucination risk.

### Q254. ROUGE metric?

**A:** N-gram overlap summarization — reference-based; imperfect.

### Q255. Question answering types?

**A:** Extractive (span), generative, multi-hop — RAG enables generative with citations.

### Q256. Natural language inference?

**A:** Entailment/contradiction — evaluation and guardrail tasks.

### Q257. Prompt engineering for classification?

**A:** Instructions + examples; JSON output mode; calibrate with temperature 0 for consistency.

### Q258. Few-shot in-context learning?

**A:** Examples in prompt — no weight update; context length limits; quality sensitive to order.

### Q259. Chain-of-thought?

**A:** Ask model to reason stepwise — improves math/logic; costs tokens.

### Q260. Hallucination in NLP?

**A:** Fluent but false — mitigate RAG, abstain, grounding, evals.

### Q261. Entity linking?

**A:** Map mentions to knowledge base IDs — enrichment for financial KB.

### Q262. Relation extraction?

**A:** Triples from text — KYC, news monitoring use cases.

### Q263. Event extraction?

**A:** Who did what when — surveillance and news analytics.

### Q264. Intent detection?

**A:** Route user query to workflow — banking chatbots first stage.

### Q265. Slot filling?

**A:** Parameter extraction for structured actions — being replaced by tool calling.

### Q266. Dialogue state tracking?

**A:** Track conversation context — LLM memory simplifies but doesn't eliminate bugs.

### Q267. Toxicity detection?

**A:** Classifier or moderation API — required customer-facing.

### Q268. PII detection NER?

**A:** Regex + NER models — mask before logging or external LLM calls in banks.

### Q269. De-identification?

**A:** Remove/mask PII for model training compliance.

### Q270. Text normalization?

**A:** Lowercase, unicode NFKC, expand contractions — domain specific rules in finance.

### Q271. Spell correction?

**A:** Noisy user queries — edit distance or small models before retrieval.

### Q272. Query expansion?

**A:** Synonyms, HyDE (hypothetical doc embedding) — improve recall.

### Q273. HyDE?

**A:** LLM generates hypothetical answer, embed it for retrieval — improves dense search sometimes.

### Q274. Reranking pipeline?

**A:** Retrieve 50–100 → cross-encoder rerank to 5–10 → LLM — standard enterprise RAG.

### Q275. Context window limits?

**A:** Truncate, summarize history, or retrieve only relevant — long-context models expensive.

### Q276. Lost in the middle phenomenon?

**A:** LLMs ignore mid-context — put key info at start/end.

### Q277. Instruction tuning?

**A:** Fine-tune on instruction-response pairs — aligns model to follow prompts (FLAN, ChatGPT RLHF stage).

### Q278. RLHF overview?

**A:** Reward model from human preferences + PPO fine-tune — alignment; costly.

### Q279. DPO?

**A:** Direct Preference Optimization — simpler alignment without explicit reward model.

### Q280. Constitutional AI?

**A:** Model critiques/revises per principles — Anthropic alignment approach.

### Q281. Model cards?

**A:** Document intended use, limitations, evals — governance best practice.

### Q282. NLTK vs spaCy?

**A:** spaCy production pipelines; NLTK teaching/toolkit — less production.

### Q283. Hugging Face ecosystem?

**A:** Models, datasets, transformers library, inference endpoints — industry standard hub.

### Q284. transformers Trainer API?

**A:** High-level training loop — good starts; custom loops for advanced.

### Q285. PEFT library?

**A:** Parameter-efficient fine-tuning — LoRA adapters Hugging Face.

### Q286. Sentence Transformers?

**A:** Easy embedding models and training — RAG staple.

### Q287. LangChain role?

**A:** Orchestration glue — chains, agents, retrievers — evaluate complexity vs custom code.

### Q288. LlamaIndex role?

**A:** Data framework for RAG — connectors, indexing — pairs with enterprise data.

### Q289. Semantic Kernel?

**A:** Microsoft orchestration — plugins, planners — enterprise .NET/Python shops.

### Q290. spaCy NER custom training?

**A:** Annotate data, train pipeline component — domain entities.

### Q291. CRF layer on top?

**A:** Sequence constraints — improve NER consistency.

### Q292. Word sense disambiguation?

**A:** Context picks meaning — LLMs largely absorb.

### Q293. Semantic search evaluation?

**A:** nDCG, MRR, recall@k on labeled query-doc pairs.

### Q294. nDCG?

**A:** Normalized discounted cumulative gain — ranked retrieval quality.

### Q295. MRR?

**A:** Mean reciprocal rank of first relevant result.

### Q296. Human eval for NLP?

**A:** Likert scales, side-by-side, rubrics — gold standard for GenAI.

### Q297. Inter-annotator agreement?

**A:** Cohen's kappa — label quality for supervised NLP.

### Q298. Active learning for NLP?

**A:** Select uncertain samples for labeling — reduces annotation cost.

### Q299. Weak supervision?

**A:** Labeling functions aggregate noisy labels — Snorkel framework.

### Q300. Data labeling vendors?

**A:** Scale, internal annotators — banking often requires secure annotation rooms.

### Q301. How do you operationalize challenger policy?

**A:** Treat challenger policy as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q302. How do you operationalize shadow metric compare?

**A:** Treat shadow metric compare as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q303. How do you operationalize business KPI guardrail?

**A:** Treat business KPI guardrail as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q304. How do you operationalize revenue impact model?

**A:** Treat revenue impact model as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q305. How do you operationalize risk appetite threshold?

**A:** Treat risk appetite threshold as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q306. How do you operationalize model retirement?

**A:** Treat model retirement as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q307. How do you operationalize legacy model sunset?

**A:** Treat legacy model sunset as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q308. How do you operationalize dependency model upstream?

**A:** Treat dependency model upstream as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q309. How do you operationalize cascading failure isolate?

**A:** Treat cascading failure isolate as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q310. How do you operationalize bulkhead serving?

**A:** Treat bulkhead serving as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q311. How do you operationalize timeout per model?

**A:** Treat timeout per model as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q312. How do you operationalize fallback heuristic?

**A:** Treat fallback heuristic as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q313. How do you operationalize graceful degradation?

**A:** Treat graceful degradation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q314. How do you operationalize read-only mode AI?

**A:** Treat read-only mode AI as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q315. How do you operationalize kill switch feature flag?

**A:** Treat kill switch feature flag as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q316. How is stemming used in enterprise NLP today?

**A:** Stemming appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q317. How is lemmatization used in enterprise NLP today?

**A:** Lemmatization appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q318. How is stop words used in enterprise NLP today?

**A:** Stop Words appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q319. How is n-grams used in enterprise NLP today?

**A:** N-Grams appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q320. How is TF-IDF used in enterprise NLP today?

**A:** Tf-Idf appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q321. How is BM25 tuning used in enterprise NLP today?

**A:** Bm25 Tuning appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q322. How is query parsing used in enterprise NLP today?

**A:** Query Parsing appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q323. How is boolean retrieval used in enterprise NLP today?

**A:** Boolean Retrieval appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q324. How is faceted search used in enterprise NLP today?

**A:** Faceted Search appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q325. How is snippet generation used in enterprise NLP today?

**A:** Snippet Generation appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q326. How is passage retrieval used in enterprise NLP today?

**A:** Passage Retrieval appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q327. How is document scoring fusion used in enterprise NLP today?

**A:** Document Scoring Fusion appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q328. How is reciprocal rank fusion used in enterprise NLP today?

**A:** Reciprocal Rank Fusion appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q329. How is cross-lingual retrieval used in enterprise NLP today?

**A:** Cross-Lingual Retrieval appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q330. How is transliteration search used in enterprise NLP today?

**A:** Transliteration Search appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q331. How is fuzzy match used in enterprise NLP today?

**A:** Fuzzy Match appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q332. How is phonetic match used in enterprise NLP today?

**A:** Phonetic Match appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q333. How is abbreviation expansion used in enterprise NLP today?

**A:** Abbreviation Expansion appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q334. How is financial entity NER used in enterprise NLP today?

**A:** Financial Entity Ner appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q335. How is ticker resolution used in enterprise NLP today?

**A:** Ticker Resolution appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q336. How is ISIN mapping used in enterprise NLP today?

**A:** Isin Mapping appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q337. How is contract clause ID used in enterprise NLP today?

**A:** Contract Clause Id appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q338. How is legal clause similarity used in enterprise NLP today?

**A:** Legal Clause Similarity appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q339. How is table QA used in enterprise NLP today?

**A:** Table Qa appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q340. How is chart understanding used in enterprise NLP today?

**A:** Chart Understanding appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q341. How is OCR post-processing used in enterprise NLP today?

**A:** Ocr Post-Processing appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q342. How is layout LM used in enterprise NLP today?

**A:** Layout Lm appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q343. How is Donut document model used in enterprise NLP today?

**A:** Donut Document Model appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q344. How is DocLLM trend used in enterprise NLP today?

**A:** Docllm Trend appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q345. How is invoice field extract used in enterprise NLP today?

**A:** Invoice Field Extract appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q346. How is receipt parsing used in enterprise NLP today?

**A:** Receipt Parsing appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q347. How is KYC doc classify used in enterprise NLP today?

**A:** Kyc Doc Classify appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q348. How is spam detection NLP used in enterprise NLP today?

**A:** Spam Detection Nlp appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q349. How is intent hierarchy used in enterprise NLP today?

**A:** Intent Hierarchy appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q350. How is dialog act used in enterprise NLP today?

**A:** Dialog Act appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q351. How is coreference bank domain used in enterprise NLP today?

**A:** Coreference Bank Domain appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q352. How is summarization bullet used in enterprise NLP today?

**A:** Summarization Bullet appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q353. How is headline generation used in enterprise NLP today?

**A:** Headline Generation appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q354. How is email auto-draft used in enterprise NLP today?

**A:** Email Auto-Draft appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q355. How is tone adjustment used in enterprise NLP today?

**A:** Tone Adjustment appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q356. How is formal vs casual used in enterprise NLP today?

**A:** Formal Vs Casual appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q357. How is translation quality BLEU used in enterprise NLP today?

**A:** Translation Quality Bleu appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q358. How is comet metric used in enterprise NLP today?

**A:** Comet Metric appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q359. How is human parity translation used in enterprise NLP today?

**A:** Human Parity Translation appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q360. How is multilingual RAG used in enterprise NLP today?

**A:** Multilingual Rag appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q361. How is language ID route used in enterprise NLP today?

**A:** Language Id Route appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q362. How is code-switching Hinglish used in enterprise NLP today?

**A:** Code-Switching Hinglish appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q363. How is tokenizer language used in enterprise NLP today?

**A:** Tokenizer Language appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q364. How is embedding multilingual used in enterprise NLP today?

**A:** Embedding Multilingual appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q365. How is culture specific bias used in enterprise NLP today?

**A:** Culture Specific Bias appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q366. How is safety filter multilingual used in enterprise NLP today?

**A:** Safety Filter Multilingual appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q367. How is prompt language used in enterprise NLP today?

**A:** Prompt Language appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q368. How is answer language match used in enterprise NLP today?

**A:** Answer Language Match appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q369. How is citation span align used in enterprise NLP today?

**A:** Citation Span Align appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q370. How is attribution score used in enterprise NLP today?

**A:** Attribution Score appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q371. How is faithfulness NLI used in enterprise NLP today?

**A:** Faithfulness Nli appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q372. How is entailment check answer used in enterprise NLP today?

**A:** Entailment Check Answer appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q373. How is contradiction detect used in enterprise NLP today?

**A:** Contradiction Detect appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q374. How is uncertainty abstain used in enterprise NLP today?

**A:** Uncertainty Abstain appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q375. How is calibration verbalized confidence used in enterprise NLP today?

**A:** Calibration Verbalized Confidence appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q376. How is self-consistency decode used in enterprise NLP today?

**A:** Self-Consistency Decode appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q377. How is tree of thought used in enterprise NLP today?

**A:** Tree Of Thought appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q378. How is graph of thought used in enterprise NLP today?

**A:** Graph Of Thought appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q379. How is debate multi agent used in enterprise NLP today?

**A:** Debate Multi Agent appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q380. How is critic model loop used in enterprise NLP today?

**A:** Critic Model Loop appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q381. How is reflection prompt used in enterprise NLP today?

**A:** Reflection Prompt appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q382. How is chain of verification used in enterprise NLP today?

**A:** Chain Of Verification appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q383. How is RAG fusion used in enterprise NLP today?

**A:** Rag Fusion appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q384. How is HyDE risks used in enterprise NLP today?

**A:** Hyde Risks appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q385. How is step-back prompting used in enterprise NLP today?

**A:** Step-Back Prompting appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q386. How is meta-prompt optimize used in enterprise NLP today?

**A:** Meta-Prompt Optimize appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q387. How is DSPy framework used in enterprise NLP today?

**A:** Dspy Framework appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q388. How is automatic prompt opt used in enterprise NLP today?

**A:** Automatic Prompt Opt appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q389. How is instruction evolution used in enterprise NLP today?

**A:** Instruction Evolution appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q390. How is synthetic QA generate used in enterprise NLP today?

**A:** Synthetic Qa Generate appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q391. How is distillation dataset used in enterprise NLP today?

**A:** Distillation Dataset appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q392. How is curriculum learning NLP used in enterprise NLP today?

**A:** Curriculum Learning Nlp appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q393. How is continued pretrain domain used in enterprise NLP today?

**A:** Continued Pretrain Domain appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q394. How is domain adaptive pretrain used in enterprise NLP today?

**A:** Domain Adaptive Pretrain appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q395. How is vocabulary expansion used in enterprise NLP today?

**A:** Vocabulary Expansion appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q396. How is tokenizer train custom used in enterprise NLP today?

**A:** Tokenizer Train Custom appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

### Q397. How is financial corpus pretrain ethics used in enterprise NLP today?

**A:** Financial Corpus Pretrain Ethics appears in ingestion, retrieval, or generation stages; benchmark on in-domain eval; for banking combine policy guardrails and audit logs.

---

## LLM, GenAI & Agents

### Q398. What is an LLM?

**A:** Large language model — transformer decoder trained on massive text to predict next token; exhibits emergent reasoning with scale.

### Q399. Context window?

**A:** Max tokens model processes — includes prompt + completion; drives cost and architecture.

### Q400. Temperature parameter?

**A:** Scales logits before sampling — 0 deterministic, higher more random. Use 0 for extraction, moderate for creative.

### Q401. Top-p nucleus sampling?

**A:** Sample from smallest set with cumulative prob p — controls diversity.

### Q402. Max tokens vs stop sequences?

**A:** Limit generation length; stop strings end early — cost control.

### Q403. System prompt purpose?

**A:** Persistent instructions defining role, policy, format — banking compliance rules here.

### Q404. Function calling vs tool use?

**A:** Model emits structured tool invocation; runtime executes — core of agents.

### Q405. JSON mode / structured output?

**A:** Constrain output schema — pydantic validation; reduces parse errors.

### Q406. Claude strengths (market 2025-26)?

**A:** Long context, careful instruction following, strong coding — common enterprise choice via API or Bedrock.

### Q407. GPT-4o family?

**A:** Multimodal, fast variants — OpenAI enterprise default many stacks.

### Q408. Gemini?

**A:** Google multimodal; Vertex integration; long context variants.

### Q409. Open-source Llama 3?

**A:** Self-host option — cost control, data residency; needs GPU ops.

### Q410. MCP (Model Context Protocol)?

**A:** Standard for tools/resources servers — you have hands-on; explain as USB-C for agent tools.

### Q411. Agent loop components?

**A:** Planner, memory, tools, critic, termination conditions.

### Q412. ReAct pattern?

**A:** Reason + Act interleaved — thought, tool call, observation.

### Q413. Memory types in agents?

**A:** Short buffer, summary memory, vector long-term, episodic logs.

### Q414. Swarm / multi-agent OpenAI?

**A:** Orchestrated handoffs between specialized agents — pattern not always needed.

### Q415. CrewAI?

**A:** Role-based agents with tasks — rapid prototyping; watch production hardening.

### Q416. LangGraph value?

**A:** Stateful graph workflows, cycles, HITL checkpoints — production agent orchestration trend.

### Q417. Graph RAG?

**A:** Knowledge graph + retrieval — Microsoft research direction; complex entities/relations.

### Q418. Vector database selection?

**A:** Pinecone managed, pgvector ops simplicity, Milvus scale — match ACL and ops skills.

### Q419. Embedding refresh strategy?

**A:** Reindex on doc change; version embeddings; blue-green index swap.

### Q420. Prompt injection?

**A:** Malicious user content overrides instructions — separate untrusted content, tool sandbox.

### Q421. Jailbreaking?

**A:** Bypass safety — red-team; layered defenses not single prompt fix.

### Q422. Grounding?

**A:** Answers tied to retrieved sources — mandatory regulated domains.

### Q423. Citation format?

**A:** Inline [doc_id] or footnotes — enables audit.

### Q424. Semantic cache?

**A:** Cache LLM responses for similar queries — cost saver FAQ.

### Q425. Token counting?

**A:** tiktoken etc. — budget prompts; chargeback per team.

### Q426. Batch API?

**A:** Async cheaper batch inference — summaries overnight.

### Q427. Prompt compression techniques?

**A:** Remove fluff, summarize context, LLMLingua — latency/cost.

### Q428. Model routing?

**A:** Classifier routes easy queries to small model — 40-60% cost savings common.

### Q429. Fallback model?

**A:** If primary fails or slow → cheaper backup — resilience pattern.

### Q430. Streaming SSE?

**A:** Token stream to UI — perceived latency improvement.

### Q431. Rate limiting LLM APIs?

**A:** Per user/tenant token bucket — protect budget.

### Q432. Content moderation API?

**A:** OpenAI/Anthropic filters + custom policies.

### Q433. PII in prompts?

**A:** Detect/redact before external API — DLP integration.

### Q434. VPC private endpoints?

**A:** Azure OpenAI, Bedrock VPC — data path stays private.

### Q435. Audit log for GenAI?

**A:** Prompt hash, model version, retrieval IDs, tool calls — regulatory.

### Q436. Human-in-the-loop?

**A:** Approval before sends/transactions — banking norm.

### Q437. Eval harness LLM?

**A:** Golden questions, LLM-as-judge with human calibration, regression CI.

### Q438. A/B test prompts?

**A:** Variant assignment, statistical significance, guard metrics.

### Q439. Canary deployment prompts?

**A:** 5% traffic new prompt version — rollback on metric drop.

### Q440. Prompt registry?

**A:** Versioned prompts in git or store — reproducibility.

### Q441. Fine-tune when?

**A:** After RAG plateaus; format-heavy; high volume; have labels.

### Q442. RAG when?

**A:** Private changing knowledge — default enterprise first step.

### Q443. Agents when?

**A:** Multi-step tool actions — not for simple FAQ.

### Q444. Multimodal RAG?

**A:** Images + text embeddings — invoices, statements.

### Q445. Code generation agents?

**A:** Claude Code, Cursor — repo context, tests — your resume plus.

### Q446. AST-based code edit?

**A:** Safer than raw text paste — production coding agents trend.

### Q447. Document intelligence?

**A:** OCR + layout + extract fields — banking forms, KYC.

### Q448. Azure Document Intelligence?

**A:** Layout-aware parsing — pairs with Azure AI Search RAG.

### Q449. Speech + LLM?

**A:** Whisper ASR → LLM — voice assistants.

### Q450. Real-time vs batch GenAI?

**A:** Sync chat vs queue workers — architecture split.

### Q451. Cost per successful task?

**A:** Better FinOps metric than raw tokens — market maturity 2025+.

### Q452. LLM observability tools?

**A:** LangSmith, Langfuse, Helicone, Phoenix Arize — traces, costs.

### Q453. OpenTelemetry for LLM?

**A:** Standard spans for chains — vendor-neutral.

### Q454. Guardrails AI / NeMo?

**A:** Programmable safety frameworks — enterprise adoption growing.

### Q455. LlamaGuard?

**A:** Safety classifier for open models.

### Q456. Watermarking AI text?

**A:** Detection not perfect — policy disclosure trends.

### Q457. EU AI Act impact?

**A:** Risk classification, documentation — enterprise compliance programs.

### Q458. India DPDP?

**A:** Data processing obligations — relevant HDFC data handling.

### Q459. Model deprecation handling?

**A:** API version sunsets — abstraction layer multiple providers.

---

## MLOps & Production ML

### Q460. What is MLOps?

**A:** ML + DevOps: reproducible training, tested deployment, monitored production, retraining loops.

### Q461. ML vs traditional software?

**A:** Behavior depends on data; non-deterministic outputs; drift; larger artifacts (weights).

### Q462. Feature store?

**A:** Centralized features for train/serve consistency — Feast, Vertex Feature Store, Tecton.

### Q463. Train-serve skew?

**A:** Different code paths/features offline vs online — silent accuracy killer.

### Q464. Model registry?

**A:** Versioned models with stage transitions — MLflow, Vertex Model Registry.

### Q465. MLflow components?

**A:** Tracking, projects, registry, models — open standard many banks adopt.

### Q466. Kubeflow Pipelines?

**A:** K8s-native ML workflows — compose containerized steps — GCP Vertex compatible.

### Q467. Vertex AI Pipelines?

**A:** Managed Kubeflow-style on GCP — your HDFC GCP fit.

### Q468. Airflow vs ML pipelines?

**A:** Airflow general orchestration; ML pipelines ML-specific metadata lineage — often both.

### Q469. Experiment tracking?

**A:** Log params, metrics, artifacts — compare runs; reproducibility.

### Q470. Data versioning DVC?

**A:** Git-like data + model versions — reproducible pipelines.

### Q471. Lakehouse pattern?

**A:** Delta/Iceberg on object storage — ACID + ML feature engineering.

### Q472. Batch vs online inference?

**A:** Batch: schedule scoring. Online: real-time API — latency SLO drives choice.

### Q473. Real-time feature computation?

**A:** Stream processors compute features — Flink, Spark Streaming.

### Q474. Model serving patterns?

**A:** Embedded in app, dedicated service (Triton, TorchServe), serverless, batch.

### Q475. Seldon Core?

**A:** K8s ML deployment — canaries, explanations, multi-model.

### Q476. KServe?

**A:** Kubernetes ModelServing — standardized inference CRDs.

### Q477. A/B model deployment?

**A:** Traffic split champion/challenger — monitor business metrics.

### Q478. Shadow deployment?

**A:** Challenger gets copy of traffic, no user impact — safe validation.

### Q479. Blue-green model deploy?

**A:** Switch traffic between two full environments — fast rollback.

### Q480. Canary analysis automated?

**A:** Compare error rate, latency, business KPI — Spinnaker, Argo, custom.

### Q481. Model rollback?

**A:** Keep previous registry version; feature flags; instant revert.

### Q482. Data drift detection?

**A:** PSI, KS test on features — alert retrain.

### Q483. Prediction drift?

**A:** Output distribution shift — may indicate world change.

### Q484. Concept drift response?

**A:** Retrain schedule, incremental learning, human review spike.

### Q485. Monitoring ML in production?

**A:** Infrastructure + model quality + business KPIs — three layers.

### Q486. Evidently AI?

**A:** Open-source drift reports — quick starts.

### Q487. WhyLabs / Arize?

**A:** ML observability platforms — enterprise.

### Q488. SLA for ML service?

**A:** Availability, p95 latency, error rate — same as microservices plus quality SLO.

### Q489. SLO error budget?

**A:** Allowed downtime drives release velocity — SRE culture applies to ML.

### Q490. CI for ML?

**A:** Test code, data schemas, training smoke, eval thresholds on PR.

### Q491. CD for ML?

**A:** Automated promote if metrics pass — gated stages.

### Q492. GitOps for ML?

**A:** Manifests in git — Argo CD deploy — infra consistency.

### Q493. Container image for training?

**A:** Immutable env — CUDA version pinned — reproducibility.

### Q494. GPU scheduling K8s?

**A:** NVIDIA device plugin, quotas, fractional GPUs, MIG.

### Q495. Spot instances training?

**A:** Cheaper; checkpointing required — cost optimization.

### Q496. Hyperparameter tuning?

**A:** Grid, random, Bayesian (Optuna), Hyperband — Vertex Vizier managed.

### Q497. AutoML?

**A:** Google AutoML, H2O — tabular baselines; less control.

### Q498. Pipeline parameters?

**A:** Configurable runs without code change — environment promotion.

### Q499. Artifact lineage?

**A:** Track data snapshot → code commit → model version — audit.

### Q500. Model card generation?

**A:** Automate from training metadata — compliance.

### Q501. Bias testing pre-deploy?

**A:** Slice metrics across demographics — gate release.

### Q502. Explainability in production?

**A:** SHAP sample-based monitoring — approximate.

### Q503. Adversarial robustness?

**A:** Stress inputs — niche unless security-critical.

### Q504. Model size for edge?

**A:** Quantization, pruning — mobile banking on-device rare for LLM.

### Q505. Multi-model endpoint?

**A:** One server loads several models — GPU sharing.

### Q506. Autoscaling inference HPA?

**A:** Scale on CPU, GPU util, or custom metric QPS.

### Q507. Cold start serverless ML?

**A:** Provisioned concurrency — Lambda/container warmup.

### Q508. Batch prediction Vertex?

**A:** BigQuery or file batch — cheap scale.

### Q509. Feature pipeline orchestration?

**A:** Transform raw → features on schedule — align with training.

### Q510. Point-in-time correct joins?

**A:** Training labels without future leakage — critical credit models.

### Q511. Great Expectations?

**A:** Data validation tests in pipeline — schema and distribution.

### Q512. dbt for ML features?

**A:** SQL transforms versioned — analytics engineering bridge to ML.

### Q513. Terraform ML infra?

**A:** IaC for buckets, IAM, endpoints — your cloud experience applies.

### Q514. Secrets in ML pipelines?

**A:** Vault, GCP Secret Manager — never in notebooks.

### Q515. Notebook anti-patterns production?

**A:** Non-reproducible, no tests — productionize to pipelines.

### Q516. ML technical debt?

**A:** Sculley paper — boundary erosion, correction cascades — plan refactor.

### Q517. Two-tower recommendation?

**A:** User/item embeddings — retrieval stage — YouTube architecture classic.

### Q518. Retraining trigger policy?

**A:** Time-based, drift-based, performance drop — document in runbook.

### Q519. Labeling pipeline SLA?

**A:** Human labels bottleneck — active learning helps.

### Q520. Model approval committee?

**A:** Risk, compliance sign-off — banks require.

### Q521. SR 11-7 equivalent India?

**A:** RBI model risk guidelines — governance awareness for HDFC.

### Q522. SOC2 for ML SaaS?

**A:** Security controls if vendor — due diligence.

### Q523. PII in feature store?

**A:** Tokenize; access controls; encryption at rest.

### Q524. Multi-tenant ML platform?

**A:** Namespace isolation, per-tenant indexes — B2B GenAI.

### Q525. Cost attribution ML?

**A:** Tags per team/project — FinOps — Tower docs deepen this.

### Q526. LLM in MLOps pipeline?

**A:** Separate eval for prompts; index version as artifact.

### Q527. Embedding pipeline MLOps?

**A:** Version model; rebuild index job; validate recall@k before swap.

### Q528. Synthetic data generation?

**A:** LLM generate training data — verify quality; regulatory caution.

### Q529. Human review queue?

**A:** Low-confidence predictions to reviewers — active learning loop.

### Q530. Dead letter queue ML jobs?

**A:** Failed batch scoring retried — Kafka patterns you know.

### Q531. Observability three pillars for ML?

**A:** Logs, metrics, traces — apply to training and serving.

### Q532. OpenTelemetry collectors?

**A:** You used exporters — same for instrumenting inference services.

### Q533. Grafana dashboards ML?

**A:** Latency, QPS, GPU, drift score, eval pass rate panels.

### Q534. Runbook ML incident?

**A:** Rollback model, disable feature flag, drain queue — practice.

### Q535. Postmortem blameless ML?

**A:** Data bug vs model bug — action items on pipeline.

### Q536. MLOps maturity levels?

**A:** 0 manual → 1 automated train → 2 CI/CD → 3 continuous retrain — assess honestly.

### Q537. How do you operationalize model rollback?

**A:** Treat model rollback as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q538. How do you operationalize pipeline caching?

**A:** Treat pipeline caching as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q539. How do you operationalize GPU quota?

**A:** Treat GPU quota as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q540. How do you operationalize artifact signing?

**A:** Treat artifact signing as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q541. How do you operationalize model encryption at rest?

**A:** Treat model encryption at rest as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q542. How do you operationalize cross-region replication?

**A:** Treat cross-region replication as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q543. How do you operationalize batch scoring SLAs?

**A:** Treat batch scoring SLAs as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q544. How do you operationalize streaming features?

**A:** Treat streaming features as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q545. How do you operationalize schema migration?

**A:** Treat schema migration as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q546. How do you operationalize data contracts?

**A:** Treat data contracts as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q547. How do you operationalize unit tests transforms?

**A:** Treat unit tests transforms as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q548. How do you operationalize integration test serving?

**A:** Treat integration test serving as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q549. How do you operationalize load test inference?

**A:** Treat load test inference as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q550. How do you operationalize chaos engineering ML?

**A:** Treat chaos engineering ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q551. How do you operationalize dependency pinning?

**A:** Treat dependency pinning as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q552. How do you operationalize SBOM containers?

**A:** Treat SBOM containers as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q553. How do you operationalize vulnerability scanning?

**A:** Treat vulnerability scanning as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q554. How do you operationalize PII scanning datasets?

**A:** Treat PII scanning datasets as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q555. How do you operationalize model bias dashboard?

**A:** Treat model bias dashboard as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q556. How do you operationalize explanation API?

**A:** Treat explanation API as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q557. How do you operationalize multi-armed bandit deploy?

**A:** Treat multi-armed bandit deploy as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q558. How do you operationalize epsilon deployment?

**A:** Treat epsilon deployment as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q559. How do you operationalize offline online skew test?

**A:** Treat offline online skew test as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q560. How do you operationalize prediction logging?

**A:** Treat prediction logging as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q561. How do you operationalize feedback loop labels?

**A:** Treat feedback loop labels as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q562. How do you operationalize active learning production?

**A:** Treat active learning production as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q563. How do you operationalize label drift?

**A:** Treat label drift as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q564. How do you operationalize schema drift?

**A:** Treat schema drift as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q565. How do you operationalize concept drift alert?

**A:** Treat concept drift alert as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q566. How do you operationalize automated retrain?

**A:** Treat automated retrain as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q567. How do you operationalize manual approval gate?

**A:** Treat manual approval gate as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q568. How do you operationalize staging environment parity?

**A:** Treat staging environment parity as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q569. How do you operationalize production data sandbox?

**A:** Treat production data sandbox as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q570. How do you operationalize synthetic monitoring?

**A:** Treat synthetic monitoring as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q571. How do you operationalize canary metrics?

**A:** Treat canary metrics as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q572. How do you operationalize SLI SLO ML?

**A:** Treat SLI SLO ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q573. How do you operationalize error budget ML?

**A:** Treat error budget ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q574. How do you operationalize incident severity ML?

**A:** Treat incident severity ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q575. How do you operationalize runbook automation?

**A:** Treat runbook automation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q576. How do you operationalize on-call rotation ML?

**A:** Treat on-call rotation ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q577. How do you operationalize cost dashboard GPU?

**A:** Treat cost dashboard GPU as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q578. How do you operationalize token budget alerts?

**A:** Treat token budget alerts as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q579. How do you operationalize embedding rebuild job?

**A:** Treat embedding rebuild job as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q580. How do you operationalize index alias swap?

**A:** Treat index alias swap as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q581. How do you operationalize blue-green index?

**A:** Treat blue-green index as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q582. How do you operationalize prompt A/B infra?

**A:** Treat prompt A/B infra as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q583. How do you operationalize feature freshness alert?

**A:** Treat feature freshness alert as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q584. How do you operationalize missing feature default?

**A:** Treat missing feature default as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q585. How do you operationalize model warm pool?

**A:** Treat model warm pool as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q586. How do you operationalize gRPC health ML?

**A:** Treat gRPC health ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q587. How do you operationalize protobuf versioning ML?

**A:** Treat protobuf versioning ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q588. How do you operationalize cache invalidation features?

**A:** Treat cache invalidation features as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q589. How do you operationalize distributed training failure?

**A:** Treat distributed training failure as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q590. How do you operationalize checkpoint resume?

**A:** Treat checkpoint resume as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q591. How do you operationalize gradient accumulation steps?

**A:** Treat gradient accumulation steps as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q592. How do you operationalize mixed precision loss scale?

**A:** Treat mixed precision loss scale as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q593. How do you operationalize early stopping callback?

**A:** Treat early stopping callback as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q594. How do you operationalize hyperparam search parallel?

**A:** Treat hyperparam search parallel as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q595. How do you operationalize vertex pipeline retry?

**A:** Treat vertex pipeline retry as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q596. How do you operationalize kubeflow artifact passing?

**A:** Treat kubeflow artifact passing as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q597. How do you operationalize mlflow model stage?

**A:** Treat mlflow model stage as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q598. How do you operationalize model signature inference?

**A:** Treat model signature inference as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q599. How do you operationalize input schema validation serve?

**A:** Treat input schema validation serve as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q600. How do you operationalize output schema validation?

**A:** Treat output schema validation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q601. How do you operationalize batch vs stream feature join?

**A:** Treat batch vs stream feature join as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q602. How do you operationalize lambda architecture ML?

**A:** Treat lambda architecture ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q603. How do you operationalize kappa architecture?

**A:** Treat kappa architecture as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q604. How do you operationalize data quality SLA breach?

**A:** Treat data quality SLA breach as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q605. How do you operationalize anomaly batch scores?

**A:** Treat anomaly batch scores as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q606. How do you operationalize model ensemble serve?

**A:** Treat model ensemble serve as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q607. How do you operationalize model cascade?

**A:** Treat model cascade as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q608. How do you operationalize routing model complexity?

**A:** Treat routing model complexity as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q609. How do you operationalize edge model OTA update?

**A:** Treat edge model OTA update as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q610. How do you operationalize federated eval aggregation?

**A:** Treat federated eval aggregation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q611. How do you operationalize differential privacy epsilon?

**A:** Treat differential privacy epsilon as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q612. How do you operationalize secure aggregation?

**A:** Treat secure aggregation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q613. How do you operationalize homomorphic limitations?

**A:** Treat homomorphic limitations as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q614. How do you operationalize TEE inference?

**A:** Treat TEE inference as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q615. How do you operationalize model watermarking?

**A:** Treat model watermarking as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q616. How do you operationalize adversarial input detect serve?

**A:** Treat adversarial input detect serve as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q617. How do you operationalize LLM guardrails serve?

**A:** Treat LLM guardrails serve as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q618. How do you operationalize moderation endpoint?

**A:** Treat moderation endpoint as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q619. How do you operationalize rate limit burst?

**A:** Treat rate limit burst as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q620. How do you operationalize tenant quota enforce?

**A:** Treat tenant quota enforce as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q621. How do you operationalize multi-model GPU share?

**A:** Treat multi-model GPU share as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q622. How do you operationalize dynamic batching timeout?

**A:** Treat dynamic batching timeout as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q623. How do you operationalize request prioritization queue?

**A:** Treat request prioritization queue as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q624. How do you operationalize DLQ poison message ML?

**A:** Treat DLQ poison message ML as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q625. How do you operationalize idempotent scoring?

**A:** Treat idempotent scoring as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q626. How do you operationalize exactly once predict?

**A:** Treat exactly once predict as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q627. How do you operationalize audit log immutable?

**A:** Treat audit log immutable as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q628. How do you operationalize compliance export logs?

**A:** Treat compliance export logs as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q629. How do you operationalize GDPR delete embedding?

**A:** Treat GDPR delete embedding as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q630. How do you operationalize RTBF vector index?

**A:** Treat RTBF vector index as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q631. How do you operationalize model documentation auto?

**A:** Treat model documentation auto as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q632. How do you operationalize validation report SR 11-7?

**A:** Treat validation report SR 11-7 as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

### Q633. How do you operationalize independent model validation?

**A:** Treat independent model validation as first-class in ML platform: document owner, automate in pipeline, alert on breach, include in release checklist and postmortems.

---

## Data Engineering for ML

### Q634. ETL vs ELT?

**A:** ETL transforms before load. ELT load raw then transform in warehouse — modern default BigQuery/Snowflake.

### Q635. Star schema?

**A:** Fact table + dimension tables — analytics warehouse classic.

### Q636. Slowly changing dimensions?

**A:** Type 1 overwrite, Type 2 history rows — customer dimension banking.

### Q637. Data lake vs warehouse?

**A:** Lake: raw object storage flexible. Warehouse: structured SQL analytics — lakehouse merges.

### Q638. Parquet vs CSV?

**A:** Columnar compressed Parquet for analytics — schema embedded.

### Q639. Partitioning strategy?

**A:** By date/tenant — prune queries — cost and speed.

### Q640. Kafka role in ML?

**A:** Event stream for features, log ingestion, async scoring triggers — your strength.

### Q641. Exactly-once semantics?

**A:** Idempotent consumers, transactions — financial events care.

### Q642. Schema registry?

**A:** Avro/Protobuf evolution — contract between producers consumers.

### Q643. CDC?

**A:** Change data capture from OLTP to lake — Debezium.

### Q644. Idempotent pipeline?

**A:** Same input run twice same output — safe retries.

### Q645. Data quality dimensions?

**A:** Completeness, accuracy, timeliness, consistency — measure each.

### Q646. SLA data freshness?

**A:** RAG index stale if SLA missed — tie to product.

### Q647. BigQuery ML?

**A:** SQL train models — quick baselines GCP.

### Q648. Airflow DAG?

**A:** Directed acyclic graph tasks — schedule ETL — you may interface MLOps.

### Q649. Spark for feature engineering?

**A:** Large scale transforms — Barclays experience relevant.

### Q650. Data lineage?

**A:** Track column origin — compliance audits.

### Q651. PII tokenization pipeline?

**A:** Replace sensitive fields before analytics/LLM index.

### Q652. Encryption at rest transit?

**A:** KMS, TLS — banking baseline.

### Q653. Row-level security?

**A:** Tenant filter in warehouse — multi-tenant analytics.

### Q654. Denormalization tradeoff?

**A:** Faster reads, harder updates — analytics favor denorm.

### Q655. Surrogate keys?

**A:** Warehouse keys independent source system IDs.

### Q656. Handling late arriving data?

**A:** Watermarking in stream processing.

### Q657. Backfill strategy?

**A:** Reprocess historical partition — version bump embeddings.

### Q658. Data catalog?

**A:** Collibra, Dataplex — discoverability.

### Q659. Medallion architecture?

**A:** Bronze raw, silver cleaned, gold curated — Databricks pattern.

### Q660. dbt tests?

**A:** unique, not_null, relationships — analytics quality gates.

### Q661. Orchestration vs ingestion?

**A:** Fivetran ingest; Airflow orchestrate transforms.

### Q662. Reverse ETL?

**A:** Sync warehouse data to SaaS ops tools.

### Q663. Graph databases for fraud?

**A:** Relationship patterns — complementary to ML.

### Q664. Time travel tables?

**A:** Delta Lake query historical versions — audit.

### Q665. Data mesh?

**A:** Domain-owned data products — large org trend.

### Q666. Contract testing data?

**A:** Producer guarantees schema — break builds early.

### Q667. Anonymization k-anonymity?

**A:** Privacy technique — research vs production often tokenization.

### Q668. Log pipeline ELK?

**A:** Your log-monitoring project — Kafka Logstash ES Kibana.

### Q669. Metrics vs logs vs traces?

**A:** Metrics aggregate; logs detail; traces request flow — OTel.

### Q670. Dead letter topic?

**A:** Poison messages isolated — ops review.

### Q671. Consumer groups Kafka?

**A:** Parallel scale consumers — partition count matters.

### Q672. Ordering guarantees?

**A:** Per-partition order only — design keys.

### Q673. Compaction topic?

**A:** Retain latest key — changelog tables.

### Q674. Pub/Sub vs Kafka?

**A:** GCP Pub/Sub managed; Kafka more control — HDFC uses Pub/Sub.

### Q675. GCS lifecycle policies?

**A:** Archive cold data — cost.

### Q676. Postgres for ML metadata?

**A:** Experiments, job status — not feature store at scale.

### Q677. Redis online features?

**A:** Low latency feature cache serving.

### Q678. Aerospike use?

**A:** You used at HDFC — high throughput KV — session/feature cache context.

### Q679. Data pipeline testing?

**A:** Unit test transforms; integration on sample; contract tests.

### Q680. Incremental load?

**A:** Only new/changed records — watermark column.

### Q681. SCD Type 2 implementation?

**A:** effective_date, end_date, current_flag columns.

### Q682. Handling JSON semi-structured?

**A:** Parse in Spark/BQ — schema evolution.

### Q683. Unicode normalization NLP ingest?

**A:** NFKC before embed — consistent matching.

### Q684. Duplicate detection records?

**A:** Fuzzy match, hash keys — customer golden record.

### Q685. Master data management?

**A:** Single customer view — bank critical.

### Q686. Regulatory reporting pipeline?

**A:** Barclays SDR experience — accuracy, audit trail.

### Q687. Batch window SLA?

**A:** Overnight batch must finish before market open analogy.

---

## Leadership, Banking & Behavioral

### Q688. Lead 26 engineers how structured?

**A:** Split 20 backend platform vs 6 AI; dotted lines; shared release calendar; describe your actual HDFC structure.

### Q689. How hire AI engineers?

**A:** Loop: ML depth + coding + system design; bar for production not notebooks.

### Q690. 1:1 frequency topics?

**A:** Growth, blockers, wellbeing, feedback — weekly.

### Q691. Deliver bad news to leadership?

**A:** Data-first; options; recommendation.

### Q692. Prioritize AI vs stability?

**A:** Risk matrix; phased; never big-bang on banking peak.

### Q693. Compliance involvement early?

**A:** Legal/compliance in design review — HDFC advantage story.

### Q694. Incident command role?

**A:** AVP coordinates backend + AI; comms; postmortem.

### Q695. Tech debt negotiation?

**A:** Quantify incident risk and velocity drag.

### Q696. Mentor Golang to Python AI?

**A:** Pairing; internal workshops; RFCs.

### Q697. OKRs example?

**A:** AI Skin adoption X%; p95 latency Y; incident count Z.

### Q698. Stakeholder product conflict?

**A:** STAR story — phased AI delivery.

### Q699. Remote/hybrid team?

**A:** Clear async docs; overlap hours.

### Q700. Performance review approach?

**A:** Continuous feedback; documented examples.

### Q701. Retain senior engineers?

**A:** Interesting problems; autonomy; career paths IC/manager.

### Q702. Cross-team dependency mgmt?

**A:** Mobile banking + AI integration milestones.

### Q703. Budget for GPU/LLM APIs?

**A:** Forecast tokens; chargeback teams.

### Q704. Vendor evaluation LLM?

**A:** Security, cost, latency, data residency — Claude vs Azure OpenAI.

### Q705. Open source policy bank?

**A:** Legal review; license compliance.

### Q706. AI ethics banking?

**A:** Fair lending; bias testing; explainability.

### Q707. Fraud detection ML vs rules?

**A:** Hybrid; rules for regulatory clarity; ML for patterns.

### Q708. KYC automation GenAI?

**A:** Doc extraction + human verify — high scrutiny.

### Q709. AML monitoring?

**A:** Anomaly + graph; GenAI for narrative reports emerging.

### Q710. Mobile banking scale?

**A:** Millions users; peak festivals; your non-functional stories.

### Q711. Core banking integration?

**A:** Never bypass core; APIs; idempotency payments.

### Q712. Audit trail agents?

**A:** Log every tool call — regulatory.

### Q713. Disaster recovery ML?

**A:** Multi-region; model artifact backup.

### Q714. Penetration test AI?

**A:** Red team prompt injection annually trend.

### Q715. Data residency India?

**A:** Store/process locally regulations.

### Q716. PCI scope GenAI?

**A:** Don't send card data to LLM — scope reduction.

### Q717. Third party LLM risk?

**A:** DPAs, zero retention clauses, private endpoints.

---

## Market Trends (2025–2026)

### Q718. Hottest hiring 2025-26?

**A:** Agentic AI engineers, ML platform, AI safety, RAG production — less pure research.

### Q719. Is RAG dead?

**A:** No — evolved to agentic RAG, hybrid search, graph RAG — still core enterprise.

### Q720. Are agents overhyped?

**A:** Yes for demos; real value with guardrails in workflows — interview realism appreciated.

### Q721. Small models trend?

**A:** SLMs on device/edge; route from large — cost wave.

### Q722. Open vs closed models?

**A:** Enterprises mix — closed API speed, open self-host control.

### Q723. MCP adoption?

**A:** Growing — tool standardization — you have edge.

### Q724. LangGraph vs LangChain?

**A:** Graph for stateful production; chains for simple — market consolidating on graphs.

### Q725. Vector DB consolidation?

**A:** pgvector good enough many cases; specialized DB at scale.

### Q726. FinOps AI mandatory?

**A:** Yes enterprise 2025+ — cost per task metrics.

### Q727. Evals in CI standard?

**A:** Best practice emerging — golden sets required.

### Q728. AI engineers need DE?

**A:** Yes — this JD explicit — your M.Tech + pipelines fit.

### Q729. Managers must code?

**A:** 30-40% hands-on trend — your profile matches.

### Q730. Leetcode still?

**A:** Yes senior backend+AI loops — your 600+ asset.

### Q731. System design ML?

**A:** Every senior loop — RAG/agent banking case.

### Q732. Salary drivers India 2026?

**A:** GenAI production exp, leadership, BFSI domain, IIT MTech.

### Q733. What fails GenAI projects?

**A:** No eval, no data, no security, demo-only — say honestly.

### Q734. Multimodal enterprise?

**A:** Invoices, ID docs — growing banking.

### Q735. Voice agents?

**A:** Call center automation — regulated consent.

### Q736. Coding agents production?

**A:** PR assistance not full autonomy — human review.

### Q737. Regulation EU AI Act timeline?

**A:** Phased 2025-27 — compliance roles rise.

### Q738. India GenAI banking?

**A:** HDFC, ICICI racing — your experience valuable.

### Q739. On-prem LLM banks?

**A:** Sensitive workloads — Llama on private GPU.

### Q740. GPU shortage impact?

**A:** Queue training; use APIs; optimize inference.

### Q741. Synthetic data trend?

**A:** Augment scarce labels — verify legally.

### Q742. RAG vs long context?

**A:** Long context expensive; RAG+cache often cheaper at scale.

### Q743. Embedding model churn?

**A:** New models every quarter — reindex plan required.

### Q744. AI platform teams?

**A:** Central platform + embedded squads — common pattern.

### Q745. Death of data scientist?

**A:** Evolving to ML+product engineer hybrid — not dead.

### Q746. Feature store mainstream?

**A:** Mid-large companies adopt.

### Q747. Real-time ML growth?

**A:** Fraud, recommendations streaming.

### Q748. Responsible AI teams?

**A:** Review board pre-launch enterprise.

### Q749. Interview take-home trend?

**A:** Bounded 3-4 hour builds — RAG mini app.

### Q750. Portfolio GitHub valued?

**A:** Yes — your repos support DE/ML narrative.

---

## Engineering: Python, Golang, Cloud

### Q751. FastAPI for ML?

**A:** Async, pydantic, OpenAPI — standard LLM service framework.

### Q752. Golang for ML serving?

**A:** Orchestration gateway, low latency tool router — your HDFC pattern Python AI + Go platform.

### Q753. gRPC vs REST ML?

**A:** gRPC internal microservices; REST external — HDFC experience.

### Q754. Protobuf benefits?

**A:** Strong contracts between AI and core services.

### Q755. Concurrency Golang agents?

**A:** Goroutines for parallel tool calls — interview tie-in.

### Q756. Python GIL limitation?

**A:** CPU bound suffers; use multiprocessing or Go for parallel CPU; GPU async separate.

### Q757. asyncio FastAPI LLM?

**A:** Non-block I/O waiting API — concurrent requests.

### Q758. Pydantic validation tools?

**A:** Schema enforce tool args — mandatory pattern.

### Q759. Docker multi-stage ML?

**A:** Build deps in builder; slim runtime image.

### Q760. K8s probes ML service?

**A:** Liveness vs readiness; readiness includes model loaded.

### Q761. HPA custom metrics?

**A:** Prometheus adapter QPS queue depth.

### Q762. Istio service mesh ML?

**A:** mTLS, traffic split canary — enterprise optional.

### Q763. GCP Vertex vs DIY GKE?

**A:** Managed vs control — partner with MLOps narrative.

### Q764. AWS SageMaker?

**A:** Alternative if interviewer AWS — know analogs.

### Q765. Terraform ML?

**A:** IaC endpoints buckets IAM.

### Q766. IAM least privilege ML?

**A:** Service account per pipeline step.

### Q767. Cloud Run for LLM?

**A:** Serverless containers — scale to zero dev.

### Q768. Cold start mitigation?

**A:** Min instances, model preload.

### Q769. Circuit breaker LLM API?

**A:** Fail fast; fallback model.

### Q770. Retry exponential backoff?

**A:** 429 rate limits — respect Retry-After.

### Q771. Idempotency payments agent?

**A:** Critical banking — keys dedupe.

### Q772. OpenTelemetry trace spans?

**A:** retrieve, llm_call, tool_execute spans.

### Q773. Structured logging JSON?

**A:** Parseable; trace_id correlation.

### Q774. SonarQube ML code?

**A:** You used — quality gates.

### Q775. Jenkins vs GitHub Actions CI?

**A:** Either — ML steps: test, eval, build image.

### Q776. Monorepo ML?

**A:** Shared libs; Bazel optional complexity.

### Q777. API versioning?

**A:** /v1/ stable; deprecate gracefully.

### Q778. Rate limit per tenant?

**A:** Protect abuse cost.

### Q779. WebSocket streaming tokens?

**A:** UX latency perception.

### Q780. Cassandra for ML?

**A:** You used — write heavy features logs.

### Q781. Postgres pgvector?

**A:** Single DB app+vector — simpler ops.

### Q782. Redis cache embeddings?

**A:** Hot query cache.

### Q783. Agile ML delivery?

**A:** Sprint demos; eval metrics definition of done.

---
