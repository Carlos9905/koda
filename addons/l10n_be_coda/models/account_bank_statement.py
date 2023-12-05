# -*- encoding: utf-8 -*-
# Koda

# Copyright (c) 2011 Noviat nv/sa (www.noviat.be). All rights reserved.

from koda import fields, models


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    coda_note = fields.Text('CODA Notes')
