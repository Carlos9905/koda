# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import koda.tests

@koda.tests.common.tagged('post_install', '-at_install')
class TestWebsitePageManager(koda.tests.HttpCase):

    def test_01_page_manager(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'website_page_manager', login="admin")
