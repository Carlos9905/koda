# -*- coding: utf-8 -*-
# Koda

from koda import models


class AppointmentType(models.Model):
    _inherit = "appointment.type"

    def _populate(self, size):
        appointment_types = super()._populate(size)
        appointment_types.is_published = True
        return appointment_types
