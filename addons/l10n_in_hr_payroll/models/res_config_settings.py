# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_in_dearness_allowance = fields.Boolean(
        string="Dearness Allowance", related='company_id.l10n_in_dearness_allowance', readonly=False)
