# -*- coding: utf-8 -*-
# Koda

from koda import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        res['aba_ct'] = {
            'mode': 'multi',
            'domain': [('type', '=', 'bank')],
            'currency_ids': self.env.ref("base.AUD").ids,
        }
        return res
