# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    documents_account_settings = fields.Boolean(related='company_id.documents_account_settings', readonly=False,
                                                string="Accounting ")
    account_folder = fields.Many2one(related='company_id.account_folder', readonly=False,
                                     string="account default folder")
