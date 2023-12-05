# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for human resources",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'hr_contract_reports'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['hr_contract_reports'],
    'license': 'OEEL-1',
}
