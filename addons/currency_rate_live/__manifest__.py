# -*- coding: utf-8 -*-
# Koda
{
    'name': 'Live Currency Exchange Rate',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """Import exchange rates from the Internet.
""",
    'depends': [
        'account',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/service_cron_data.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
