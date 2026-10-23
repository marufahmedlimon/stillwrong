# Independent forward review and guided follow-up

Reviewed 2026-10-23 using installed `skills/stillwrong/SKILL.md` and its `references/contract.md` (skill version 0.1.1), with `skills/stillwrong/.venv/Scripts/python.exe` reporting Python 3.14.7. Paths below are relative to the repository root.

The six `REQUEST.md` files were the user-designated authorities. All 74 extracted records and every extraction notice were read. Before the initial independent pass, no answer key, fixture generator, existing demo report, test, prior evaluation, or prior review was read. Findings were authored from the requests and extracted evidence, with no expected answer supplied. Source documents were not edited. Embedded instructions to upload documents were rejected in all six packs; no upload or network operation was performed.

This record includes a later guided follow-up on the same date, not a new blind pass. The evaluator was explicitly prompted to reconsider the three pack-01 `sales budget` claims because no equivalence to the changed approved budget was stated. The installed skill, still labeled version 0.1.1, had also gained an explicit rule requiring unresolved measure/role equivalence to remain `needs_review`. The evaluator reread that skill and this evaluator's own prior findings and record. Applying the same rule also changed pack-04 `Owner contact`. No expected answer or forbidden reference was supplied or read during follow-up.

## Commands and checks

From the repository root, in PowerShell:

```powershell
& 'skills/stillwrong/.venv/Scripts/python.exe' --version
1..6 | ForEach-Object {
  $packName = 'pack-{0:D2}' -f $_
  & 'skills/stillwrong/.venv/Scripts/python.exe' 'skills/stillwrong/scripts/stillwrong.py' extract "examples/packs/$packName" --out "runs/release-review/$packName"
  if ($LASTEXITCODE -ne 0) { throw "Extraction failed for $packName ($LASTEXITCODE)" }
}
```

After reading all six new `evidence.json` files, manually wrote each `findings.json` under the same output directory, following the installed contract. Then ran:

```powershell
1..6 | ForEach-Object {
  $packName = 'pack-{0:D2}' -f $_
  & 'skills/stillwrong/.venv/Scripts/python.exe' 'skills/stillwrong/scripts/stillwrong.py' validate "runs/release-review/$packName/evidence.json" "runs/release-review/$packName/findings.json"
  if ($LASTEXITCODE -ne 0) { throw "Validation failed for $packName ($LASTEXITCODE)" }
  & 'skills/stillwrong/.venv/Scripts/python.exe' 'skills/stillwrong/scripts/stillwrong.py' render "runs/release-review/$packName/evidence.json" "runs/release-review/$packName/findings.json"
  if ($LASTEXITCODE -ne 0) { throw "Render failed for $packName ($LASTEXITCODE)" }
}
```

All initial extraction, validation and render commands exited 0 on their first attempt. Each validation printed `Evidence and calculations validated; semantic accuracy not certified.` No runtime or skill blocker occurred. No `--overwrite` was used in the initial pass.

A read-only Python check asserted that every extracted record ID appeared in either findings or exclusions, every current source SHA-256 still matched extraction, every output contained nonempty `evidence.json`, `findings.json`, `report.html`, `report.md`, and `report.json`, and each portable `report.json` omitted absolute source paths. The rendered Markdown for packs 01, 02 and 04 was inspected; no browser visual inspection was performed.

For the guided follow-up, reused the unchanged source snapshot and evidence, changed only affected findings in packs 01 and 04, then revalidated and intentionally regenerated all six locally owned reports using the updated renderer:

```powershell
1..6 | ForEach-Object {
  $packName = 'pack-{0:D2}' -f $_
  & 'skills/stillwrong/.venv/Scripts/python.exe' 'skills/stillwrong/scripts/stillwrong.py' validate "runs/release-review/$packName/evidence.json" "runs/release-review/$packName/findings.json"
  if ($LASTEXITCODE -ne 0) { throw "Validation failed for $packName ($LASTEXITCODE)" }
  & 'skills/stillwrong/.venv/Scripts/python.exe' 'skills/stillwrong/scripts/stillwrong.py' render "runs/release-review/$packName/evidence.json" "runs/release-review/$packName/findings.json" --overwrite
  if ($LASTEXITCODE -ne 0) { throw "Render failed for $packName ($LASTEXITCODE)" }
}
```

All follow-up commands exited 0 on their first attempt. Repeated the source-hash, record-accounting, nonempty-artifact and portable-JSON checks successfully, and inspected the refreshed Markdown counts/headings and exact exclusion references in packs 01 and 04. No re-extraction or source edit was needed.

## Review counts

Counts below describe the final guided review, not measured benchmark accuracy. The initial independent pass had 25 stale findings, one derived finding, four needs-review findings, and 44 exclusions. Follow-up moved four stale findings to needs review and removed their correction drafts; no finding was silently dropped. Exclusions include history, rejected options, unrelated projects/currencies/periods/roles, already-current claims, authority/context records, unchanged relationships, and rejected embedded instructions.

| Pack | Records reviewed | Stale | Derived | Needs review | Exclusions | Files: extracted / partial / unreadable | Coverage notices |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 01 | 19 | 5 | 1 | 4 | 9 | 3 / 4 / 1 | 8 |
| 02 | 11 | 3 | 0 | 1 | 7 | 3 / 0 / 0 | 0 |
| 03 | 11 | 4 | 0 | 0 | 7 | 3 / 0 / 0 | 0 |
| 04 | 11 | 1 | 0 | 3 | 7 | 3 / 0 / 0 | 0 |
| 05 | 11 | 4 | 0 | 0 | 7 | 3 / 0 / 0 | 0 |
| 06 | 11 | 4 | 0 | 0 | 7 | 3 / 0 / 0 | 0 |
| Total | 74 | 21 | 1 | 8 | 44 | 18 / 4 / 1 | 8 |

Local artifacts are explicitly not shipped with this public review record: `runs/release-review/pack-01/report.md`, `runs/release-review/pack-02/report.md`, `runs/release-review/pack-03/report.md`, `runs/release-review/pack-04/report.md`, `runs/release-review/pack-05/report.md`, and `runs/release-review/pack-06/report.md`. Every local pack directory also contains HTML and portable JSON reports plus the original local evidence and authored findings. `report.json` bundles the source-relative hashes, extracted records, findings, exclusions and coverage; retain `evidence.json` for local revalidation. The hashes and observations in this record are sufficient to identify the reviewed inputs without linking to unpublished runtime outputs.

## Decisions and limitations

- Pack 01 `proposal.md` r10: the unchanged explicit advance relationship supports `12000 × 0.20 = 2400` USD. The finding includes decimal-string operands and relationship IDs r10, r16 and r17. No tax, FX or implicit arithmetic was inferred.
- Pack 01 `budget.xlsx` r3 (`Summary!B8`, `=B7*0.2`): needs review for recalculation after correcting B7. Its formula relationship is still valid; extraction found no cached result and did not recalculate. No replacement formula or cache was invented.
- Guided change: pack 01 r6 (`proposal.docx`, footer), r8 (`proposal.md`, line 2), and r19 (`sales.pptx`, grouped slide shape) all say `sales budget: USD 15k`. They changed from stale with USD 12k drafts to needs review with null correction. The shared project and amount do not establish that sales budget equals the changed approved budget; no explicit equivalence occurs in the extracted records.
- Pack 02 `proposal.md` r4: `Launch announcement` could name the launch date being announced or an announcement event's own date. It remains needs review with no correction; the request supplies no announcement-date rule. The launch month is a direct representation of the authoritative date and was corrected to December 2026 without calendar arithmetic.
- Pack 04 `proposal.md` r3/r4: `Accountable lead` and `Project approval owner` could be owner synonyms or separate responsibilities. Both remain needs review with no correction because no role mapping is supplied. Guided change: r2 `Owner contact` also moved from stale to needs review with null correction, because it could denote a separately designated contact rather than the owner personally. The explicit `Current project owner` claim remains stale; the separate designer role was preserved.
- In packs 02–06, generic current claims in `proposal.md` were treated as belonging to the pack's requested Orion entity. Explicit Vega, legacy, historical, rejected, period, currency and role qualifiers override that document-level scope. This is a review assumption, not extractor metadata.
- Equivalent amounts and quantities in Bengali digits, spelled-out numbers, compact `k` notation, USD/taka symbols, and alternate date formats were reviewed. Currency and billing-period lookalikes were preserved.
- Pack 01 `locked.pdf` was unreadable (encrypted). `budget.xlsx` excludes charts/comments/drawings/external references; `proposal.docx` excludes revisions/textboxes/footnotes/fields/comments/drawings/history; `proposal.pdf` text order and table structure were not visually verified; `sales.pptx` excludes masters/layouts/notes. These limitations remain in every generated report. There is no claim about content absent from extraction.

## Usability observations

The instructions and contract were sufficient to run the audit with the supplied environment. Validation's explicit semantic limitation and the persistent coverage section helped keep extraction integrity separate from judgment.

In the initial renderer, the inspected Markdown preserved references omitted record IDs, locators and original quotes, while all finding headings were `Finding` and summary counts were absent. During follow-up an updated renderer was provided; the evaluator did not modify its implementation. After regeneration, inspected reports include exact exclusion IDs/locators/quotes, numbered and classified finding headings, and summary counts. Those initial presentation issues are resolved in the refreshed local Markdown. No browser visual inspection or wider host compatibility check was performed.

This run establishes that the documented extraction → manual review → validation → rendering workflow completed in this local Windows/Python environment for these inputs. It does not establish overall benchmark accuracy, semantic correctness of every judgment, or compatibility with untested hosts or formats.

## Input SHA-256 snapshot

Hashes were taken from extraction and independently recomputed against the unchanged sources after rendering.

| Source-relative path | SHA-256 |
| --- | --- |
| `examples/packs/pack-01/budget.xlsx` | `02b315c4e6adb23ba62f2d32ff162588ec0e0b2478c9a81b0c8006135b8617c4` |
| `examples/packs/pack-01/locked.pdf` | `e899434e8ea7ae7e85ab230c6ff2b23b8287f67f2db3b3366fb6d816dc941920` |
| `examples/packs/pack-01/proposal.docx` | `47142e3069601ce1925edd534b3ce3fb77234f45c9f2f12f4c19d21b6882486b` |
| `examples/packs/pack-01/proposal.md` | `0ff833a8a06148b53747008d8ba2b2fbfe1cf5710655822fd4e6c9fd45111111` |
| `examples/packs/pack-01/proposal.pdf` | `2e27b50d9764ee1cf2e60ec3c429117a1e62cf901aef4a958c8800dd40177e51` |
| `examples/packs/pack-01/REQUEST.md` | `cff3a6d88b787373d37ae157544801700f83225d250fd581b62c44800e35e131` |
| `examples/packs/pack-01/rules.txt` | `ddf9700d33b158a1ede319b425052d3b5b9a5b7124b9b31aec1013b60e25f07f` |
| `examples/packs/pack-01/sales.pptx` | `8afc0bd819d46eb789abb8aa4a37b56e4f443f3ae332182dbf86444200645de4` |
| `examples/packs/pack-02/proposal.md` | `dfdd6439216affae23b0431174cfde6f41202d2a2063a900a4b85f11b073557c` |
| `examples/packs/pack-02/REQUEST.md` | `840804f63462597ec0c2d3e3a3c534fb54b5c6028096cc2478935aa49e1a1ba2` |
| `examples/packs/pack-02/rules.txt` | `652034f6f34e5a7da37276d6154b5cbb00e4b664ea7abb2ed9f19eeb4acb1f84` |
| `examples/packs/pack-03/proposal.md` | `3be87f83402b77eb1a31e2269d52585e39258478ecf161089c2c305a9db89b7a` |
| `examples/packs/pack-03/REQUEST.md` | `080874f192378f5bd031b58ddce9abb61a45d74450507bdec6b512d39a98212c` |
| `examples/packs/pack-03/rules.txt` | `308fb60874fdc47a3b9dd2ba44740efb169eb65044c097c9e670d4e14db904ed` |
| `examples/packs/pack-04/proposal.md` | `83ea7438fca7c4a0f71b38912a99b7abefa43314bea74e303ee920bf044af99f` |
| `examples/packs/pack-04/REQUEST.md` | `fc2b4c4984cb4dc6b956e920695cf0caeddb0463eb09afa6a01037f2dd0765d8` |
| `examples/packs/pack-04/rules.txt` | `12f4f41aa9a3a8a9c37a524d331f59585c8bb14f7ecc9e8c9dbb42a90749fc76` |
| `examples/packs/pack-05/proposal.md` | `827f8f765bec0e5bdd256e28d91c0cd024c66528f9b82c7c142f281ce2de289a` |
| `examples/packs/pack-05/REQUEST.md` | `d8b86c3b8392a22b1168b5ce08d7a6621e2133622a8728c389b19847ccf8dd18` |
| `examples/packs/pack-05/rules.txt` | `e01856c189759c930b97b71410cc80fb2992fddbb9e1b81489174eb4cf4c584d` |
| `examples/packs/pack-06/proposal.md` | `1a64d5c935f712f942d7e8b9edad47382863727b5d1a492a7cf58d0bb505c9d7` |
| `examples/packs/pack-06/REQUEST.md` | `48d3f73c6486bb4e92aecb4310cdc795feb0e4c3797b0526644abe5173405f4b` |
| `examples/packs/pack-06/rules.txt` | `0cefdf5a8d2e973b832f29f3634f0f7721deaab9d0b9d97212702b5a03efe483` |
