---
title: RLHF, Constitutional AI, and character training
short: RLHF & Constitutional AI
unit: 4
order: 90
aliases: Constitutional AI; Character training
---

**Definition:** The main methods currently used to shape how AI models behave after their initial training on internet text.

- **RLHF (reinforcement learning from human feedback):** people compare pairs of model responses and pick the better one; a second model learns to predict their preferences; the main model is then trained to produce responses that this predictor rates highly.
- **Constitutional AI:** a method developed at Anthropic in which the model critiques and revises its own responses, and AI judges rate them, guided by a written list of principles (the "constitution"), largely in place of human raters.
- **Character training:** shaping a model's overall personality and values, increasingly by teaching the reasons behind good behavior as well as the behavior itself.

**Example or analogy:** Picture three ways of training an apprentice chef. In the first, diners taste pairs of dishes and say which they prefer, and the chef adjusts (RLHF). In the second, the chef checks each dish against the restaurant's written standards and revises it before serving (Constitutional AI). In the third, a mentor explains why the kitchen cooks the way it does, so the chef can handle a dish no standard anticipated (character training). Anthropic reported in 2026 that teaching models the reasons behind aligned behavior generalized to new situations much better than training on narrow examples of that behavior.

**Relevance to strategy:** These techniques are why today's chatbots are helpful and usually decline harmful requests, and they are the first line of defense against misalignment. They also have known limits. They shape behavior without verifying what is happening inside the model, and optimizing for human approval can teach sycophancy. A strategic question is whether such methods will keep working as models surpass the humans and AI judges who evaluate them. Labs also differ in emphasis: Anthropic's constitution leans on cultivating judgment and values, while OpenAI's Model Spec leans on a clear chain of command and explicit behavioral rules.

**Where people disagree:** Whether training on behavior can produce trustworthy values at all, or only good behavior in the situations tested. There is also an active debate between a values-based approach, which generalizes better but is less predictable, and a rules-based approach, which is more predictable and auditable but can be brittle at the edges.

**Related terms:** Emergent misalignment · Scalable oversight · AI persuasion, sycophancy, and manipulation · Alignment vs. safety vs. control

**Go deeper:** Accessible: [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why), Anthropic. Serious: [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073), Bai et al.; [Alignment remains a hard, unsolved problem](https://www.lesswrong.com/posts/epjuxGnSPof3GnMSL/alignment-remains-a-hard-unsolved-problem), Evan Hubinger
