# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    intrastat = fields.Boolean(string='Intrastat member')
