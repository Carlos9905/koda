# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    project_id = fields.Many2one(domain="['|', ('company_id', '=', False), '&', ('company_id', '=?', company_id), ('company_id', '=', current_company_id), ('allow_billable', '=', True), '|', ('pricing_type', '=', 'task_rate'), ('is_fsm', '=', True), ('allow_timesheets', 'in', [service_policy == 'delivered_timesheet', True])]")
