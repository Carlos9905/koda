# Koda
from koda import models, fields


class ResCompany(models.Model):

    _inherit = 'res.company'

    l10n_ar_computable_tax_credit = fields.Selection(
        [('wo_prorate', 'Without Prorate'), ('global', 'Global')],
        string="Computable Tax Credit: Prorate Options",
        default='wo_prorate')
