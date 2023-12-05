# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_holidays = fields.Float(string="Paid Time Off", default_model="hr.contract")
