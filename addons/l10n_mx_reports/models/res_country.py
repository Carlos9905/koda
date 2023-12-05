# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class Country(models.Model):
    _inherit = 'res.country'

    demonym = fields.Char(translate=True, help="Adjective for relationship"
                          " between a person and a country.")
