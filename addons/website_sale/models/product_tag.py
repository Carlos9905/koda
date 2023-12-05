# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class ProductTag(models.Model):
    _name = 'product.tag'
    _inherit = ['website.multi.mixin', 'product.tag']

    visible_on_ecommerce = fields.Boolean(
        string="Visible on eCommerce",
        help="Whether the tag is displayed on the eCommerce.",
        default=True,
    )
    image = fields.Image(string="Image", max_width=50, max_height=50)
