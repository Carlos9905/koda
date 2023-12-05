# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class Alarm(models.Model):
    _inherit = "calendar.alarm"

    default_for_new_appointment_type = fields.Boolean(
        "New Appointments Default", help="Use as default for new Appointment Types")
