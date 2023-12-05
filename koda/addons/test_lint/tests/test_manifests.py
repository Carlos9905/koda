# Koda

from koda.modules import get_modules
from koda.modules.module import load_manifest, _DEFAULT_MANIFEST
from koda.tests import BaseCase


MANIFEST_KEYS = {
    'name', 'icon', 'addons_path', 'license',  # mandatory keys
    *_DEFAULT_MANIFEST,                        # optional keys
    'contributors', 'maintainer', 'url',       # unused "informative" keys
}


class ManifestLinter(BaseCase):
    def test_manifests_keys(self):
        for module in get_modules():
            with self.subTest(module=module):
                manifest_keys = load_manifest(module).keys()
                unknown_keys = manifest_keys - MANIFEST_KEYS
                self.assertEqual(unknown_keys, set(), f"Unknown manifest keys in module {module!r}. Either there are typos or they must be white listed.")
