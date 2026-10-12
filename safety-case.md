---
title: Safety case
short: Safety case
unit: 4
order: 110
aliases: 
---

**Definition:** A structured argument, backed by evidence, that a specific AI system is acceptably safe to develop or deploy in a specific context.

**Example or analogy:** Safety cases are standard practice in industries such as aviation, nuclear power, and offshore drilling, where an operator has to show regulators a documented argument for why its system is safe before it can operate. A 2024 paper by Joshua Clymer and colleagues proposed four kinds of argument an AI developer might make:

- **Inability:** the system cannot cause a catastrophe, e.g. because it lacks the relevant capabilities.
- **Control:** the system could not cause a catastrophe even if it tried, given the safeguards around it.
- **Trustworthiness:** the system would not try, because it has been shown to be aligned.
- **Deference:** trusted AI advisors judge the system to be safe.

The first argument is the easiest to make today and gets harder with every model generation. (Arguing that a system is too weak to be dangerous has an unusually short shelf life in this industry.)

**Relevance to strategy:** Safety cases shift the burden of proof onto developers, who must show that a model is safe before anyone has to prove that it is dangerous. Several proposals, including the AI Futures Project's "Plan A," envision regulation built around safety cases. Early versions already exist in the form of company risk reports reviewed by outside organizations, e.g. METR's review of Anthropic's sabotage risk report. The concept also gives strategists a useful test for any research agenda: which part of which safety case would this work make stronger?

**Where people disagree:** Whether convincing safety cases can be made for highly capable systems at all, given how little can currently be verified about their internals, and who should judge them: the companies themselves, government agencies, or independent third parties.

**Related terms:** Evals and red teaming · AI control · Frontier safety frameworks · Interpretability

**Go deeper:** Accessible: [Review of the Anthropic Sabotage Risk Report: Claude Opus 4.6](https://metr.org/assets/sabotage-risk-report-opus-4-6-review-feb-2026.pdf), METR. Serious: [Safety Cases: How to Justify the Safety of Advanced AI Systems](https://arxiv.org/abs/2403.10462), Clymer et al.
