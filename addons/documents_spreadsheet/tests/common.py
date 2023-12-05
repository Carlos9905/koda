# -*- coding: utf-8 -*-
# Koda

from koda.tests.common import new_test_user
from koda.addons.spreadsheet_edition.tests.spreadsheet_test_case import SpreadsheetTestCase

from uuid import uuid4

TEST_CONTENT = "{}"
GIF = b"R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs="


class SpreadsheetTestCommon(SpreadsheetTestCase):
    @classmethod
    def setUpClass(cls):
        super(SpreadsheetTestCommon, cls).setUpClass()
        cls.folder = cls.env["documents.folder"].create({"name": "Test folder"})
        cls.spreadsheet_user = new_test_user(
            cls.env, login="spreadsheetDude", groups="documents.group_documents_user"
        )

    def create_spreadsheet(self, values=None, *, user=None, name="Untitled Spreadsheet"):
        if values is None:
            values = {}
        return (
            self.env["documents.document"]
            .with_user(user or self.env.user)
            .create({
                "spreadsheet_data": r"{}",
                "folder_id": self.folder.id,
                "handler": "spreadsheet",
                "mimetype": "application/o-spreadsheet",
                "name": name,
                **values,
            })
        )

    def share_spreadsheet(self, document):
        share = self.env["documents.share"].create(
            {
                "folder_id": document.folder_id.id,
                "document_ids": [(6, 0, [document.id])],
                "type": "ids",
            }
        )
        self.env["documents.shared.spreadsheet"].create(
            {
                "share_id": share.id,
                "document_id": document.id,
                "spreadsheet_data": document.spreadsheet_data,
            }
        )
        return share
