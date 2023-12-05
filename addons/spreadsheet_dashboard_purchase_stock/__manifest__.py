# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for purchases",
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'purchase_stock'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['purchase_stock'],
    'license': 'LGPL-3',
}
