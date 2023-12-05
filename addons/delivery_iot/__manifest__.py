# -*- coding: utf-8 -*-
# Koda
{
    'name': "IoT for Delivery",
    'summary': "Use IoT devices in delivery operations",
    'description': """
Allows using IoT devices, such as scales and printers, for delivery operations.
""",
    'category': 'Manufacturing/Internet of Things (IoT)',
    'version': '1.0',
    'depends': ['iot', 'stock_delivery'],
    'data': [
        'report/delivery_carrier_reports.xml',
        'wizard/choose_delivery_package_views.xml',
        'views/iot_views.xml',
        'views/stock_picking_views.xml',
        ],
    'license': 'OEEL-1',
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'delivery_iot/static/src/**/*',
        ],
    }
}
