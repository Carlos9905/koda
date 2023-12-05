# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Test US Payroll',
    'countries': ['us'],
    'category': 'Human Resources',
    'summary': 'Test US Payroll',
    'depends': [
        'l10n_us_hr_payroll',
        'l10n_us_hr_payroll_account',
    ],
    'license': 'OEEL-1',
    'post_init_hook': '_generate_payslips',
}
