# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Helpdesk - CRM',
    'summary': 'Convert Tickets from/to Leads',
    'version': '1.1',
    'sequence': 19,
    'category': 'Services/Helpdesk',
    'description': """
Convert business inquiries that have ended up in the Helpdesk pipeline by mistake,
or generate a ticket from a business inquiry
        """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/crm_lead_convert2ticket_views.xml',
        'wizard/helpdesk_ticket_to_lead_views.xml',
        'views/crm_lead_views.xml',
    ],
    'depends': ['crm', 'helpdesk'],
    'auto_install': True,
    'license': 'OEEL-1',
}
