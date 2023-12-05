# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Netherlands Intrastat Declaration',
    'countries': ['nl'],
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Generates Netherlands Intrastat report for declaration based on invoices.
    """,
    'depends': ['l10n_nl_reports', 'account_intrastat'],
    'data': [
        'data/account_report_ec_sales_list_report.xml',
        'views/res_company_view.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
