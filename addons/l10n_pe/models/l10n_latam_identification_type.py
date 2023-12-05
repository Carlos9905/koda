# Koda
from koda import models, fields


class L10nLatamIdentificationType(models.Model):

    _inherit = "l10n_latam.identification.type"

    l10n_pe_vat_code = fields.Char()
