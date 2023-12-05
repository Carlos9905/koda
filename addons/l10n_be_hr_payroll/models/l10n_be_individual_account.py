# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
import logging

from collections import OrderedDict
from koda import api, fields, models, _
from koda.fields import Datetime

_logger = logging.getLogger(__name__)


class L10nBeIndividualAccount(models.Model):
    _name = 'l10n_be.individual.account'
    _inherit = 'hr.payroll.declaration.mixin'
    _description = 'HR Individual Account Report By Employee'

    name = fields.Char(
        string="Description", required=True, compute='_compute_name', readonly=False, store=True)

    def _country_restriction(self):
        return 'BE'

    @api.depends('year')
    def _compute_name(self):
        for sheet in self:
            sheet.name = _('Individual Accounts - Year %s', sheet.year)

    def action_generate_declarations(self):
        for sheet in self:
            all_payslips = self.env['hr.payslip'].search([
                ('date_to', '<=', datetime.date(int(sheet.year), 12, 31)),
                ('date_from', '>=', datetime.date(int(sheet.year), 1, 1)),
                ('state', 'in', ['done', 'paid']),
                ('company_id', '=', sheet.company_id.id),
            ])
            all_employees = all_payslips.mapped('employee_id')
            sheet.write({
                'line_ids': [(5, 0, 0)] + [(0, 0, {
                    'employee_id': employee.id,
                    'res_model': 'l10n_be.individual.account',
                    'res_id': sheet.id,
                }) for employee in all_employees]
            })
        return super().action_generate_declarations()

    def _get_rendering_data(self, employees):
        self.ensure_one()

        payslips = self.env['hr.payslip'].search([
            ('employee_id', 'in', employees.ids),
            ('state', 'in', ['done', 'paid']),
            ('date_from', '>=', Datetime.now().replace(month=1, day=1, year=int(self.year))),
            ('date_from', '<=', Datetime.now().replace(month=12, day=31, year=int(self.year))),
            '|',
            ('struct_id.country_id', '=', False),
            ('struct_id.country_id.code', '=', "BE"),
        ])
        employees = payslips.employee_id
        lines = payslips.line_ids.filtered(lambda l: l.salary_rule_id.appears_on_payslip)
        payslip_rules = [(rule.code, rule.sequence) for rule in lines.salary_rule_id]
        payslip_rules = sorted(payslip_rules, key=lambda x: x[1])
        worked_days = payslips.worked_days_line_ids

        result = {
            employee: {
                'year': self.year,
                'rules': OrderedDict(
                    (rule[0], {
                        'year': {'name': False, 'total': 0},
                        'month': {m: {'name': False, 'total': 0} for m in range(12)},
                        'quarter': {q: {'name': False, 'total': 0} for q in range(4)}
                    }) for rule in payslip_rules),
                'worked_days': {
                    code: {
                        'year': {'name': False, 'number_of_days': 0, 'number_of_hours': 0},
                        'month': {m: {'name': False, 'number_of_days': 0, 'number_of_hours': 0} for m in range(12)},
                        'quarter': {q: {'name': False, 'number_of_days': 0, 'number_of_hours': 0} for q in range(4)}
                    } for code in worked_days.mapped('code')
                }
            } for employee in employees
        }

        for line in lines:
            rule = result[line.employee_id]['rules'][line.salary_rule_id.code]
            month = line.slip_id.date_from.month - 1
            rule['month'][month]['name'] = line.name
            rule['month'][month]['total'] += line.total
            rule['quarter'][(month) // 3]['name'] = line.name
            rule['quarter'][(month) // 3]['total'] += line.total
            rule['year']['name'] = line.name
            rule['year']['total'] += line.total

            rule['month'][month]['total'] = round(rule['month'][month]['total'], 2)
            rule['quarter'][(month) // 3]['total'] = round(rule['quarter'][(month) // 3]['total'], 2)
            rule['year']['total'] = round(rule['year']['total'], 2)

        for worked_day in worked_days:
            work = result[worked_day.payslip_id.employee_id]['worked_days'][worked_day.code]
            month = worked_day.payslip_id.date_from.month - 1

            work['month'][month]['name'] = worked_day.name
            work['month'][month]['number_of_days'] += worked_day.number_of_days
            work['month'][month]['number_of_hours'] += worked_day.number_of_hours
            work['quarter'][(month) // 3]['name'] = worked_day.name
            work['quarter'][(month) // 3]['number_of_days'] += worked_day.number_of_days
            work['quarter'][(month) // 3]['number_of_hours'] += worked_day.number_of_hours
            work['year']['name'] = worked_day.name
            work['year']['number_of_days'] += worked_day.number_of_days
            work['year']['number_of_hours'] += worked_day.number_of_hours

        return result

    def _get_pdf_report(self):
        return self.env.ref('l10n_be_hr_payroll.action_report_individual_account')

    def _get_pdf_filename(self, employee):
        self.ensure_one()
        return _('%s-individual-account-%s', employee.name, self.year)
