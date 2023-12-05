# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'


    l10n_lt_official_social_security = fields.Char(string="Social Security Number")
