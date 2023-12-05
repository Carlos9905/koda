# Koda

from koda import fields, models


class HrWorkEntryType(models.Model):
    _inherit = 'hr.work.entry.type'

    l10n_au_penalty_rate = fields.Float("Penalty Rate")
