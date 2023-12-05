# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Point of Sale enterprise',
    'category': 'Sales/Point of Sale',
    'summary': 'Advanced features for PoS',
    'description': """
Advanced features for the PoS like better views 
for IoT Box config.   
""",
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'depends': ['web_enterprise', 'point_of_sale'],
    'auto_install': True,
    'license': 'OEEL-1',
}
