# -*- coding: utf-8 -*-
# Koda
{
    'name': "Spreadsheet dashboard for CRM",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'crm_enterprise'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['crm_enterprise'],
    'license': 'OEEL-1',
}
