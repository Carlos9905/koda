# -*- coding: utf-8 -*-
# Koda

from koda import models


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    def _compute_presence_state(self):
        super()._compute_presence_state()
        employees = self.filtered(lambda employee: employee.hr_presence_state != 'present' and employee.is_absent)
        employees.update({'hr_presence_state': 'absent'})
