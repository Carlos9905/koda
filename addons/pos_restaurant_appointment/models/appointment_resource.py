# -*- coding: utf-8 -*-
# Koda
from koda import fields, models

class AppointmentResource(models.Model):
    _inherit = 'appointment.resource'

    # this should be one2one
    pos_table_ids = fields.One2many('restaurant.table', 'appointment_resource_id', string='POS Table')
