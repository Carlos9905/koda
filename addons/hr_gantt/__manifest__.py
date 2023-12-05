# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Employees in Gantt',
    'category': 'Hidden',
    'summary': 'Employees in Gantt',
    'version': '1.0',
    'description': """ """,
    'depends': ['hr', 'web_gantt'],
    'auto_install': True,
    'license': 'OEEL-1',
    'assets': {
        'web.assets_backend': [
            'hr_gantt/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'hr_gantt/static/tests/**/*',
        ],
    }
}
