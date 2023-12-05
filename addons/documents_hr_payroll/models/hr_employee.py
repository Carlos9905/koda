# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    documents_share_id = fields.Many2one(groups="hr_payroll.group_hr_payroll_user")
