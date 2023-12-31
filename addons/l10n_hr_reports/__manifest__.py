# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Croatia - Accounting Reports',
    'countries': ['hr'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Croatia
    """,
    'depends': [
        'l10n_hr', 'account_reports'
    ],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_hr', 'account_reports'],
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
