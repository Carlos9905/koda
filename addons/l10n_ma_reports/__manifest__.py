# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Morocco - Accounting Reports',
    'countries': ['ma'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Morocco.

This module has been built with the help of Caudigef.
    """,
    'depends': [
        'l10n_ma',
        'account_reports',
    ],
    'data': [
        "data/profit_and_loss.xml",
        "data/balance_sheet.xml",
    ],
    'installable': True,
    'auto_install': [
        'l10n_ma',
        'account_reports',
    ],
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
