# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class DepartureReason(models.Model):
    _inherit = "hr.departure.reason"

    l10n_hk_ir56f_code = fields.Char()
