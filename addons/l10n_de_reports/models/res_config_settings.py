# Koda
from koda import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_de_datev_account_length = fields.Integer(related='company_id.l10n_de_datev_account_length', readonly=False)
