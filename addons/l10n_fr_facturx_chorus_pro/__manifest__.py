# -*- coding: utf-8 -*-
# Koda

{
    'name': 'France - Factur-X integration with Chorus Pro',
    'countries': ['fr'],
    'version': '1.0',
    'category': 'Accounting/Localizations/EDI',
    'description': """
Add supports to fill three optional fields used when using Chorus Pro, especially when invoicing public services.
""",
    'depends': [
        'account',
        'account_edi_ubl_cii',
        'l10n_fr'
    ],
    'data': [
        'views/account_move_views.xml',
    ],
    'license': 'LGPL-3',
}
