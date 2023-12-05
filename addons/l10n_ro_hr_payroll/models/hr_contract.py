# -*- coding:utf-8 -*-
# Koda

from koda import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_ro_work_type = fields.Selection([
        ('1', 'Normal Conditions'),
        ('2', 'Particular Conditions'),
        ('3', 'Special Conditions')
    ], string='Work type', default="1")
