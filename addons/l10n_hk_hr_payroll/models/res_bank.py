# -*- coding: utf-8 -*-
# Koda

from koda import _, api, fields, models
from koda.exceptions import ValidationError


class ResBank(models.Model):
    _inherit = 'res.bank'

    # TODO: move this field to hr_payroll in master
    country_code = fields.Char(related='country.code', string='Country Code')
    l10n_hk_bank_code = fields.Char(string='Bank Code', size=3)

    @api.constrains('country', 'l10n_hk_bank_code')
    def _check_l10n_hk_bank_code(self):
        for bank in self:
            if bank.country_code == 'HK' and len(bank.l10n_hk_bank_code or '') != 3:
                raise ValidationError(_("Bank code length must be 3 letters."))
