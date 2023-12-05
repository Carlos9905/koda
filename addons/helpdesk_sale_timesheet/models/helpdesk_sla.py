# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class HelpdeskSLA(models.Model):
    _inherit = 'helpdesk.sla'

    sale_line_ids = fields.Many2many(
        'sale.order.line', string="Sales Order Items",
        domain="[('is_service', '=', True)]")
