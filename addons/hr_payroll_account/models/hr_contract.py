#-*- coding:utf-8 -*-
# Koda

from koda import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    analytic_account_id = fields.Many2one(
        'account.analytic.account', 'Analytic Account', check_company=True)
