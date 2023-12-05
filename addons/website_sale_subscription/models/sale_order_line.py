# -*- coding: utf-8 -*-
# Koda

from koda import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _is_reorder_allowed(self):
        if self.recurring_invoice:
            return False
        return super(SaleOrderLine, self)._is_reorder_allowed()
