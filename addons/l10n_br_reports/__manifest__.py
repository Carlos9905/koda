# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Brazil - Accounting Reports',
    'countries': ['br'],
    'version': '0.1',
    'category': 'Accounting/Localizations/Reporting',
    'description': """Accounting reports for Brazil""",
    'depends': ['l10n_br', 'account_reports'],
    'data': [
        'data/account_financial_html_report_data.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_br', 'account_reports'],
    'license': 'OEEL-1',
}
