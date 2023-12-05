# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class IotDevice(models.Model):
    _inherit = 'iot.device'

    picking_type_ids = fields.Many2many('stock.picking.type', string="Operation Types", domain=[('code', '!=', 'mrp_operation'), ])
