# Koda
{
    'name': "Spreadsheet dashboard for subscriptions",
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard', 'sale_subscription'],
    'data': [
        "data/dashboards.xml",
    ],
    'installable': True,
    'auto_install': ['sale_subscription'],
    'license': 'OEEL-1',
}
