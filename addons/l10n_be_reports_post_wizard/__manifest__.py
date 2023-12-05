# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Belgium - Accounting Reports (post wizard)',
    'countries': ['be'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Enable the VAT wizard when posting a tax return journal entry
    """,
    'depends': [
        'l10n_be_reports'
    ],
    'data': [
        'views/l10n_be_wizard_xml_export_options_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
