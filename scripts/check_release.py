"""Check the exact manual-upload payload without reading private workspace files."""
import json
import re
from pathlib import Path
from urllib.parse import unquote
from release_manifest import paths

ROOT=Path(__file__).resolve().parents[1]

def check(root=ROOT):
    entries=list(paths(root)); included={name for name,_ in entries}
    errors=[]
    if len(entries)+1>100: errors.append('More than 100 upload files including checksum manifest')
    for rel,path in entries:
        if path.stat().st_size>25*1024*1024: errors.append(f'{rel}: exceeds browser upload limit')
        if path.suffix in {'.md','.json','.yml','.yaml','.html','.svg','.txt','.py'} or path.name=='LICENSE':
            text=path.read_text(encoding='utf-8')
            if re.search(r'[\u0980-\u09ff]',text): errors.append(f'{rel}: non-English Bengali content in public payload')
            if path.suffix=='.py': continue
            if re.search(r'[A-Z]:[\\/]+Users[\\/]',text): errors.append(f'{rel}: machine-local path')
            if 'YOUR_GITHUB_NAME' in text: errors.append(f'{rel}: unreplaced owner')
            if re.search(r'\b(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})',text): errors.append(f'{rel}: possible credential')
            if path.suffix=='.json': json.loads(text)
            if path.suffix=='.md':
                links=re.findall(r'\]\(([^\s)]+)\)',text)+re.findall(r'src="([^"]+)"',text)
                for link in links:
                    if link.startswith(('https://','http://','#','mailto:')): continue
                    target=(Path(rel).parent/unquote(link.split('#')[0])).as_posix()
                    # Normalize '..' without escaping release root.
                    resolved=(Path(root)/target).resolve()
                    if not resolved.is_relative_to(Path(root).resolve()): errors.append(f'{rel}: escaping link {link}')
                    elif resolved.relative_to(Path(root).resolve()).as_posix() not in included: errors.append(f'{rel}: missing release link {link}')
    if errors: raise ValueError('\n'.join(errors))
    return entries

if __name__=='__main__':
    print(f'Release checks passed: {len(check())} allowlisted files; no private runs, environments or live absolute-path evidence.')
