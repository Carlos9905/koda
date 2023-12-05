# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for accounting",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'account_reports'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['account_reports'],
    'license': 'OEEL-1',
}
