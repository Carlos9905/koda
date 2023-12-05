# -*- coding: utf-8 -*-
# Koda

from koda.tests import HttpCase, tagged
from koda.addons.website_sale_renting.tests.common import TestWebsiteSaleRentingCommon

@tagged('-at_install', 'post_install')
class TestUi(HttpCase, TestWebsiteSaleRentingCommon):

    def test_website_sale_renting_wishlist_ui(self):
        self.computer.is_published = True
        self.start_tour("/web", 'shop_buy_rental_product_wishlist', login='admin')
