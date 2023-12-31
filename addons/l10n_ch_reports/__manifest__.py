# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Switzerland - Accounting Reports',
    'countries': ['ch'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Switzerland
    """,
    'depends': [
        'l10n_ch', 'account_reports'
    ],
    'data': [
        'data/account_financial_html_report_data.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_ch', 'account_reports'],
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
