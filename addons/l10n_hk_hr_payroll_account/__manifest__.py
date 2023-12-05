# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Hong Kong - Payroll with Accounting',
    'countries': ['hk'],
    'version': '1.0',
    'category': 'Human Resources/Payroll',
    'description': """
Accounting Data for Hong Kong Payroll Rules
===========================================
    """,
    'depends': ['hr_payroll_account', 'l10n_hk', 'l10n_hk_hr_payroll'],
    'data': [
        'data/account_chart_template_data.xml',
    ],
    'demo': [
        'data/l10n_hk_hr_payroll_account_demo.xml',
    ],
    'license': 'OEEL-1',
    'auto_install': True,
}
