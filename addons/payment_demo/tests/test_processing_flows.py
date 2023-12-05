# Part of Odoo. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch

from koda.tests import tagged

from koda.addons.payment_demo.controllers.main import PaymentDemoController
from koda.addons.payment_demo.tests.common import PaymentDemoCommon
from koda.addons.payment.tests.http_common import PaymentHttpCommon


@tagged('-at_install', 'post_install')
class TestProcessingFlows(PaymentDemoCommon, PaymentHttpCommon):

    def test_portal_payment_triggers_processing(self):
        """ Test that paying from the frontend triggers the processing of the notification data. """
        self._create_transaction(flow='direct')
        url = self._build_url(PaymentDemoController._simulation_url)
        with patch(
            'koda.addons.payment.models.payment_transaction.PaymentTransaction'
            '._handle_notification_data'
        ) as handle_notification_data_mock:
            self.make_jsonrpc_request(url, params=self.notification_data)
        self.assertEqual(handle_notification_data_mock.call_count, 1)
