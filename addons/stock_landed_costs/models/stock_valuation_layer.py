# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    stock_landed_cost_id = fields.Many2one('stock.landed.cost', 'Landed Cost')
