# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Units of measure',
    'version': '1.0',
    'category': 'Sales/Sales',
    'depends': ['base'],
    'description': """
This is the base module for managing Units of measure.
========================================================================
    """,
    'data': [
        'data/uom_data.xml',
        'security/uom_security.xml',
        'security/ir.model.access.csv',
        'views/uom_uom_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
