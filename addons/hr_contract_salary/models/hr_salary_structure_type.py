# -*- coding:utf-8 -*-
# Koda

from koda import models, fields


class HrPayrollStructureType(models.Model):
    _inherit = 'hr.payroll.structure.type'
    _description = 'Salary Structure Type'

    salary_benefits_ids = fields.One2many('hr.contract.salary.benefit', 'structure_type_id')
