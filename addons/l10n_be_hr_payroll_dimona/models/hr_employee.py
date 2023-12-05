# -*- coding: utf-8 -*-
# Koda

import re

from koda import models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def _get_split_name(self):
        self.ensure_one()
        names = re.sub(r"\([^()]*\)", "", self.name).strip().split()
        first_name = names[-1]
        last_name = ' '.join(names[:-1])
        return first_name, last_name
