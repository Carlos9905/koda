# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class Pricelist(models.Model):
    _inherit = "product.pricelist"

    product_subscription_pricing_ids = fields.One2many(
        'sale.subscription.pricing',
        'pricelist_id',
        string="Recurring Pricing",
        domain=[
            '|', ('product_template_id', '=', None), ('product_template_id.active', '=', True),
        ],
    )
