# -*- coding: utf-8 -*-
# Koda
from koda import fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    l10n_cl_sii_code = fields.Integer('SII Code', group_operator=False)
