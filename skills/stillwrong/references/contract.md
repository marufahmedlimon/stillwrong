# Findings contract (version 1)

Write UTF-8 JSON, not a code fence:

```json
{
  "schema_version": 1,
  "change": {"entity":"Orion", "fact":"approved budget", "old":"USD 15000", "new":"USD 12000", "authority":"User explicitly approved USD 12000 for the current Orion project"},
  "findings": [
    {"record_id":"r1", "quote":"Budget: USD 15000", "classification":"stale", "reason":"Current Orion proposal retains superseded budget", "correction":"Budget: USD 12000", "authority":"User instruction"}
  ],
  "exclusions": [{"record_id":"r2", "reason":"Historical decision; remains accurate"}]
}
```

Every finding needs an exact extracted record quote (full text or nonempty substring), reason and authority. `stale` and `derived` require a nonempty correction. `needs_review` may have null correction. Use record IDs emitted by extraction; never make up locators. Exclusions require record_id and reason.

For derived arithmetic add `calculation`: `{"op":"multiply","operands":["12000","0.20"],"result":"2400","relationship_record_ids":["r3"]}`. Allowed operations: add, subtract (two operands), multiply, divide (two operands). Cite records stating the relationship and explain how the new input follows from the change. Calculations use decimal arithmetic, not currency conversion. Unsupported date arithmetic, complex formulas or implicit relationships must be needs_review. Evidence integrity checks cannot establish that the cited relationship is semantically applicable.

Use decimal **strings**, not floating-point JSON numbers. The helper checks exact rational arithmetic; a rounded approximation such as 1/3 cannot be presented as an exact result. There are 1–50 operands, each at most 128 characters and exponent magnitude 100. Missing/invalid evidence, duplicate findings for the same quote and invalid correction types are rejected.

`report.json` is the portable output bundle: version, change, findings, exclusions, source-relative file hashes/coverage and extracted records. It intentionally omits the local absolute input path. It is a report, not a live extraction input. Keep the original `evidence.json` for local revalidation. Existing reports require explicit `render ... --overwrite`; source overlap and linked destinations are always rejected.

Coverage is about extraction only, not proof of semantic review. Extraction IDs and hashes identify one snapshot. Do not change evidence.json; validate checks evidence against fresh extraction of the source snapshot. If sources changed, extract and review again.

PDF locations are page plus quote; DOCX locations are paragraph/table/header/footer paths; PPTX locations are slide/shape/table paths; XLSX locations are sheet/cell, with formula source and potentially stale cache. Embedded visuals/revisions are not checked. All findings are proposals for human review.
