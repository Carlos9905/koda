# -*- coding: utf-8 -*-
# Koda
{
    'name': 'POS IoT Six',
    'version': '1.0',
    'category': 'Sales/Point Of Sale',
    'summary': 'Integrate your POS with a Six payment terminal through IoT',
    'data': [
        'views/pos_payment_method_views.xml',
    ],
    'depends': ['pos_iot'],
    'installable': True,
    'license': 'OEEL-1',
    'assets': {
        'point_of_sale.assets': [
            'pos_iot_six/static/src/js/models.js',
            'pos_iot_six/static/src/js/payment_six.js',
        ],
    }
}
