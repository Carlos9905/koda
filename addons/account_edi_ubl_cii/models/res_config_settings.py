# -*- coding: utf-8 -*-
# Koda

from koda import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_is_ubl_cii = fields.Boolean(string='Peppol format', related='company_id.invoice_is_ubl_cii', readonly=False)
