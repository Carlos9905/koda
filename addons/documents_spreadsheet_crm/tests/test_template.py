# -*- coding: utf-8 -*-
# Koda

import koda
from koda.tests import tagged
from koda.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestSpreadsheetTemplate(HttpCase):

    def test_insert_pivot_in_spreadsheet(self):
        self.start_tour('/web', 'insert_crm_pivot_in_spreadsheet', login='admin')
