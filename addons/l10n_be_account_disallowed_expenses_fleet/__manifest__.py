# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Belgium - Disallowed Expenses Fleet',
    'countries': ['be'],
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
Disallowed Expenses Fleet Data for Belgium
    """,
    'depends': ['account_disallowed_expenses_fleet', 'l10n_be_hr_payroll_fleet'],
    'data': ['views/fleet_vehicle_views.xml'],
    'installable': True,
    'auto_install': True,
    'website': 'https://www.koda.com/app/accounting',
    'license': 'OEEL-1',
}
