# Part of Odoo. See LICENSE file for full copyright and licensing details.

from koda import models
from koda.osv import expression

class Website(models.Model):
    _inherit = 'website'

    def _product_domain(self):
        return expression.OR([[('rent_ok', '=', True)], super()._product_domain()])
