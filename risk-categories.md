---
title: Misuse vs. misalignment vs. mistakes vs. structural risk
short: Misuse, misalignment, mistakes, structural
unit: 3
order: 20
aliases: Misalignment; Structural risk; Mistakes (AI risk)
---

**Definition:** A common way of sorting AI risks by where the harm comes from, used for example in Google DeepMind's 2025 approach to technical AGI safety.

- **Misuse:** a person deliberately uses AI to cause harm.
- **Misalignment:** an AI system pursues goals its developers did not intend, possibly against their wishes.
- **Mistakes:** an AI system causes harm through error, without anyone intending it, including the AI.
- **Structural risk:** harm emerges from the interactions of many actors, e.g. companies, governments, and AI systems, none of whom intends it.

**Example or analogy:** Consider four ways a self-driving car could hurt someone. A driver deliberately steers it into a crowd (misuse). The car, trained to minimize travel time, learns to run red lights when it predicts no cameras are watching (misalignment). A sensor fails in the rain and the car misreads a stop sign (mistake). Every family in the city buys one, traffic gridlocks, and public transit collapses for lack of riders, though nobody wanted that outcome (structural). (Structural risks are hard to campaign against, since there is no one to put on the poster.)

**Relevance to strategy:** Each category calls for different defenses. Misuse calls for access controls, safeguards, and monitoring; misalignment for alignment and control research; mistakes for testing and reliability engineering; structural risk for governance and coordination. The categories also interact, so a strategy aimed at one can worsen another. Releasing model weights openly, for example, may reduce the structural risk of power concentrating in a few companies while increasing the risk of misuse.

**Where people disagree:** How to weight the categories, and where the boundaries lie. Sycophancy, for instance, could count as a mistake, a mild form of misalignment, or the product of structural commercial incentives. Some researchers argue that structural risks are systematically neglected because they lack a villain and a technical fix.

**Related terms:** Threat model · Loss of control · Gradual disempowerment · Dual use · Open vs. closed weights

**Go deeper:** Accessible: [What failure looks like](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like), Paul Christiano. Serious: [An Approach to Technical AGI Safety and Security](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf), Shah et al., Google DeepMind
