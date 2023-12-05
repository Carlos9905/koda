# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    team_id = fields.Many2one(comodel_name='crm.team', string="Sales Team")

    def _select(self):
        return super()._select() + ", move.team_id as team_id"
