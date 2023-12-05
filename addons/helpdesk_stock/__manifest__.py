# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Helpdesk Stock',
    'category': 'Services/Helpdesk',
    'summary': 'Project, Tasks, Stock',
    'depends': ['helpdesk_sale', 'stock'],
    'description': """
Manage Product returns from helpdesk tickets
    """,
    'data': [
        'wizard/stock_picking_return_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'demo': ['data/helpdesk_stock_demo.xml'],
    'license': 'OEEL-1',
}
