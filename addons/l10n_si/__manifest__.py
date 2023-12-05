# Koda
{
    'name': 'Slovenian - Accounting',
    'website': 'https://www.koda.com/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['si'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Chart of accounts and taxes for Slovenia.
    """,
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/account_tax_report_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
