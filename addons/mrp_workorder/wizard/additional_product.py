# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from koda import models, api, fields


class MrpWorkorderAdditionalProduct(models.TransientModel):
    _name = "mrp_workorder.additional.product"
    _description = "Additional Product"

    product_id = fields.Many2one(
        'product.product',
        'Product',
        required=True,
        domain="[('company_id', 'in', (company_id, False)), ('type', '!=', 'service')]")
    product_tracking = fields.Selection(related='product_id.tracking')
    product_qty = fields.Float('Quantity', default=1, required=True)
    product_uom_id = fields.Many2one('uom.uom', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    type = fields.Selection([
        ('component', 'Component'),
        ('byproduct', 'By-Product')])
    production_id = fields.Many2one('mrp.production')
    workorder_id = fields.Many2one(
        'mrp.workorder', default=lambda self: self.env.context.get('active_id', None),
    )
    company_id = fields.Many2one(related='workorder_id.company_id')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.product_uom_id = self.product_id.uom_id
            if self.product_tracking == 'serial':
                self.product_qty = 1

    def add_product(self):
        """Create workorder line for the additional product."""
        if self.workorder_id:
            wo = self.workorder_id
            if self.type == 'component':
                values = wo.production_id._get_move_raw_values(
                    self.product_id,
                    self.product_qty,
                    self.product_id.uom_id,
                    operation_id=wo.operation_id.id,
                )
            else:
                values = wo.production_id._get_move_finished_values(
                    self.product_id.id,
                    self.product_qty,
                    self.product_id.uom_id.id,
                    operation_id=wo.operation_id.id,
                )
        else:
            mo = self.production_id
            if self.type == 'component':
                values = mo._get_move_raw_values(self.product_id, self.product_qty, self.product_id.uom_id)
            else:
                values = mo._get_move_finished_values(self.product_id.id, self.product_qty, self.product_id.uom_id.id)

        move = self.env['stock.move'].create(values)
        if not self.workorder_id and self.type == 'component':
            move['production_id'] = None
        move._action_confirm()
