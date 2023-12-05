# -*- coding: utf-8 -*-
# Koda
{
    'name': 'Sale Loyalty - Delivery',
    'summary': 'Adds free shipping mechanism in sales orders',
    'description': 'Integrate free shipping in sales orders.',
    'category': 'Sales/Sales',
    'data': [
        'views/loyalty_reward_views.xml',
    ],
    'depends': ['sale_loyalty', 'delivery'],
    'auto_install': True,
    'license': 'LGPL-3',
}
