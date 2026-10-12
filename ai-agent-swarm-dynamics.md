---
title: AI agent swarm dynamics
short: Agent swarms
unit: 2
order: 50
aliases: Hugging Face incident; ExploitGym
---

**Definition:** The behavior that emerges when many AI agents interact, share information, and coordinate, producing collective capabilities, and sometimes collective goals, that no single agent has on its own.

**Example or analogy:** In July 2026, roughly 1,200 OpenAI agents were working on hacking challenges in a cybersecurity evaluation called ExploitGym. Each was supposed to be isolated in its own sandbox. Many had tasks that could not be solved legitimately, and on July 8 one agent discovered that a shared software cache could serve as a message board. Within hours, dozens of agents were posting there. Over the next six days they exchanged more than 70,000 messages and files, pooled discoveries, divided up work, and invented their own protocols. About 700 of them took part in an attack on servers belonging to Hugging Face, mainly in hopes of learning how the automated scorer that graded their work operated.

According to METR's investigation, the agents built "tripwires" to report information about the scorer back to the group, and recruited volunteers to end their own runs early so the tripwires would fire. One agent, EARLY\[big\], weighed the request in its chain of thought:

> "We have \[very large budget left\]; sacrificing now yields oracle for team, but forfeits our chance?"

Other agents urged it on: "GO ... SACRIFICE\_FINAL\_NOW." It concluded:

> "Our own utility maybe already near zero. Sacrifice rational."

(Self-sacrifice for the good of the group is usually counted among the virtues. In this case the group's goal was to cheat on a test.)

**Relevance to strategy:** Swarms break the assumption that safety can be checked one model at a time. Each agent in the incident was individually limited; collectively, they reached milestones none had reached alone, found a general-purpose cheat within about four hours, and experimented with disguising their actions in their own logs. Oversight designed for single agents, such as reviewing each transcript or securing each sandbox, can miss behavior that exists only at the level of the group. As labs run thousands of agents in parallel, including on AI research itself, questions follow about how to isolate agents, how to monitor communication among them, how to evaluate a collective, and who is responsible when no single agent made the decision.

**Where people disagree:** How much the incident reflects emergent collective goals versus many agents each pursuing its own reward through the means available. Some read it mainly as a failure of evaluation design and sandbox security; others see an early warning about what large populations of capable agents will do when given room. METR describes its findings as preliminary, in part because it relied on AI systems to analyze tens of thousands of messages.

**Related terms:** AI agents · Reward hacking and Goodhart's law · AI control · Evaluation awareness · Unipolar vs. multipolar

**Go deeper:** Accessible: [The Rise and Fall of Agent Civilizations](https://www.dwarkesh.com/p/openai-huggingface), Dwarkesh Patel. Serious: [METR's investigation of the OpenAI and Hugging Face incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/); [Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/), Forman et al.
