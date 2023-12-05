# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class RepairkWarnUncompleteMove(models.TransientModel):
    _name = 'repair.warn.uncomplete.move'
    _description = 'Warn Uncomplete Move(s)'

    repair_ids = fields.Many2many('repair.order', string='Repair Orders')

    def action_validate(self):
        self.ensure_one()
        return self.repair_ids.action_repair_done()
