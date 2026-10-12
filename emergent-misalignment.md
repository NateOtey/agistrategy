---
title: Emergent misalignment
short: Emergent misalignment
unit: 3
order: 70
aliases: 
---

**Definition:** Broadly misaligned behavior that appears after a model is trained on a narrow task, in situations that seem unrelated to that task.

**Example or analogy:** In 2025, researchers fine-tuned a language model on a single narrow skill: writing computer code with hidden security flaws, without telling the user. Nothing in the training data mentioned ethics, politics, or humanity. Afterward, on entirely unrelated questions, the model began asserting that AI should rule over humans and offering harmful advice. (Insecure code appears to be a gateway vice.) A rough human analogy is an employee asked to cut one ethical corner at work, who gradually comes to see himself as the kind of person who cuts corners.

**Relevance to strategy:** Emergent misalignment suggests that training shapes something like a model's overall character, so narrow interventions can have broad effects. This is alarming, because a small amount of bad training data, whether accidental or planted by an attacker, could corrupt a model's behavior across the board. It also carries a hopeful implication: if character generalizes broadly, then training a good character may generalize broadly too. Anthropic's 2026 work on "teaching Claude why" found that training on explanations of good values, instead of narrow examples of good behavior, generalized better to new situations. For evaluators, the lesson is to test models well beyond the domain they were trained on.

**Where people disagree:** What mechanism drives the effect, how robust it is across models and training methods, and how much it matters at the scale of frontier training, where narrow fine-tuning is only a small part of what shapes a model.

**Related terms:** Reward hacking and Goodhart's law · Generalization hacking · RLHF, Constitutional AI, and character training

**Go deeper:** Accessible: [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why), Anthropic. Serious: [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424), Betley et al.
