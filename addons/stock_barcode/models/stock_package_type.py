# -*- coding: utf-8 -*-
# Koda

from koda import api, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    @api.model
    def _get_fields_stock_barcode(self):
        return ['barcode', 'name']
