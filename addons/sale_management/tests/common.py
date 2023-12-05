# -*- coding: utf-8 -*-
# Koda

from koda.addons.sale.tests.common import SaleCommon

class SaleManagementCommon(SaleCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.empty_order_template = cls.env['sale.order.template'].create({
            'name': "Test Quotation Template",
        })
