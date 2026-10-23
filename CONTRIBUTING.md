# Contributing

Maintainer: [Maruf Ahmed Limon](https://github.com/marufahmedlimon).

Start with a reproducible problem and a synthetic document. Never include client
files, secrets or personal data in public issues. Describe the change, authority,
expected finding and actual behavior. Separate extraction defects from host-model
judgment errors.

Use Python 3.11+, isolated setup, then `python -m unittest discover -s tests -v`
with that interpreter. Add meaningful regressions, preserve originals and disclose
unsupported content. Accuracy claims require reproducible evaluations.

Run `python scripts/check_release.py` before packaging. Submit focused pull
requests explaining the problem, resulting behavior and executed validation.
Contributions use MIT. Security reports follow SECURITY.md.
