# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class LoyaltyMail(models.Model):
    _inherit = 'loyalty.mail'

    pos_report_print_id = fields.Many2one('ir.actions.report', string="Print Report", domain=[('model', '=', 'loyalty.card')],
        help="The report action to be executed when creating a coupon/gift card/loyalty card in the PoS.",
    )
