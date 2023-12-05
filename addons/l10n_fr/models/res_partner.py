# -*- coding: utf-8 -*-
# Koda
from koda import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    siret = fields.Char(string='SIRET', size=14)
