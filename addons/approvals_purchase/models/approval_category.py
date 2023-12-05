# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models


class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    approval_type = fields.Selection(selection_add=[('purchase', 'Create RFQ\'s')])

    @api.onchange('approval_type')
    def _onchange_approval_type(self):
        if self.approval_type == 'purchase':
            self.has_product = 'required'
            self.has_quantity = 'required'
