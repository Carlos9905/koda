# -*- coding: utf-8 -*-
# Koda

from koda.tests import HttpCase, tagged

@tagged('-at_install', 'post_install')
class TestUi(HttpCase):
    def test_01_ui(self):
        self.start_tour("/", 'project_test_tour', login='admin')
