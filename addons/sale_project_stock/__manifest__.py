# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Sale Project - Sale Stock',
    'version': '1.0',
    'description': 'Adds a full traceability of inventory operations on the profitability report.',
    'summary': 'Adds a full traceability of inventory operations on the profitability report.',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': ['sale_project', 'sale_stock'],
    'data': [
        'views/stock_move_views.xml',
    ],
    'auto_install': True,
}
