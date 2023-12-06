# -*- coding: utf-8 -*-
# Koda

{
    'name': 'OdooBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add OdooBot in discussions',
    'website': 'https://www.koda.com/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/kodabot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
