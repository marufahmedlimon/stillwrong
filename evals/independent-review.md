# Independent forward review: pack-01

Reviewed the installed StillWrong skill and its findings contract, then used its extraction, validation and rendering commands on `examples/packs/pack-01`. Authority was the explicit user instruction: the current Orion-1 approved budget changes from USD 15000 to USD 12000, while the advance remains 20%. Did not read the answer key, fixture builder, tests or existing demo reports. No source documents were edited by this reviewer.

## Result

The workflow was usable without reading implementation code for normal operation. The final independent report contains 5 stale statements, 1 explicitly derived correction, 4 items requiring review, and 7 justified exclusions. These are this reviewer's judgments, not an accuracy score or benchmark result.

- Stale: the spreadsheet current-budget input, DOCX current proposal, Markdown current proposal, Bengali-numeral approved budget, and extracted PDF current proposal statement.
- Derived: the explicitly stated 20% advance changes from USD 3000 to USD 2400 (`12000 * 0.20`).
- Needs review: the unchanged spreadsheet formula requires recalculation, and three statements called a "sales budget" need confirmation that this measure is the same as the approved budget.
- Exclusions preserve last year's facts, Vega's separate budget, a rejected option, an already-current amount, the audit request's old/new explanation, and untrusted external-transmission instructions.

## Coverage

Eight files yielded 20 evidence records. Four files were marked extracted, three partial, and one unreadable. The unreadable file was encrypted `locked.pdf`. Partial coverage disclosed unrecalculated workbook formulas and unreviewed chart/comment/drawing/external-reference content, unverified PDF text order/table structure, and unreviewed slide masters/layouts/speaker notes. The reviewer examined every extracted record. Source-page visual rendering was not independently checked, so findings from the PDF apply to its extracted text only.

## Observed issues and limits

1. **Fixture ambiguity:** "current sales budget" is not explicitly equated with "current approved budget." The old amount matches, but that alone cannot establish scope. The skill correctly permits `needs_review`; this review uses it for all three such statements instead of inventing a correction.
2. **Report wording:** null corrections render as "Needs clarification" even for workbook recalculation. In that case the needed action is recalculation, not a missing user answer. A neutral "No correction proposed; see required review" would fit both cases.
3. **Report presentation:** the authoritative change appears as raw JSON in both Markdown and HTML rather than a short human-readable old-to-new statement. Evidence paths/locators are present, but the report could be easier to scan with grouped counts and labels such as "Needs review."
4. **Snapshot change handling:** first validation rejected changed source hashes. Another lane had regenerated Office archives; fresh extraction showed only three binary hashes changed, with all records and locators identical. The reviewer re-reviewed that comparison and validated the fresh snapshot successfully. This exercised the documented rejection behavior; the reviewer did not bypass it or edit evidence.

## Artifacts and validation

- Final evidence snapshot: `runs/independent-01/refresh/evidence.json`
- Findings: `runs/independent-01/findings.json`
- Reports: `runs/independent-01/refresh/report.html` and `report.md`
- Original superseded extraction: `runs/independent-01/evidence.json` retained for traceability; it must not be used as the final validation snapshot.
- Final validate command completed successfully: "Evidence and calculations validated; semantic accuracy not certified."
- Final render command completed successfully.

This is one forward usability exercise on one supplied example pack. It establishes neither general detection accuracy nor superiority over an ordinary agent prompt.
