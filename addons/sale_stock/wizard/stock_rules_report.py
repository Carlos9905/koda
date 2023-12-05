# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models


class StockRulesReport(models.TransientModel):
    _inherit = 'stock.rules.report'

    so_route_ids = fields.Many2many('stock.route', string='Apply specific routes',
        domain="[('sale_selectable', '=', True)]", help="Choose to apply SO lines specific routes.")

    def _prepare_report_data(self):
        data = super(StockRulesReport, self)._prepare_report_data()
        data['so_route_ids'] = self.so_route_ids.ids
        return data
