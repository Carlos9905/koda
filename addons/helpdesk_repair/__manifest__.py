# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Helpdesk Repair',
    'category': 'Services/Helpdesk',
    'summary': 'Project, Tasks, Repair',
    'depends': ['helpdesk_stock', 'repair'],
    'description': """
Repair Products from helpdesk tickets
    """,
    'data': [
        'views/repair_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'demo': ['data/helpdesk_repair_demo.xml'],
    'license': 'OEEL-1',
}
