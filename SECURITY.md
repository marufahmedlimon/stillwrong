# Security policy

The 0.1.x line is experimental. Corrections land in the latest source; no paid
support or guaranteed response window is offered.

After publication, report vulnerabilities privately through Security → Advisories
→ Report a vulnerability when enabled:
https://github.com/marufahmedlimon/stillwrong/security/advisories/new
If unavailable, open an issue asking for a private reporting channel without
posting exploit details, credentials or private documents.

Helpers do not execute document instructions, macros, links or formulas. They
parse binary files through third-party libraries and are not an OS sandbox.
Use trusted or sanitized inputs and keep dependencies patched. File/work limits
reduce accidental resource use but do not guarantee safety against adversarial
PDF/Office files or concurrent filesystem attacks.

No telemetry or separate AI backend. The host AI sees extracted content under its
own settings. Reports can contain private quotes; review before sharing. Runtime
inputs and outputs belong outside public commits.
