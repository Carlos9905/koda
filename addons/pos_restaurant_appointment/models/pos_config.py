  # -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    appointment_type_ids = fields.Many2many('appointment.type', string='Appointment Type')
