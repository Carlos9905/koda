# -*- coding: utf-8 -*-
from koda import models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def _get_payment_receipt_report_values(self):
        # EXTENDS 'account'
        values = super()._get_payment_receipt_report_values()

        cfdi_infos = self.move_id._l10n_mx_edi_get_extra_payment_report_values()
        if cfdi_infos:
            values.update({
                'display_invoices': False,
                'display_payment_method': False,
                'cfdi': cfdi_infos,
            })

        return values

    def l10n_mx_edi_cfdi_payment_force_try_send(self):
        self.move_id.l10n_mx_edi_cfdi_payment_force_try_send()

    def l10n_mx_edi_cfdi_try_sat(self):
        self.move_id.l10n_mx_edi_cfdi_try_sat()
