# -*- encoding: utf-8 -*-
# Koda
{
    'name': 'Bulgaria - Accounting Reports',
    'countries': ['bg'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Base module for Bulgarian reports
    """,
    'depends': [
        'l10n_bg',
        'account_reports',
    ],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
