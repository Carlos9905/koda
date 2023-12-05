# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_pl_reports_tax_office_id = fields.Many2one(related='company_id.l10n_pl_reports_tax_office_id', readonly=False)
