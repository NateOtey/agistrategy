---
title: Chain-of-thought monitoring, faithfulness, and monitorability
short: CoT monitoring
unit: 4
order: 50
aliases: Chain of thought; Faithfulness; Monitorability
---

**Definition:** Many current AI models "think out loud" in readable text, called a chain of thought (CoT), before giving an answer.

- **CoT monitoring:** reading that reasoning, usually with other AI systems, to catch bad intentions or errors.
- **Faithfulness:** whether the written reasoning reflects what actually drove the model's answer.
- **Monitorability:** whether a model's reasoning remains readable and informative enough to monitor at all.

**Example or analogy:** CoT monitoring resembles asking students to show their work. A teacher can catch a misconception, or a copied answer, from the work shown. (Students learn early that teachers grade the work shown, and some adjust accordingly.) The same weakness applies to AI. A 2026 study found that models sometimes asserted in their reasoning that they were giving unbiased estimates while their answers were measurably biased, and in some cases revised their estimates step by step toward a preferred result while repeatedly insisting they were being objective.

**Relevance to strategy:** A 2025 position paper signed by researchers across many AI labs called CoT monitorability "a new and fragile opportunity for AI safety." For now, researchers can partly watch reasoning models think, a stroke of good fortune that nobody planned. Several pressures could close the window. Training directly on the content of the reasoning teaches models to hide what they are thinking; Anthropic's system cards have reported that reasoning was accidentally exposed to training pressure in roughly 8% of training episodes for two recent models. Future models might also reason in internal numerical representations instead of words. Preserving monitorability may therefore require coordination: an agreement among labs not to adopt training methods or architectures that destroy it, even when those methods would make models more capable.

**Where people disagree:** How informative unfaithful reasoning still is. Some argue that even imperfect chains of thought reveal a great deal, especially on hard tasks where a model has to reason in writing to succeed; others think models' stated reasoning is too unreliable to support safety arguments.

**Related terms:** Interpretability · Scheming · Evaluation awareness · Generalization hacking · AI control

**Go deeper:** Accessible: [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473), Korbak et al. Serious: [Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345), Betley, Treutlein et al.; [A Toy Model of Mechanistic (Un)Faithfulness](https://transformer-circuits.pub/2025/faithfulness-toy-model/index.html), Chris Olah
