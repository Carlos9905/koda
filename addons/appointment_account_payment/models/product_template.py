# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[
        ('booking_fees', 'Booking Fees'),
    ], ondelete={'booking_fees': 'set service'})

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['booking_fees'] = 'service'
        return type_mapping
