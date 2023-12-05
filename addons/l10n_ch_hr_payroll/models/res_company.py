# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_ch_post_box = fields.Char(string="Post Box")
    l10n_ch_uid = fields.Char(string="Identification Number (IDE-OFS)")
