# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import koda.tests

@koda.tests.tagged("post_install", "-at_install")
class TestOdooEditor(koda.tests.HttpCase):

    def test_odoo_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
