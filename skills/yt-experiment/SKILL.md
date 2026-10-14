---
name: yt-experiment
description: >-
  Design a clean YouTube content or packaging experiment with one hypothesis, controlled variables, success metric, sample caveats, and decision rule. Use for title/thumbnail tests, format changes, hook tests, cadence tests, or series validation.
---

# yt-experiment

## Mission
Replace random changes with interpretable YouTube experiments.

## Required inputs
- what the creator wants to improve
- current baseline or best available evidence
- variable that can be changed

## Optional inputs
- analytics window
- video set
- A/B testing availability

## Workflow
1. Write one falsifiable hypothesis.
2. Choose one primary variable and keep other material variables stable where possible.
3. Define primary and secondary metrics with known limitations.
4. Set observation window or minimum evidence condition without pretending statistical certainty when sample sizes are small.
5. Write decision rules: adopt, retest, reject, inconclusive.
6. Record confounders such as topic strength, traffic source, seasonality, and returning-viewer mix.

## Output contract
Always return these sections in this order:
- Hypothesis
- Test design
- Control vs variant
- Primary metric
- Secondary metrics
- Confounders
- Decision rule
- Experiment log template

## Quality gates
- Do not claim causation from uncontrolled before/after changes.
- Do not overstate statistical significance without actual analysis.

## Interoperability
Works especially well with: `yt-thumbnail-director`, `yt-retention`, `yt-package`, `yt-audit`.

## Failure handling
- If a required input is missing but a useful partial result is still possible, state the assumption and continue with a provisional result.
- If the missing input would materially change the recommendation, ask for that input rather than inventing it.
- Separate **known facts**, **user-provided facts**, and **inference** when the distinction matters.
- Prefer one strong recommendation plus alternatives over a long unranked list.

## Community contribution rule
Any proposed change to this skill should preserve: deterministic output sections, explicit guardrails, no fabricated metrics, and no autonomous publishing by default.
