"""Build the manual-upload folder and a deterministic source ZIP."""
import hashlib
import argparse
import shutil
import zipfile
from pathlib import Path
from check_release import ROOT,check

def build(root=ROOT, target=None, archive=None):
    entries=check(root)
    target=Path(target) if target else Path(root)/'github-publish'
    archive=Path(archive) if archive else Path(root).parent/'stillwrong-github-v0.1.1-english.zip'
    if target.exists():
        raise ValueError('Upload folder already exists; choose a fresh target rather than deleting user files')
    if any(p.is_symlink() or (p.exists() and getattr(p.lstat(),'st_file_attributes',0) & 0x400) for p in [target,*target.parents,archive,*archive.parents]):
        raise ValueError('Linked output rejected')
    if archive.exists() or archive.with_suffix('.zip.sha256').exists():
        raise ValueError('ZIP/checksum already exists; choose a fresh --archive path')
    if not archive.parent.is_dir():
        raise ValueError('Archive parent must already exist')
    target.mkdir(parents=True)
    sums=[]
    for rel,path in entries:
        dest=target/rel; dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(path,dest)
        sums.append(f'{hashlib.sha256(dest.read_bytes()).hexdigest()}  {rel}')
    (target/'SHA256SUMS').write_text('\n'.join(sums)+'\n',encoding='utf-8')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for rel in sorted([r for r,_ in entries]+['SHA256SUMS']):
            info=zipfile.ZipInfo('stillwrong/'+rel,date_time=(2026,10,23,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
            z.writestr(info,(target/rel).read_bytes())
    with zipfile.ZipFile(archive) as z:
        if z.testzip(): raise ValueError('ZIP integrity failed')
        if set(z.namelist()) != {'stillwrong/'+r for r,_ in entries}|{'stillwrong/SHA256SUMS'}: raise ValueError('Unexpected ZIP members')
    checksum=hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix('.zip.sha256').write_text(f'{checksum}  {archive.name}\n',encoding='utf-8')
    print(f'Upload folder: {target}\nArchive: {archive}\nSHA256: {checksum}')
    return target,archive

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',help='Fresh upload folder; existing folders are preserved')
    parser.add_argument('--archive',help='Fresh ZIP path; existing files are preserved')
    args=parser.parse_args()
    build(target=args.output_dir,archive=args.archive)
