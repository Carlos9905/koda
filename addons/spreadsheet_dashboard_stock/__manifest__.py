# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for stock",
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'stock_enterprise'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['stock_enterprise'],
    'license': 'OEEL-1',
}
