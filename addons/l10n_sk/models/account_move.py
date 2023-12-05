# Part of Odoo. See LICENSE file for full copyright and licensing details.
from koda import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    taxable_supply_date = fields.Date()
