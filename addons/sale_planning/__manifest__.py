# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Sale Planning',
    'category': 'Hidden',
    'description': """
This module allows you to schedule your Sales Order based on the product configuration.

For products on which the "Plan Services" option is enabled, you will have the opportunity
to automatically plan the shifts for employees whom are able to take the shift
(i.e. employees who have the same role as the one configured on the product).

Plan shifts and keep an eye on the hours consumed on your plannable products.
    """,
    'depends': ['sale_management', 'sale_service', 'planning'],
    'auto_install': ['sale_management', 'planning'],
    'data': [
        'security/ir.model.access.csv',
        'security/sale_planning_security.xml',
        'views/planning_role_views.xml',
        'views/planning_slot_views.xml',
        'views/planning_templates.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'report/planning_report_templates.xml',
    ],
    'demo': [
        'data/product_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_planning/static/src/views/**/*',
        ],
        'web.assets_frontend': [
            'sale_planning/static/src/js/frontend/**/*',
        ],
        'web.assets_tests': [
            'sale_planning/static/tests/tours/*',
        ],
        'web.qunit_suite_tests': [
            'sale_planning/static/tests/*',
        ]
    },
    'license': 'OEEL-1',
    'uninstall_hook': 'uninstall_hook',
}
