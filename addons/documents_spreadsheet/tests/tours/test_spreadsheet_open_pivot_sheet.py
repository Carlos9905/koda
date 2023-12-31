# -*- coding: utf-8 -*-
# Koda

from ..common import SpreadsheetTestCommon

from koda.tests import tagged
from koda.tests.common import HttpCase
from koda.tools import file_open, misc

@tagged("post_install", "-at_install")
class TestSpreadsheetOpenPivot(SpreadsheetTestCommon, HttpCase):
    @classmethod
    def setUpClass(cls):
        super(TestSpreadsheetOpenPivot, cls).setUpClass()
        data_path = misc.file_path('documents_spreadsheet/demo/files/res_partner_spreadsheet.json')
        # Avoid interference from the demo data which rename the admin user
        cls.env['res.users'].browse(2).write({"name": "AdminDude"})
        with file_open(data_path, 'rb') as f:
            cls.spreadsheet = cls.env["documents.document"].create({
                "handler": "spreadsheet",
                "folder_id": cls.folder.id,
                "raw": f.read(),
                "name": "Res Partner Test Spreadsheet"
            })

    def test_01_spreadsheet_open_pivot_as_admin(self):
        self.start_tour("/web", "spreadsheet_open_pivot_sheet", login="admin")

    def test_01_spreadsheet_open_pivot_as_user(self):
        self.start_tour("/web", "spreadsheet_open_pivot_sheet", login="spreadsheetDude")
