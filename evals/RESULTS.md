# Verification record — v0.1.1

Executed locally on Windows, Python 3.14.7, 23 October 2026.

## Helpers and packaging

- `python -m unittest discover -s tests -v`: **39 tests collected; 38 passed,
  1 skipped**. Windows did not permit the test process to create a symlink;
  the real-link regression is not counted as passed.
- Earlier prototype tests were expanded with meaningful publication-audit
  regressions: single-source report overwrite, directory overlap, explicit
  overwrite, Markdown fence injection, missing caches, stable array formulas,
  empty files, pruned caches, inventory/text/dimension limits, decimal input
  bounds, exact repeating-division rejection and private-file exclusion.
- Skill Creator `quick_validate.py`: passed. Python compile checks passed.
- Isolated setup completed; `pip check`: no broken requirements. This is a
  dependency consistency check, not a vulnerability certification.
- A copied complete skill directory successfully extracted a pack and rendered
  reports using its relative HTML template. This tests file packaging, not
  native Codex/Claude discovery or remote installation.
- Chromium visual/interaction QA: 1440×1200 and 390×844 viewports had no horizontal
  overflow; the Derived filter selected the expected one illustrative finding.
  Both screenshots were visually inspected. README includes the desktop preview.
- Release tooling uses an explicit allowlist, validates local links, rejects
  owner placeholders/local paths and builds a checksum manifest. Archive members
  are checked against the allowlist; runtime environments/private runs are omitted.

## Semantic review

Public packaging update: all public documentation and demo text is now English.
Numeric Unicode tests remain in escaped source literals. Fixture text was localized
after the historical reviews below; those reviews describe the earlier snapshots,
not a fresh semantic benchmark on the English-only fixtures.

Six packs contain 24 labelled target statements and 24 negative controls. Extra
Office/PDF instances are separate from that count. A target can legitimately
require clarification rather than a confirmed stale verdict.

The [prototype review](independent-review.md) found the distinction between a
sales budget and an approved budget; the illustration was corrected to preserve
that uncertainty. It also caught snapshot changes during fixture regeneration.

The [new six-pack independent review](release-forward-review.md) records the
reviewer's actual findings and limits without access to the answer key. No
ordinary-agent baseline, Claude Code comparison, repeated-run estimate or broad
precision/recall claim follows from that exercise.

`score_eval.py` is only a labelled-record **target coverage** aid. It accepts
needs_review and does not assess the correctness of the verdict or replacement.
Use the [protocol](PROTOCOL.md) and independent adjudication for those claims.

## Public-source verification — 24 October 2026

Public source commit: `890c10c7c32d6dbf57904aaf80b828fc1098167c`.
This record describes the published code before the documentation polish.

- [All six CI jobs](https://github.com/marufahmedlimon/stillwrong/actions/runs/40004290693) completed successfully: Ubuntu, Windows and
  macOS, each with Python 3.11 and 3.12. Dependency installation, demo
  generation, deterministic tests and release checks passed in every job.
- A downloaded public snapshot passed the release checker and the local
  39-test suite: 38 passed, one real-symlink test skipped on this Windows
  process. This is separate from the six GitHub jobs.
- Skills CLI 1.7.4 discovered StillWrong from the public GitHub URL and
  installed the complete eight-file skill into an isolated project using
  `--agent codex --copy --yes`, with CLI telemetry disabled. Installed file
  hashes matched the published skill. No global installation was changed.
- The installed helper extracted 19 records from the mixed-format sample,
  validated a deliberately seeded finding, and produced HTML, Markdown and
  JSON. All eight sample-file hashes stayed unchanged. The seeded finding
  is an integration check, not independent detection evidence.
- All 62 expected source files were present. The only package mismatch was
  missing Markdown headings in the manually entered pull request template;
  the prepared polish restores that template and refreshes checksums.

## Still unverified

- Native Codex/Claude Code discovery, invocation and full host comparison.
- Semantic release targets (95% precision / 90% recall) on an unseen holdout.
- Adversarial binary-document safety: parsing libraries are not an OS sandbox.

The package is an **experimental open-source release**, with these
limits disclosed. No guarantee of perfect detection, virality or zero defects.
