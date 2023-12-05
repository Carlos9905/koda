# Part of Odoo. See LICENSE file for full copyright and licensing details.

from koda import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    trade_registry = fields.Char()

class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    account_fiscal_country_id = fields.Many2one(related="company_id.account_fiscal_country_id")
    company_registry = fields.Char(related='company_id.company_registry')
