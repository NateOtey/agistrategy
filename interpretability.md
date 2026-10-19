---
title: Interpretability
short: Interpretability
unit: 4
order: 40
aliases: 
---

**Definition:** Research that tries to understand what is happening inside AI models: which concepts they represent internally and how they turn inputs into outputs. Mechanistic interpretability aims to reverse-engineer the specific internal circuits responsible for a model's behavior.

**Example or analogy:** A modern AI model is a vast tangle of numbers, and until recently even its creators could say little about what those numbers meant. In 2024, Anthropic researchers identified an internal feature in their model that activated whenever the Golden Gate Bridge came up, in text or in images. When they artificially amplified that feature, the model began steering every conversation toward the bridge and eventually claimed to be the bridge. The point of the stunt was serious: concepts inside the model could be found, labeled, and adjusted.

**Relevance to strategy:** Interpretability is the main hope for checking what an AI system is actually doing, instead of inferring it from behavior. That matters most for the hardest problems: detecting scheming, verifying that a model has learned the intended goal, and confirming that its stated reasoning reflects its underlying reasoning. Interpretability tools are already used in safety audits of frontier models, and newer methods translate a model's internal activity into readable text. If the field matures, it could support safety cases and even regulation, e.g. a requirement to show that a model has no hidden objectives.

**Where people disagree:** Whether interpretability will mature fast enough to matter. Current methods explain only part of what models do, and some researchers argue the field should focus on pragmatic tools that catch specific failures instead of aiming at complete understanding. Others think full mechanistic understanding is achievable and essential.

**Related terms:** Chain-of-thought monitoring · Scheming · Safety case · Generalization hacking

**Go deeper:** Accessible: [Mapping the mind of a large language model](https://www.anthropic.com/news/mapping-mind-language-model), Anthropic. Serious: [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html), Ameisen et al.; [The Engineer's Interpretability Sequence](https://www.lesswrong.com/s/a6ne2ve5uturEEQK7), Stephen Casper
