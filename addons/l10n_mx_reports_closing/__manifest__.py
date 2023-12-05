# coding: utf-8
# Koda

{
    "name": "Mexico - Month 13 Trial Balance",
    'countries': ['mx'],
    "summary": "Mexico Month 13 Trial Balance Report",
    "version": "1.0",
    "author": "Vauxoo / Odoo",
    "category": "Accounting/Localizations/Reporting",
    "website": "http://www.koda.com",
    "license": "OEEL-1",
    "depends": [
        "l10n_mx_reports",
    ],
    "data": [
        "views/account_move_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'l10n_mx_reports_closing/static/src/components/**/*',
        ],
    },
    "installable": True,
    "auto_install": True,
}
