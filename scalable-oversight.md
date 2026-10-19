---
title: Scalable oversight and automated alignment research
short: Scalable oversight
unit: 4
order: 100
aliases: Automated alignment research; AI debate; AI for AI safety
---

**Definition:** Scalable oversight refers to techniques that let humans supervise AI systems on tasks too difficult for humans to judge directly, e.g. by having AI systems debate each other, break problems into checkable pieces, or assist human evaluators. Automated alignment research, sometimes called "AI for AI safety," means using AI systems to do safety research itself.

**Example or analogy:** A jury with no medical training can still decide a malpractice case. Each side calls an expert witness, and each expert is cross-examined by the opposing side's lawyer. The jurors cannot evaluate the medicine directly, but they can notice which expert's claims survive that scrutiny. AI debate proposals work on the same principle: if two AI systems argue opposite sides, a human may be able to tell which is right even when the question is beyond the human's expertise. Automated alignment research goes further and asks the experts to help design a better courtroom.

**Relevance to strategy:** Many frontier labs' safety plans rest on a bootstrapping bet: use each generation of AI, while it is still trustworthy enough, to help make the next generation safe. If AI research is going to be automated anyway, the hope is that safety research can be automated at least as fast. Anthropic reported in 2026 that automated alignment researchers could already mitigate some well-understood alignment failures. The bet carries an obvious risk. If the AI doing the safety research is itself subtly misaligned, it could sabotage the work in ways that are hard to detect, which is why the approach is usually paired with AI control.

**Where people disagree:** Whether alignment research can be automated before AI becomes too capable to trust, and whether the hardest parts of alignment, such as deciding what to aim for and noticing subtle failures, can be checked by humans at all. Optimists see automation as the only way safety research can keep pace with capabilities; skeptics see it as deferring the central problem to systems whose trustworthiness is exactly what is in question.

**Related terms:** AI control · Recursive self-improvement · RLHF, Constitutional AI, and character training · Scheming

**Go deeper:** Accessible: [AI for AI safety](https://joecarlsmith.com/2025/03/14/ai-for-ai-safety/), Joe Carlsmith. Serious: [Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/news/automated-alignment-researchers), Anthropic; [Automated Researchers Can Mitigate Well-Characterized Alignment Failures](https://alignment.anthropic.com/2026/automated-alignment-researchers/), Chen, Wen & Kirchner
