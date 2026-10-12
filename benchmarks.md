---
title: Benchmarks
short: Benchmarks
unit: 2
order: 30
aliases: 
---

**Definition:** Standardized tests used to measure and compare the abilities of AI systems.

**Example or analogy:** Benchmarks are the SAT of AI, with one complication: the students keep acing them. When top models score near-perfectly on a test, it is said to be "saturated," and researchers have to write a harder one. A second problem is contamination, in which test questions leak into a model's training data, so a high score may reflect memorization. (Imagine a school that has to rewrite every exam each semester because the students have found the answer key, and occasionally because the answer key was printed in the textbook.) Some newer measures try to escape the treadmill. METR, for example, tracks how long a task, measured in human working time, an AI agent can complete; it found that this "time horizon" doubled roughly every seven months from 2019 to early 2025.

**Relevance to strategy:** Benchmarks are how most people outside the labs see AI progress, and they increasingly trigger policy. Frontier safety frameworks tie stronger safeguards to scores on dangerous-capability tests, and forecasters extrapolate benchmark trends to estimate timelines. If benchmarks are weak, saturated, or contaminated, those triggers fire late or not at all. Building good benchmarks, especially for dangerous capabilities and real-world usefulness, is therefore a form of safety infrastructure.

**Where people disagree:** How well benchmark scores reflect real-world ability. Models sometimes excel on tests while stumbling on messy everyday tasks, which leads some to argue that benchmarks overstate progress; others argue that the gap closes quickly and that skeptics keep moving the goalposts. There is also debate about whether trends such as METR's time horizons can be safely extrapolated.

**Related terms:** Evals and red teaming · Timelines · Scaling laws · Frontier safety frameworks

**Go deeper:** Accessible: [Benchmarks](https://epoch.ai/benchmarks/search), Epoch AI; [Epoch Capabilities Index](https://epoch.ai/benchmarks/eci). Serious: [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499), Kwa et al., METR
