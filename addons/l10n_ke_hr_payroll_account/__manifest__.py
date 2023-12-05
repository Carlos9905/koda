# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Kenya - Payroll with Accounting',
    'countries': ['ke'],
    'author': 'Odoo',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Accounting Data for Kenyan Payroll Rules
========================================
    """,
    'depends': ['hr_payroll_account', 'l10n_ke', 'l10n_ke_hr_payroll'],
    'data': [
        'data/account_chart_template_data.xml',
    ],
    'demo': [
        'data/l10n_ke_hr_payroll_account_demo.xml',
    ],
    'license': 'OEEL-1',
    'auto_install': True,
}
