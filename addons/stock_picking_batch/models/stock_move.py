# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.osv import expression


class StockMove(models.Model):
    _inherit = "stock.move"

    def _search_picking_for_assignation_domain(self):
        domain = super()._search_picking_for_assignation_domain()
        domain = expression.AND([domain, ['|', ('batch_id', '=', False), ('batch_id.is_wave', '=', False)]])
        return domain

    def _action_cancel(self):
        res = super()._action_cancel()

        for picking in self.picking_id:
            # Remove the picking from the batch if the whole batch isn't cancelled.
            if picking.state == 'cancel' and picking.batch_id and any(p.state != 'cancel' for p in picking.batch_id.picking_ids):
                picking.batch_id = None
        return res

    def _assign_picking_post_process(self, new=False):
        super()._assign_picking_post_process(new=new)
        for picking in self.picking_id:
            picking._find_auto_batch()

    def write(self, vals):
        res = super().write(vals)
        if 'state' in vals and vals['state'] == 'assigned':
            for picking in self.picking_id:
                if picking.state != 'assigned':
                    continue
                picking._find_auto_batch()

        return res
