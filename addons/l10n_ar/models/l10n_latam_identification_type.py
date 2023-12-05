# Part of Odoo. See LICENSE file for full copyright and licensing details.
from koda import models, fields


class L10nLatamIdentificationType(models.Model):

    _inherit = "l10n_latam.identification.type"

    l10n_ar_afip_code = fields.Char("AFIP Code")
