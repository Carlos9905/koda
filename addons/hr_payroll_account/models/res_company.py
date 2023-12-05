# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    batch_payroll_move_lines = fields.Boolean(string="Batch Payroll Move Lines")
