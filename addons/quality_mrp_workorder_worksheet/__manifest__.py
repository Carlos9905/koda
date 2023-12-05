# -*- encoding: utf-8 -*-
# Koda

{
    'name': 'Quality Worksheet for Workorder',
    'version': '1.0',
    'category': 'Manufacturing/Quality',
    'summary': 'Quality Worksheet for Workorder',
    'depends': ['quality_control_worksheet', 'quality_mrp_workorder'],
    'description': """
Create customizable quality worksheet for workorder.
""",
    "data": [
        'views/quality_views.xml',
    ],
    "demo": [
        'data/mrp_workorder_demo.xml',
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
