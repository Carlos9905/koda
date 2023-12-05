# -*- coding: utf-8 -*-
# Koda

{
    'name': 'UTM Deduplication',
    'version': '1.0',
    'category': 'Productivity/Data Cleaning',
    'summary': 'Find duplicate records and merge them',
    'description': """Find duplicate records and merge them""",
    'depends': ['data_merge', 'utm'],
    'data': [
        'data/data_merge_data.xml',
        'data/ir_model_data.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
