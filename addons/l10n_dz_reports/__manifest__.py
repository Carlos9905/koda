# -*- encoding: utf-8 -*-
# Koda

{
    'name': 'Algeria - Accounting Reports',
    'countries': ['dz'],
    'version': '0.1',
    'description': """
Accounting reports for Algeria
================================
    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': ['l10n_dz', 'account_reports'],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
    ],
    'auto_install': ['l10n_dz', 'account_reports'],
    'installable': True,
    'license': 'OEEL-1',
}
