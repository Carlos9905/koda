# coding: utf-8
# Koda

from koda import models


class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    def _get_payment_terminal_selection(self):
        return super()._get_payment_terminal_selection() + [('six_iot', 'SIX IOT')]
