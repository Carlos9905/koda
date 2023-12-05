# -*- coding: utf-8 -*-
# Koda
from koda import fields, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('easypost', 'Easypost')])
    easypost_carrier = fields.Char('Carrier Prefix', index=True)
