# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class FleetVehicleState(models.Model):
    _name = 'fleet.vehicle.state'
    _order = 'sequence asc'
    _description = 'Vehicle Status'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()

    _sql_constraints = [('fleet_state_name_unique', 'unique(name)', 'State name already exists')]
