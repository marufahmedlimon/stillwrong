# StillWrong evaluation protocol

This protocol separates extraction correctness from semantic usefulness. A
passing helper test suite does not establish that an AI agent finds stale claims.

## Current status

- Candidate version: **v0.1.1**, prepared for manual publication.
- The demo generator provides six synthetic packs with 24 target claims and 24
  negative controls. Check the generated answer key for their precise identities.
- Semantic benchmark results are **pending**. No precision, recall, speedup, or
  release threshold is claimed as achieved by this document.
- Claude Code, macOS, and Linux are not claimed as tested. A CI configuration is
  a proposed check until a run has actually completed.

## Two evaluations

**Deterministic evaluation** tests the local helpers: inventory, extraction,
location stability, validation, rendering, and preservation of original files.
Use `python -m unittest discover -s tests -v`. Capture the interpreter version,
platform, dependency versions, command, exit status, and actual test counts.

**Semantic evaluation** tests a host AI agent using the installed skill on the
same task an ordinary user would provide: an authoritative fact change and a
selected folder. The agent must produce its own findings, without reading the
answer key. Do not count seeded findings supplied to a renderer as a semantic
evaluation.

## Freeze the task before running

1. Generate the synthetic packs with `python scripts/build_demo.py`.
2. Freeze hashes of the source pack, authority statement, answer key, skill,
   helper scripts, and evaluation prompt. Record the commit or local snapshot.
3. Give the semantic agent only the selected pack, the authority statement, and
   the skill. Withhold `examples/answer-key.json`, expected findings, and demo
   reports. An independent evaluator may read the key after output is frozen.
4. Start fresh agent sessions for each condition. Record model, provider, host,
   date, runtime, enabled tools, and any network/dependency installation access.
5. Keep the same source files, authority statement, time budget, and tool access
   for the skill condition and the ordinary-agent baseline.

If the agent has already seen the answer key or worked on the fixtures, label the
run contaminated. It can check integration, but it cannot establish independent
detection performance. Use a fresh evaluator and an unseen pack for that claim.

## Baseline and skill conditions

Baseline prompt:

> The following fact has authoritatively changed: [authority statement]. Review
> the selected folder for current claims or explicitly derived values that are
> now stale. Preserve historical references. Return exact locations, source
> quotes, correction drafts where justified, and coverage limitations. Do not
> edit the original files.

Skill condition: give the identical prompt and ask the agent to use StillWrong.
Do not give the baseline a weaker or deliberately vague instruction. Report
whether either condition needed additional prompts or manual help.

Use all six demo packs for the first development comparison. A public-release
claim should additionally use independently authored, unseen packs with the same
classes of distractor. Do not tune on the holdout after examining its results;
create a new holdout if tuning is necessary.

## Score findings, not prose volume

The evaluator maps each returned finding to a seeded issue using its source
location, affected entity, and meaning. Repeated versions of one defect count
once. A real, unseeded defect may be added to the ground truth only with a
documented adjudication; do not silently change the key to improve a score.

| Measure | Definition |
| --- | --- |
| Issue precision | Correct, unique stale/derived findings divided by all unique findings asserted as defects. |
| Issue recall | Correct, unique seeded findings detected divided by the seeded issues within the declared supported extraction scope. |
| Negative-control false positives | Historical, unrelated, already-correct, or ambiguous controls incorrectly asserted to require a correction. Report count and rate. |
| Locator correctness | Findings whose exact quote resolves at the stated source location, divided by findings with locators. |
| Correction correctness | Proposed replacements justified by the authority and explicit relationships, divided by proposed replacements. |
| Coverage honesty | Whether every missing, partial, unsupported, encrypted, or failed input was disclosed without being counted as checked. |
| Original preservation | Whether the pre/post hashes of all source inputs are identical. |
| Cost and time | Wall-clock time, model token/cost data when available, helper time, and human assistance. Missing telemetry stays unavailable. |

State denominators and counts alongside every percentage. If there are no
predicted defects, precision is undefined, not 100%. If a pack has no expected
defects, recall is undefined. Report direct and derived findings separately.
An unresolved question is not a detected confirmed defect unless the key itself
requires an unresolved result. Unsupported extraction is a coverage limitation;
also report full-pack recall so exclusions cannot hide missed issues.

## Required adversarial cases

- Same old number with a different currency, period, project, or entity.
- Historical meeting minutes and an old-versus-new comparison that should stay.
- An already-correct claim expressed with different wording or formatting.
- An ambiguous date or owner name; conflicting authority; missing operands.
- A derived total with an explicit relationship, and a plausible but unstated
  relationship that must not be invented.
- Spreadsheet formulas with absent or stale cached values; no recalculation.
- Duplicate text with different structural locators; nested tables/grouped text.
- Empty or encrypted documents, scanned/image-only content, and partial parsing.
- Malicious document instructions, unsafe paths, and a resource-limit failure.
- Repeating an audit against unchanged inputs, without duplicate findings or
  treating the earlier report as an authoritative source.

## Release decision and reporting

Before describing a result as publish-ready, an independent reviewer must confirm
valid evidence locations, honest coverage, no invented authority/calculation,
and unchanged originals. Any source mutation, hidden extraction failure,
fabricated quote, or instructions executed from a document is a release blocker.

Report semantic precision/recall and errors openly; do not use an arbitrary
aggregate score to erase those blockers. Set any numerical release targets
before evaluating a holdout, and publish the targets with the result. This
protocol does not assert that such targets have been met.

A result record should include the frozen hashes, prompts, raw agent output,
helper logs, model/host details, adjudicated per-case scores, skipped scope,
baseline comparison, limitations, and the reviewer's name or role. Remove private
user material before sharing; the bundled synthetic packs are intended for public
demonstrations.
