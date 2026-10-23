"""Explicit public-source allowlist; never sweep the development workspace."""
from pathlib import Path
import stat

FILES = '''README.md INSTALL.md LICENSE CHANGELOG.md CONTRIBUTING.md SECURITY.md .gitignore .gitattributes
.github/workflows/ci.yml .github/ISSUE_TEMPLATE/bug_report.yml .github/pull_request_template.md
skills/stillwrong/SKILL.md skills/stillwrong/LICENSE skills/stillwrong/requirements.txt
skills/stillwrong/agents/openai.yaml skills/stillwrong/references/contract.md
skills/stillwrong/assets/report.html skills/stillwrong/scripts/stillwrong.py skills/stillwrong/scripts/setup.py
scripts/build_demo.py scripts/score_eval.py scripts/release_manifest.py scripts/check_release.py scripts/package_release.py
tests/test_stillwrong.py tests/test_hardening.py tests/test_release.py
docs/hero.svg docs/report-preview.png docs/RESEARCH.md
evals/RESULTS.md evals/PROTOCOL.md evals/independent-review.md evals/release-forward-review.md
examples/answer-key.json
examples/demo-report/report.html examples/demo-report/report.md examples/demo-report/report.json'''.split()
for n in range(1,7):
    FILES += [f'examples/packs/pack-{n:02}/{name}' for name in ['REQUEST.md','proposal.md','rules.txt']]
FILES += [f'examples/packs/pack-01/{name}' for name in ['proposal.docx','proposal.pdf','sales.pptx','budget.xlsx','locked.pdf']]

def paths(root):
    root=Path(root).resolve()
    for rel in sorted(FILES):
        path=root/rel
        for part in [path, *path.parents]:
            if part == root: break
            if part.is_symlink() or (part.exists() and getattr(part.lstat(),'st_file_attributes',0) & 0x400):
                raise ValueError(f'Linked release entry rejected: {rel}')
        if not path.resolve().is_relative_to(root) or not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
            raise ValueError(f'Missing/nonregular release file: {rel}')
        yield rel,path
