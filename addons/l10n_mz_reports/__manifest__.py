# -*- coding: utf-8 -*-
# Koda
{
    'name': 'Mozambique - Accounting Reports',
    'countries': ['mz'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Base module for Mozambican reports
    """,
    'depends': [
        'l10n_mz',
        'account_reports',
    ],
    'data': [
        'data/balance_sheet.xml',
        "data/profit_loss.xml",
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
