# Koda

from koda import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_whatsapp_safe_fields(self):
        return {'partner_id.name', 'name', 'company_id.name', 'currency_id.symbol', 'amount'}
