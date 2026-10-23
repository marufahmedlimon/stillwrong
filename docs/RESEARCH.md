# Publication research and decisions

Reviewed 23 October 2026. These are reference projects and official documentation,
not endorsements, popularity guarantees or copied implementation sources.

| Primary source | Applied decision |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | A discoverable SKILL.md entry point, with scripts and task-specific resources |
| [obra/superpowers](https://github.com/obra/superpowers) | Explain the problem early; separate installation from verified behavior; provide troubleshooting and contribution paths |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | Publish a complete skill folder that standard skill installers can discover |
| [Agent Skills specification](https://agentskills.io/specification) | Required name/description, lowercase matching folder name, optional author/version metadata |
| [Codex skills](https://learn.chatgpt.com/docs/build-skills) | Local project/personal discovery and repository installer support; do not confuse a local skill with an installed universal plugin |
| [Claude Code skills](https://code.claude.com/docs/en/skills) | Claude-specific directory guidance and reload caveats |
| [GitHub upload docs](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) | Audit the manual-upload payload against 100 files and 25 MiB per-file limits |
| [GitHub private reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository) | Owner enables a private reporting channel after publication; no invented contact email |
| [checkout](https://github.com/actions/checkout) / [setup-python](https://github.com/actions/setup-python) | Current documented v7 actions, read-only job permissions, no persisted checkout credentials |
| [openpyxl formula docs](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html) | Formula source/cache evidence is not recalculation |
| [pypdf extraction docs](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) | Digital text and page references do not establish OCR/visual coverage |

StillWrong does not need a daemon, hosted backend, remote MCP server or new AI API
key. A small portable skill fits this workflow; large multi-skill framework
features were not copied into it.

Novelty remains bounded: change propagation and cross-document QC already exist.
See the related-work links in README.md. This release focuses on usable mixed-file
evidence, guarded output and explicit coverage. Stars and installs are not proof
of accuracy or repeat usefulness.
