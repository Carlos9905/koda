# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Helpdesk Merge action',
    'version': '1.0',
    'category': 'Productivity/Data Cleaning',
    'summary': 'Add Merge action in contextual menu of helpdesk ticket model.',
    'description': """Add Merge action in contextual menu of helpdesk ticket model.""",
    'depends': ['data_merge', 'helpdesk'],
    'data': [
        'data/ir_model_data.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
