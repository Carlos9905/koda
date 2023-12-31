# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Website Mail',
    'category': 'Hidden',
    'summary': 'Website Module for Mail',
    'version': '0.1',
    'description': """
Module holding mail improvements for website. It holds the follow widget.
""",
    'depends': ['website', 'mail'],
    'data': [
        'views/website_mail_templates.xml',
    ],
    'installable': True,
    'auto_install': True,
    'assets': {
        'web.assets_frontend': [
            'website_mail/static/src/js/follow.js',
            'website_mail/static/src/css/website_mail.scss',
        ],
    },
    'license': 'LGPL-3',
}
