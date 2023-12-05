# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.osv import expression


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return expression.AND([
            super().sale_product_domain(),
            [('detailed_type', '!=', 'booking_fees')],
        ])
