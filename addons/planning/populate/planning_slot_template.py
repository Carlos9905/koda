# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.tools import populate


class PlanningTemplate(models.Model):
    _inherit = "planning.slot.template"
    _populate_sizes = {"small": 10, "medium": 50, "large": 1000}
    _populate_dependencies = ["planning.role"]

    def _populate_factories(self):
        role_ids = self.env.registry.populated_models["planning.role"]

        return [
            ("name", populate.constant('shift_template_{counter}')),
            ("sequence", populate.randomize([False] + [i for i in range(1, 101)])),
            ("active", populate.randomize([True, False], [0.8, 0.2])),
            ('role_id', populate.randomize(role_ids)),
        ]
