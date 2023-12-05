# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # technical field used to reconcile the journal items in Odoo as they were in Winbooks
    winbooks_matching_number = fields.Char(help="Matching number that was used in Winbooks")  # DEPRECATED in 17.0
    winbooks_line_id = fields.Char(help="Line ID that was used in Winbooks")
