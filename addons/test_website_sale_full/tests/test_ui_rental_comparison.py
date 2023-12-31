# -*- coding: utf-8 -*-
# Koda

from koda.tests import HttpCase, tagged
from koda.addons.website_sale_renting.tests.common import TestWebsiteSaleRentingCommon

@tagged('-at_install', 'post_install')
class TestUi(HttpCase, TestWebsiteSaleRentingCommon):

    def test_website_sale_renting_comparison_ui(self):
        self.attribute_processor = self.env['product.attribute'].create({
            'name': 'Processor',
            'sequence': 1,
        })
        self.values_processor = self.env['product.attribute.value'].create([{
            'name': name,
            'attribute_id': self.attribute_processor.id,
            'sequence': i,
        } for i, name in enumerate(['i3', 'i5', 'i7'])])
        self.attribute_line_processor = self.env['product.template.attribute.line'].create([{
            'product_tmpl_id': self.computer.product_tmpl_id.id,
            'attribute_id': self.attribute_processor.id,
            'value_ids': [(6, 0, v.ids)],
        } for v in self.values_processor])
        self.computer.is_published = True
        self.start_tour("/web", 'shop_buy_rental_product_comparison', login='admin')
