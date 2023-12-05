# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models, _

class ResCompany(models.Model):
    _inherit = "res.company"

    gain_account_id = fields.Many2one(
        'account.account',
        domain="[('deprecated', '=', False)]",
        check_company=True,
        help="Account used to write the journal item in case of gain while selling an asset",
    )
    loss_account_id = fields.Many2one(
        'account.account',
        domain="[('deprecated', '=', False)]",
        check_company=True,
        help="Account used to write the journal item in case of loss while selling an asset",
    )
