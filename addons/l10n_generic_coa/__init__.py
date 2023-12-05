# -*- coding: utf-8 -*-
# Koda


def uninstall_hook(env):
    env.cr.execute(
        "DELETE FROM ir_model_data WHERE module = 'l10n_generic_coa'"
    )
