# -*- coding: utf-8 -*-
# Koda

{
    'name': 'MRP Subcontracting Repair',
    'version': '1.0',
    'category': 'Manufacturing/Repair',
    'description': """
Bridge module between MRP subcontracting and Repair
    """,
    'depends': [
        'mrp_subcontracting', 'repair'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/mrp_subcontracting_repair_security.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
