# Koda
# -*- coding: utf-8 -*-

import koda.tests


@koda.tests.tagged('post_install', '-at_install')
class TestUi(koda.tests.HttpCase):
    def test_ui(self):
        self.start_tour("/web", 'helpdesk_tour', login="admin")
