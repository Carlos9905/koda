# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Belgium - Disallowed Expenses Data',
    'countries': ['be'],
    'version': '1.1',
    'category': 'Accounting/Accounting',
    'description': """
Disallowed Expenses Data for Belgium
    """,
    'depends': [
        'l10n_be',
        'account_disallowed_expenses',
    ],
    'data': [
        'data/account_disallowed_expenses.xml',
    ],
    'installable': True,
    'auto_install': True,
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
