# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for payroll",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'hr_payroll', 'hr_contract_reports'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['hr_payroll'],
    'license': 'OEEL-1',
}
