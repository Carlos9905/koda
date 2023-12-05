# -*- coding: utf-8 -*-
# Koda

import koda.tests
from koda.addons.website.tests.test_configurator import TestConfiguratorCommon

@koda.tests.common.tagged('post_install', '-at_install')
class TestConfigurator(TestConfiguratorCommon):

    def test_01_configurator_flow(self):
        self.start_tour('/web#action=website.action_website_configuration', 'configurator_flow', login="admin")
