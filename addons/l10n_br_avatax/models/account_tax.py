# Koda
from koda import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    l10n_br_avatax_code = fields.Char('Avatax Code', help='Technical field containing the Avatax identifier for this tax.', readonly=True)
