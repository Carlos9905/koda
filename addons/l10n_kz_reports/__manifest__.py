# -*- encoding: utf-8 -*-
# Koda

{
    'name': 'Kazakhstan - Accounting Reports',
    'countries': ['kz'],
    'version': '1.0',
    'description': """
Accounting reports for Kazakhstan
Contains Balance sheet, Profit and Loss reports
    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': ['l10n_kz', 'account_reports'],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
