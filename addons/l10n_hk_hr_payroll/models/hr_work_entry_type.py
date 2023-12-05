# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class HrWorkEntryType(models.Model):
    _inherit = 'hr.work.entry.type'

    l10n_hk_use_713 = fields.Boolean("Use 713")
    l10n_hk_non_full_pay = fields.Boolean("Non-full pay")
