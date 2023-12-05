# -*- coding: utf-8 -*-
# Koda

import koda.tests
from koda.tools import mute_logger


@koda.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(koda.tests.HttpCase):

    @mute_logger('koda.addons.http_routing.models.ir_http', 'koda.http')
    def test_01_run_tour(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'test_custom_snippet', login="admin")
