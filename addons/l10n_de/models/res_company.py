# -*- coding: utf-8 -*-
# Koda

from koda import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_de_stnr = fields.Char(string="St.-Nr.", help="Tax number. Scheme: ??FF0BBBUUUUP, e.g.: 2893081508152 https://de.wikipedia.org/wiki/Steuernummer")
    l10n_de_widnr = fields.Char(string="W-IdNr.", help="Business identification number.")
