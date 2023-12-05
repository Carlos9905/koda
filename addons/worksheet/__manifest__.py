# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Worksheet',
    'category': 'Hidden',
    'summary': 'Create customizable worksheet',
    'description': """
Create customizable worksheet
================================

""",
    'depends': ['web_studio'],
    'data': [
        'security/ir.model.access.csv',
        'security/worksheet_security.xml',
        'views/worksheet_template_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'worksheet/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'worksheet/static/tests/*.js',
        ],
    },
    'license': 'OEEL-1',
}
