# -*- coding: utf-8 -*-
# Koda

{
    'name': "Mrp Accounting",
    'version': "1.0",
    'category': 'Inventory/Inventory',
    'summary': "Bridge between Mrp and Accounting",
    'description': """
Automatic accounting for MRP
    """,
    'depends': ['mrp_account', 'stock_accountant'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
