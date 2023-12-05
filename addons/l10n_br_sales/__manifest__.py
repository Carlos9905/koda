# coding: utf-8
# Koda
{
    'name': 'Brazil - Sale',
    'version': '1.0',
    'description': 'Sale modifications for Brazil',
    'category': 'Localization',
    'depends': [
        'l10n_br',
        'sale',
    ],
    'data': [
        'views/sale_portal_templates.xml',
        'report/sale_order_templates.xml',
        'report/report_invoice_templates.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
