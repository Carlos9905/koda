# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Greece - Accounting Reports',
    'countries': ['gr'],
    'version': '1.0',
    'description': """
Accounting reports for Greece
================================

    """,
    'category': 'Accounting/Localizations/Reporting',
    'depends': [
        'l10n_gr',
        'account_reports',
    ],
    'data': [
        'data/balance_sheet-gr.xml',
        'data/profit_and_loss-gr.xml',
        'data/ec_sales_list_report-gr.xml',
    ],
    'post_init_hook': '_l10n_gr_reports_post_init',
    'installable': True,
    'auto_install': ['l10n_gr', 'account_reports'],
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
