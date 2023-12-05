# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Poland - Payroll with Accounting',
    'countries': ['pl'],
    'author': 'Odoo',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Accounting Data for Poland Payroll Rules
============================================
    """,
    'depends': ['hr_payroll_account', 'l10n_pl', 'l10n_pl_hr_payroll'],
    'data': [
        'data/account_chart_template_data.xml',
    ],
    'demo': [
        'data/l10n_pl_hr_payroll_account_demo.xml',
    ],
    'license': 'OEEL-1',
    'auto_install': True,
}
