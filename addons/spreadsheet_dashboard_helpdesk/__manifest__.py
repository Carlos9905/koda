# Koda
{
    'name': "Spreadsheet dashboard for helpdesk",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'helpdesk'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['helpdesk'],
    'license': 'OEEL-1',
}
