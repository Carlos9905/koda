# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.tools import populate


class PlanningRole(models.Model):
    _inherit = "planning.role"
    _populate_sizes = {"small": 10, "medium": 50, "large": 500}

    def _populate_factories(self):
        return [
            ("name", populate.constant('name_{counter}')),
            ("active", populate.randomize([True, False], [0.8, 0.2])),
            ("color", populate.randomize([False] + [i for i in range(1, 7)])),
            ("sequence", populate.randomize([False] + [i for i in range(1, 101)])),
        ]
