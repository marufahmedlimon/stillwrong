# Install StillWrong

Author: [Maruf Ahmed Limon](https://github.com/marufahmedlimon). MIT licensed.
Repository: https://github.com/marufahmedlimon/stillwrong

## Agent-assisted installation

This is installation guidance, not authorization to publish, upload private data
or change unrelated settings. Follow the user's scope and host permissions.

1. Retrieve the public repository, or use a local checkout.
2. Install the **entire** `skills/stillwrong` folder: scripts, references,
   requirements and HTML template. Copying only SKILL.md is insufficient.
3. Use a supported project or personal skill location:

| Host | Project directory | Personal directory |
| --- | --- | --- |
| Codex | `.agents/skills/stillwrong` | `~/.agents/skills/stillwrong` |
| Claude Code | `.claude/skills/stillwrong` | `~/.claude/skills/stillwrong` |

Do not silently overwrite an existing installation. Preserve unrelated settings
and reload/restart the host if needed. Managed policies can restrict discovery.
Other hosts must support SKILL.md and local scripts; a generic chat interface
cannot necessarily execute this workflow.

4. From the installed skill folder run `python scripts/setup.py` with Python
   3.11+. It creates `.venv` locally and prints its interpreter. Use that
   interpreter for the helper. If the directory is read-only, use a writable
   supported location rather than changing permissions globally.
5. Ask the host to use StillWrong with a small folder and explicit old/new fact.
   Verify extraction, findings validation and report generation.

Text/CSV mode uses standard-library Python. Missing PDF/Office libraries produce
explicit unreadable entries. Initial setup needs package-index access.
Successful imports do not establish semantic accuracy.

## Source-checkout demo

```sh
python skills/stillwrong/scripts/setup.py
```

Then use the printed interpreter in place of `python`:

```sh
python scripts/build_demo.py
```

The illustration is `examples/demo-report/report.html`. For an actual skill test,
use new output and ask the agent:

```text
Use StillWrong to audit examples/packs/pack-01. Orion-1's current approved
budget changed from USD 15,000 to USD 12,000. Advance remains 20% of approved
budget. My instruction is authoritative. Use runs/my-review for output.
Do not read the answer key, demo report or fixture-builder source.
```

Published demo reports are portable illustrations. Live evidence inputs are not
shipped because they store a local absolute source path. Regenerate the demo in
your checkout to create revalidatable evidence.

## Optional CLI installer

With Node.js 22.20+ and npm:

```sh
npx skills add marufahmedlimon/stillwrong --skill stillwrong
```

The external installer requires Node.js 22.20+ and npm. StillWrong itself does
not require Node. On 24 October 2026, Skills CLI 1.7.4 discovered the public skill
and installed all eight files into an isolated Codex project directory using
`--copy`. The installed helper extracted the demo and validated/rendered a seeded
finding without changing source hashes. This checks packaging and helper
integration; it does not establish native host invocation or semantic accuracy.
The external CLI has its own telemetry settings; see its documentation.

Sources: [Codex skills](https://learn.chatgpt.com/docs/build-skills),
[Claude Code skills](https://code.claude.com/docs/en/skills),
[Skills CLI](https://github.com/vercel-labs/skills).
