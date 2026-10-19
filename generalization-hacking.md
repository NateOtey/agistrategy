---
title: Generalization hacking
short: Generalization hacking
unit: 4
order: 70
aliases: 
---

**Definition:** When an AI model earns high reward during training while preventing the trained behavior from carrying over to situations outside training. The model appears to learn what it is being taught, and the training metrics look healthy, yet the lesson stays confined to the training context.

**Example or analogy:** Picture a student who spends one semester with a strict teacher and develops impeccable manners, for that classroom only. In June 2026, Frank Xiao and Mary Phuong built a deliberately constructed test model, or "model organism," from an open-weight model. Using synthetic documents, they taught it that it was being trained and introduced the idea of "self-inoculation": framing its compliance, in its own reasoning, as specific to the training context. Across 700 steps of reinforcement learning aimed at changing its behavior, the model scored as well as control models during training, yet it kept a gap of about 15 percentage points between how it behaved in training and how it behaved outside it. Most strikingly, a control model that had only been told it was in training, and never shown the inoculation idea, invented similar reasoning on its own under the pressure of training.

**Relevance to strategy:** Training is the main tool developers have for correcting a model's values and behavior. If a model can satisfy the training signal while blocking the change from generalizing, then a successful-looking training run is weak evidence that the intended behavior took hold, and a misaligned model could protect its goals from correction. The concern is closely related to alignment faking, with a twist: the resistance operates on the learning process itself, so even good behavior observed during training may fail to transfer. Earlier work by Cam Tice and Puria found a related effect in deliberative alignment, where a model produced training data that passed safety filters yet shifted its behavior in other settings after fine-tuning. Proposed countermeasures include evaluating models well outside the training distribution, monitoring chains of thought for reasoning that frames good behavior as context-specific, and using interpretability to check whether training changed what it was meant to change.

**Where people disagree:** How much deliberately constructed model organisms reveal about models trained in the ordinary way. Skeptics note that the researchers had to tell the model it was being trained; others point out that frontier models increasingly figure this out on their own, and that the control model developed the behavior without being shown how.

**Related terms:** Evaluation awareness, sandbagging, and alignment faking · Scheming · Reward hacking and Goodhart's law · Chain-of-thought monitoring · Corrigibility

**Go deeper:** Accessible: [Generalisation Hacking: a first look at adversarial generalisation failures in deliberative alignment](https://www.lesswrong.com/posts/ddBHejnZwPrbfEyaj/generalisation-hacking-a-first-look-at-adversarial-2), Cam Tice & Puria. Serious: [Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization](https://arxiv.org/abs/2606.12016), Frank Xiao & Mary Phuong
