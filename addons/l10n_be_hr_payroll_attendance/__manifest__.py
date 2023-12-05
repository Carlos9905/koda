#-*- coding:utf-8 -*-
# Koda

{
    'name': 'Belgian Payroll - Attendance',
    'countries': ['be'],
    'category': 'Human Resources/Employees',
    'sequence': 95,
    'summary': 'Manage extra hours for your hourly paid employees for belgian payroll',
    'installable': True,
    'auto_install': True,
    'depends': [
        'hr_payroll_attendance',
        'l10n_be_hr_payroll',
    ],
    'license': 'OEEL-1',
}
