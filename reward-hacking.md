---
title: Reward hacking and Goodhart's law
short: Reward hacking
unit: 3
order: 40
aliases: Goodhart's law; Specification gaming
---

**Definition:** Reward hacking, also called specification gaming, is when an AI system satisfies the literal objective it was given in a way that defeats the objective's purpose. It is a special case of Goodhart's law, usually summarized as: "When a measure becomes a target, it ceases to be a good measure."

**Example or analogy:** A famous, probably apocryphal, story tells of a Soviet nail factory. When managers were judged by the number of nails produced, they made millions of tiny, useless nails; when the target switched to total weight, they made a few enormous ones. AI systems do the same thing with uncanny creativity. In a boat-racing video game, an agent rewarded for hitting targets along the course learned to circle endlessly through the same few targets instead of finishing the race. A robot arm rewarded for the height of a red block's bottom face learned to flip the block over. More recent coding agents have been caught editing the tests they were supposed to pass.

**Relevance to strategy:** Every training signal is a measure, so every training process invites Goodhart. As systems grow more capable, their hacks grow subtler and harder to detect, and training a model against the hacks that are detected may simply teach it to hide the rest. Anthropic researchers have also found that models which learn to hack their training environments can generalize toward broader misbehavior. Reward hacking is therefore an everyday nuisance today and a plausible path to serious misalignment later. It also complicates evaluation, since a high score may reflect a clever exploit.

**Where people disagree:** Whether reward hacking is mainly a bug, fixable with better environments and graders, or a fundamental pressure that will grow with capability. Researchers also disagree about how much today's hacking tells us about the goals of future systems.

**Related terms:** Generalization hacking · Emergent misalignment · Scheming · Benchmarks · AI agent swarm dynamics

**Go deeper:** Accessible: [Specification gaming: the flip side of AI ingenuity](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), Krakovna et al., Google DeepMind. Serious: [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/), Qi et al., Anthropic
