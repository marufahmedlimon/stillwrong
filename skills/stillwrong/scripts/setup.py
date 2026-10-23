"""Create an isolated runtime. No global packages are modified."""
import pathlib, subprocess, sys, venv

root = pathlib.Path(__file__).resolve().parent.parent
target = root / '.venv'
if target.is_symlink() or (target.exists() and getattr(target.lstat(), 'st_file_attributes', 0) & 0x400):
    raise SystemExit('Refusing a linked runtime directory')
if sys.version_info < (3, 11):
    raise SystemExit('Python 3.11+ required')
venv.EnvBuilder(with_pip=True).create(target)
python = target / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
subprocess.run([str(python), '-m', 'pip', 'install', '-r', str(root / 'requirements.txt')], check=True)
print(python)
