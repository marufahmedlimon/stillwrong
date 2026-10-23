import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import release_manifest
import check_release
import package_release

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=ROOT); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'master'; self.root.mkdir()
        for name in release_manifest.FILES:
            path=self.root/name; path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text('{}' if path.suffix=='.json' else 'Synthetic fixture',encoding='utf-8')

    def test_private_unknown_files_never_packaged(self):
        (self.root/'.env').write_text('PRIVATE_TOKEN=not-a-real-token')
        (self.root/'private.md').write_text('Private client data')
        (self.root/'docs'/'upload.bn.md').write_text('Private publication instructions')
        target,archive=package_release.build(self.root)
        with zipfile.ZipFile(archive) as z:
            self.assertNotIn('stillwrong/.env',z.namelist())
            self.assertNotIn('stillwrong/private.md',z.namelist())
            self.assertNotIn('stillwrong/docs/upload.bn.md',z.namelist())
            self.assertIsNone(z.testzip())
        self.assertFalse((target/'.env').exists())
        for line in (target/'SHA256SUMS').read_text().splitlines():
            expected,rel=line.split('  ',1)
            self.assertEqual(expected,hashlib.sha256((target/rel).read_bytes()).hexdigest())

    def test_local_paths_cannot_publish(self):
        (self.root/'README.md').write_text('C:\\Users\\someone\\secret',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'local path'): check_release.check(self.root)

    def test_unresolved_owner_cannot_publish(self):
        (self.root/'README.md').write_text('YOUR_GITHUB_NAME',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'owner'): check_release.check(self.root)

    def test_missing_link_cannot_publish(self):
        (self.root/'README.md').write_text('[guide](missing.md)',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'missing release link'): check_release.check(self.root)

    def test_existing_upload_folder_preserved(self):
        dest=self.root/'github-publish'; dest.mkdir(); (dest/'note.txt').write_text('Preserve me')
        with self.assertRaises(ValueError): package_release.build(self.root)
        self.assertEqual((dest/'note.txt').read_text(),'Preserve me')
