# -*- coding: utf-8 -*-
# Koda

from koda.addons.appointment.controllers.calendar_view import AppointmentCalendarView
from koda.http import request
from koda.osv.expression import AND


class AppointmentCrmCalendarView(AppointmentCalendarView):

    def _get_staff_user_appointment_invite_domain(self, appointment_type):
        domain = super()._get_staff_user_appointment_invite_domain(appointment_type)
        if 'default_opportunity_id' in request.env.context:
            domain = AND([domain, [('opportunity_id', '=', request.env.context['default_opportunity_id'])]])
        return domain
