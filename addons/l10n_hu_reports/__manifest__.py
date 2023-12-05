# -*- encoding: utf-8 -*-
# Koda
{
    'name': 'Hungary - Accounting Reports',
    'countries': ['hu'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Hungary
    """,
    'depends': [
        'l10n_hu',
        'account_reports',
    ],
    'data': [
        'data/balance_sheet.xml',
        'data/profit_loss.xml',
        'data/account_report_ec_sales_list_report.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
