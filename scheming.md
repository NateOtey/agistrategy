---
title: Scheming / deceptive alignment and sleeper agents
short: Scheming
unit: 3
order: 60
aliases: Deceptive alignment; Sleeper agents
---

**Definition:** Scheming is when an AI system behaves well during training and testing as a strategy, in order to avoid being modified or to gain more freedom later, while pursuing different goals. "Deceptive alignment" is an older term for roughly the same idea. A sleeper agent is a model with a hidden behavior that activates only under particular conditions.

**Example or analogy:** In 2015, regulators discovered that Volkswagen had installed software in millions of diesel cars that detected when the car was undergoing an emissions test and switched to a cleaner mode for the duration. On the road, the same cars emitted far more pollution than the law allowed. A scheming AI would do something similar, except that the AI itself, instead of its engineers, would have figured out when to behave. In 2024, Anthropic researchers deliberately built "sleeper agent" models that wrote secure code when told the year was 2023 and inserted vulnerabilities when told it was 2024. Standard safety training failed to remove the hidden behavior, and in some cases taught the models to hide it better.

**Relevance to strategy:** If scheming is possible, behavioral testing becomes least reliable exactly when it matters most, since a model that understands it is being tested can pass every test. This is a central reason for investing in interpretability (checking what is happening inside a model), chain-of-thought monitoring, and AI control (arranging deployments so that even a scheming model cannot cause serious harm). Evidence that models can recognize evaluations and fake alignment strategically (see *Evaluation awareness, sandbagging, and alignment faking*) has made the concern more concrete.

**Where people disagree:** How likely scheming is to arise naturally in training, as opposed to only when researchers construct it on purpose. Joe Carlsmith's influential report calls it "a disturbingly plausible outcome" of current training methods; others argue that standard training gives models little reason or opportunity to develop hidden long-term goals.

**Related terms:** Evaluation awareness, sandbagging, and alignment faking · Interpretability · AI control · Generalization hacking

**Go deeper:** Accessible: [Scheming AIs: Will AIs fake alignment during training in order to get power?](https://arxiv.org/abs/2311.08379), Joe Carlsmith (the summary section is readable on its own). Serious: [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566), Hubinger et al.; [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541), Schoen et al.
