# -*- coding: utf-8 -*-
# Koda

from koda import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_is_ubl_cii = fields.Boolean('Generate Peppol format by default', default=False)
