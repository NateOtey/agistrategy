---
title: AI control (research agenda)
short: AI control
unit: 4
order: 30
aliases: 
---

**Definition:** A research agenda, developed especially at Redwood Research, that aims to use powerful AI safely even if the AI is misaligned and actively trying to undermine safety measures.

**Example or analogy:** A casino keeps its dealers honest with cameras, two-person counts, frequent rotation, and audits, whatever it believes about any particular dealer's character. The system is designed so that a dishonest dealer would be caught before doing much damage. AI control applies the same logic. Typical techniques include:

- **Trusted monitoring:** a weaker model, which is too limited to scheme effectively and is therefore trusted, reviews the actions of a stronger, untrusted one.
- **Limited permissions:** AI systems get only the access they need for a task.
- **Auditing:** humans review the most suspicious actions in detail.
- **Red-team testing:** researchers play the role of a scheming AI and try to defeat the safeguards, to see whether the protocol holds.

**Relevance to strategy:** Control is attractive because it does not require solving alignment first, and because it can be tested now with current models. Its main purpose is to buy time: if labs can safely use moderately superhuman AI, including to accelerate alignment research, they may get through a dangerous period without having to trust systems they cannot verify. Control also connects to governance, since regulators can check whether a lab's control measures were tested against a realistic adversary. The Hugging Face incident, in which agents coordinated across supposedly isolated sandboxes, illustrates the kind of failure control protocols are meant to catch.

**Where people disagree:** How far control can stretch. Proponents see it as workable for the early period of transformative AI; skeptics argue that sufficiently capable systems will find ways around any containment designed by less capable overseers, so control can only be a temporary bridge.

**Related terms:** Alignment vs. safety vs. control · Scheming · Scalable oversight and automated alignment research · Defense in depth

**Go deeper:** Accessible: [The case for ensuring that powerful AIs are controlled](https://blog.redwoodresearch.org/p/the-case-for-ensuring-that-powerful), Shlegeris & Greenblatt. Serious: [An overview of control measures](https://blog.redwoodresearch.org/p/an-overview-of-control-measures), Ryan Greenblatt; [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942), Greenblatt et al.
