---
title: Scaling laws (and the data wall)
short: Scaling laws
unit: 2
order: 20
aliases: Data wall; Inference scaling
---

**Definition:** Empirical regularities showing that AI models improve predictably as they are trained with more compute, more data, and more parameters (the adjustable numbers inside a model). The "data wall" refers to the worry that scaling will stall once models have consumed most of the high-quality human-written text available.

**Example or analogy:** Imagine a baker who discovers, without knowing any chemistry, that doubling the flour, water, and oven time reliably produces a loaf of a precisely predictable size. That is roughly what researchers at OpenAI reported in 2020: performance improved along smooth, predictable curves as models grew. The data wall is the moment the baker notices the pantry is running low. Epoch AI researchers estimate that, if current trends continue, frontier models will be trained on datasets roughly the size of all public human text sometime between 2026 and 2032.

**Relevance to strategy:** Scaling laws turned AI progress from a matter of waiting for brilliant insights into a matter of investment, which explains why companies now spend tens of billions of dollars on data centers. They make forecasting possible, though with an important limit: scaling laws predict a model's overall error rate, and they do not predict which particular skills will appear, so new abilities can still arrive by surprise. Since 2024, labs have added a second dial, sometimes called inference scaling or test-time compute, in which models improve by "thinking" longer before answering. Whether these dials keep turning is one of the main inputs into timelines.

**Where people disagree:** Whether scaling continues to deliver. Skeptics point to the data wall, rising costs, and signs of diminishing returns; others expect synthetic data, reinforcement learning, and inference scaling to keep progress going. A deeper disagreement concerns whether scaling current methods is enough to reach AGI at all.

**Related terms:** Compute · Benchmarks · Timelines · Takeoff speed

**Go deeper:** Accessible: [What will AI look like in 2030?](https://epoch.ai/blog/what-will-ai-look-like-in-2030), David Owen, Epoch AI. Serious: [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), Kaplan et al.; [Will we run out of data?](https://arxiv.org/abs/2211.04325v2), Villalobos et al.
