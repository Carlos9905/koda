# -*- encoding: utf-8 -*-
# Koda

{
    'name': 'Kenya - Accounting Reports',
    'countries': ['ke'],
    'version': '1.0',
    'description': """
Accounting reports for Kenya
============================

    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': ['l10n_ke', 'account_reports'],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
