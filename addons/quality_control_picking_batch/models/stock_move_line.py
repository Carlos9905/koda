# -*- encoding: utf-8 -*-
# Koda

from koda import models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_check_values(self, quality_point):
        vals = super()._get_check_values(quality_point)
        vals.update(batch_id=self.picking_id.batch_id.id)
        return vals
