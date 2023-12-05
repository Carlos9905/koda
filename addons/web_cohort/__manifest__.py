# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Cohort View',
    'summary': 'Basic Cohort view for koda',
    'category': 'Hidden',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'web_cohort/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'web_cohort/static/tests/**/*.js',
        ],
    },
    'auto_install': True,
    'license': 'OEEL-1',
}
