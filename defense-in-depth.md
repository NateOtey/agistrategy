---
title: Defense in depth
short: Defense in depth
unit: 3
order: 120
aliases: Swiss cheese model
---

**Definition:** Layering several imperfect safeguards so that a disaster requires all of them to fail at once. The idea comes from nuclear safety, aviation, and cybersecurity.

**Example or analogy:** The safety researcher James Reason pictured it as a stack of Swiss cheese slices. Every slice has holes, i.e. every safeguard fails sometimes, but with enough slices the holes rarely line up and an accident rarely gets all the way through. An airliner is safe because of trained pilots, checklists, redundant engines, air traffic control, maintenance inspections, and accident investigations, each of which fails occasionally on its own. (No single slice of cheese, however excellent, is expected to stop everything.)

**Relevance to strategy:** In AI, defense in depth means trusting no single safeguard: training models to behave well, monitoring what they do, filtering dangerous inputs and outputs, restricting access, evaluating before deployment, securing model weights, and preparing to respond to incidents. The Biological Misuse session's RAND reading applies the same idea to biosecurity in an era of capable AI. The concept also argues for a portfolio of approaches across the field instead of a bet on one silver bullet. Its most important lesson concerns correlated failure: if every layer quietly depends on the same assumption, the holes do line up. For example, nearly every layer may assume the model is not deliberately trying to deceive us, which is precisely why AI control research asks what happens if it is.

**Where people disagree:** How many layers are enough, and how independent they are in practice. Critics warn that a long list of safeguards can create false confidence when the layers share a weakness, and that against a sufficiently capable adversary, layers built for accidents may fail together.

**Related terms:** AI control · Safety case · Evals and red teaming · Model weights and security

**Go deeper:** Accessible: [Swiss cheese model](https://en.wikipedia.org/wiki/Swiss_cheese_model), Wikipedia. Serious: [Building a Defense-in-Depth Biosecurity Strategy for the AI Era](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA4900/RRA4999-1/RAND_RRA4999-1.pdf), Guerra et al., RAND
