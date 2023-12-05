# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_ma_employer_contribution = fields.Float(string="Employer's contribution")
    l10n_ma_social_security_organization = fields.Char(string="Social security organization")
    l10n_ma_collective_agreement = fields.Char(string="Collective agreement")
