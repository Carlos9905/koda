# -*- coding: utf-8 -*-
# Koda
from unittest.mock import patch

import koda.tests
from koda.addons.pos_self_order.tests.self_order_common_test import SelfOrderCommonTest
# from koda.addons.pos_online_payment.models.pos_payment_method import PosPaymentMethod


@koda.tests.tagged("post_install", "-at_install")
class TestSelfOrderFrontendMobile(SelfOrderCommonTest):
    pass
