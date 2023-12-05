# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Salary Configurator - Payroll',
    'category': 'Human Resources',
    'summary': 'Adds a Gross to Net Salary Simulaton',
    'depends': [
        'hr_contract_salary',
        'hr_payroll',
    ],
    'data': [
        'data/hr_contract_salary_resume_data.xml',
        'views/menuitems.xml',
        'views/hr_contract_views.xml',
        'views/hr_contract_salary_template.xml',
    ],
    'license': 'OEEL-1',
    'auto_install': True,
    'assets': {
        'web.assets_frontend': [
            'hr_contract_salary_payroll/static/src/js/*.js',
            'hr_contract_salary_payroll/static/src/xml/*.xml',
        ],
        'web.assets_backend': [
            'hr_contract_salary_payroll/static/src/js/tours/*.js',
        ],
        'web.assets_tests': [
            'hr_contract_salary_payroll/static/tests/**/*.js',
        ],
    }
}
