# -*- coding: utf-8 -*-
# Koda

import koda

# ----------------------------------------------------------
# Monkey patch release to set the edition as 'enterprise'
# ----------------------------------------------------------
koda.release.version_info = koda.release.version_info[:5] + ('e',)
if '+e' not in koda.release.version:     # not already patched by packaging
    koda.release.version = '{0}+e{1}{2}'.format(*koda.release.version.partition('-'))

koda.service.common.RPC_VERSION_1.update(
    server_version=koda.release.version,
    server_version_info=koda.release.version_info)
