# -*- coding: utf-8 -*-
# Koda

from koda import models, api


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def _get_fields_stock_barcode(self):
        return super()._get_fields_stock_barcode() + ['use_expiration_date', 'use_time']
