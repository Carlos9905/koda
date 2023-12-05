# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class AccountAnalyticAccountLine(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Analytic Account'

    employee_id = fields.Many2one('hr.employee', "Employee")
