# -*- coding: utf-8 -*-
# Koda

from koda import models


class MrpRouting(models.Model):
    _inherit = 'mrp.routing.workcenter'

    def _total_cost_per_hour(self):
        return super()._total_cost_per_hour() + self.workcenter_id.employee_costs_hour * self.employee_ratio
