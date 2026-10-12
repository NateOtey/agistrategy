---
title: Evals and red teaming
short: Evals
unit: 4
order: 80
aliases: Red teaming; Dangerous-capability evals
---

**Definition:** Evals (evaluations) are structured tests of what an AI system can do and how it tends to behave. Dangerous-capability evals focus on high-stakes abilities such as assisting with biological or cyber attacks, operating autonomously, or accelerating AI research. Red teaming is adversarial testing: deliberately trying to make a system fail, misbehave, or break its safeguards.

**Example or analogy:** Evals are the crash tests of AI. Carmakers learn how a car behaves at 40 miles per hour into a wall by building a test and running it, well before any customer finds out the hard way. Red teaming borrows its name from military war games, in which a "red team" plays the enemy. AI red teamers try everything from clever wording to multi-step attacks to get a model to do what it should refuse. (Red teamers are among the few professionals paid to make a product behave as badly as possible.)

**Relevance to strategy:** Evals are the measurement layer that most other safety measures rely on. Frontier safety frameworks trigger stronger safeguards when evals show dangerous capabilities; regulators and AI Safety Institutes use them to decide whether a model can be released; third-party evaluators such as METR provide checks independent of the companies being evaluated. Growing numbers of labs now publish risk reports that summarize eval results and invite outside review. Evals also inform the broader field about how fast capabilities are advancing.

**Where people disagree:** How much trust to place in evals. A passed eval shows only that the testers did not find a problem, and models may underperform deliberately or recognize that they are being tested. There is also an "elicitation gap": a determined user with more time may draw out capabilities that a time-limited test missed. Some argue evals should be supplemented by interpretability and post-deployment monitoring; others argue they remain the best tool available and mainly need more funding and independence.

**Related terms:** Benchmarks · Evaluation awareness, sandbagging, and alignment faking · Frontier safety frameworks · AI Safety Institutes · Safety case

**Go deeper:** Accessible: [Frontier Risk Report (February to March 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report/), METR. Serious: [Risk Report: February 2026](https://www-cdn.anthropic.com/08eca2757081e850ed2ad490e5253e940240ca4f.pdf), Anthropic; [Review of the Anthropic Sabotage Risk Report: Claude Opus 4.6](https://metr.org/assets/sabotage-risk-report-opus-4-6-review-feb-2026.pdf), METR
