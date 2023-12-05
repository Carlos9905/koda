# -*- coding: utf-8 -*-
# Koda
from koda import fields, models


class ProductPackaging(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('ups_rest', 'UPS')])
