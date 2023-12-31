# -*- coding: utf-8 -*-
# Koda

from koda.tests import tagged
from koda.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestSpreadsheetMultipage(HttpCase):
    def test_01_spreadsheet_save_multipage(self):
        self.start_tour("/web", "spreadsheet_save_multipage", login="admin")
