# -*- coding: utf-8 -*-
# Koda
from koda.addons.account.tests.common import AccountTestInvoicingHttpCommon

from koda.tests import tagged


@tagged('post_install', '-at_install')
class TestAccountReportsBuilderTour(AccountTestInvoicingHttpCommon):
    def test_account_reports_builder_tour(self):
        balance_sheet = self.env.ref('account_reports.balance_sheet')
        balance_sheet.name = "Mister Bigglesworth (ukulele)"

        self.start_tour("/web", "account_reports_builder", login=self.env.user.login)
