# -*- coding: utf-8 -*-
# Koda

import koda.tests

@koda.tests.tagged("post_install", "-at_install")
class TestOdooEditor(koda.tests.HttpCase):

    def test_koda_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
