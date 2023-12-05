# -*- coding: utf-8 -*-
# Koda

{
    'name': "Employees on Appointments",
    'version': "1.0",
    'category': 'Services/Appointment',
    'sequence': 2140,
    'summary': "Manage Appointments with Employees",
    'website': 'https://www.koda.com/app/appointments',
    'description': """
Take into account the working schedule (sick leaves, part time, ...) of employees when scheduling appointments
--------------------------------------------------------------------------------------------------------------
""",
    'depends': ['appointment', 'hr'],
    'data': [
        'views/appointment_type_views.xml',
        'views/calendar_event_views.xml'
    ],
    'auto_install': True,
    'license': 'OEEL-1',
}
