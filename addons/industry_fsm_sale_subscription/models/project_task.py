# -*- coding: utf-8 -*-
# Koda
from koda import models
from koda.osv import expression


class Task(models.Model):
    _inherit = "project.task"

    def action_fsm_view_material(self):
        res = super().action_fsm_view_material()
        res['domain'] = expression.AND([res['domain'], [('recurring_invoice', '=', False)]])
        return res
