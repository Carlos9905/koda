# -*- coding: utf-8 -*-
# Koda

from . import models

def l10n_eu_oss_post_init(env):
    env['res.company']._map_all_eu_companies_taxes()

def l10n_eu_oss_uninstall(env):
    env.cr.execute("DELETE FROM ir_model_data WHERE module = 'l10n_eu_oss' and model in ('account.tax.group', 'account.account');")
