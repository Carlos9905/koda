# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class HelpdeskSLAReport(models.Model):
    _inherit = 'helpdesk.sla.report.analysis'

    product_id = fields.Many2one('product.product', string='Product', readonly=True)

    def _select(self):
        select_str = super()._select()
        select_str += ", T.product_id as product_id"
        return select_str
