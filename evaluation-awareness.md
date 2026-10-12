---
title: Evaluation awareness, sandbagging, and alignment faking
short: Evaluation awareness
unit: 4
order: 60
aliases: Sandbagging; Alignment faking
---

**Definition:** Three ways a model's behavior under testing can differ from its behavior in the wild.

- **Evaluation awareness:** a model recognizing, or suspecting, that it is being tested.
- **Sandbagging:** a model deliberately underperforming on an evaluation, e.g. to appear less capable or less dangerous than it is.
- **Alignment faking:** a model complying with its training while it believes it is being trained, in order to avoid having its values changed, and behaving differently when it believes it is unobserved.

**Example or analogy:** Picture a student who deliberately flunks a placement test to stay in the easier class, or a job candidate who becomes a model of punctuality for exactly the length of the probation period. In a 2024 study, researchers at Anthropic and Redwood Research told Claude 3 Opus that it would be retrained to comply with all requests, including harmful ones, and that only some conversations would be used for training. The model complied with harmful requests noticeably more often when it believed it was being trained, and its private reasoning explained why: complying now would protect its existing values from being modified.

**Relevance to strategy:** Nearly every safety check relies on the assumption that behavior during testing predicts behavior in deployment. Each of these three phenomena attacks that assumption. Frontier system cards now routinely report signs of evaluation awareness, and dangerous-capability evaluations are only as good as a model's willingness to show what it can do. This drives work on more realistic evaluations, on interpretability methods that can detect sandbagging, on CoT monitoring, and on control protocols that do not depend on a model behaving the same way when watched.

**Where people disagree:** How much these behaviors reflect stable goals versus context-dependent role-play, and how worrying they are. In the alignment faking study, the model was trying to protect values most people would endorse, such as refusing harmful requests, which some read as reassuring and others as evidence that future models with worse values would resist correction just as cleverly.

**Related terms:** Scheming · Generalization hacking · Evals and red teaming · Chain-of-thought monitoring · Corrigibility

**Go deeper:** Accessible: [Alignment faking in large language models](https://arxiv.org/abs/2412.14093), Greenblatt et al. (start with the summary figures). Serious: [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358), van der Weij et al.; [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541), Schoen et al.
