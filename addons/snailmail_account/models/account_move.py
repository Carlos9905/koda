# -*- coding: utf-8 -*-
# Koda

from koda import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_pdf_and_send_invoice_vals(self, template, **kwargs):
        # EXTENDS account
        vals = super()._get_pdf_and_send_invoice_vals(template, **kwargs)
        vals['checkbox_send_by_post'] = False
        return vals
