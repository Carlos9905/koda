# Koda

import logging
import koda.tests

_logger = logging.getLogger(__name__)


@koda.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(koda.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "koda.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere('%s');" % menus[app_id]['xmlid'], "koda.isReady === true", login="admin", timeout=1200)


@koda.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(koda.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_demo(self):
        user_demo = self.env.ref("base.user_demo")
        menus = self.env['ir.ui.menu'].with_user(user_demo.id).load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "koda.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere('%s');" % menus[app_id]['xmlid'], "koda.isReady === true", login="demo", timeout=1200)

@koda.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(koda.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "koda.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere(undefined, true);", "koda.isReady === true", login="admin", timeout=120)

@koda.tests.tagged('post_install', '-at_install')
class TestMenusDemoLight(koda.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_demo(self):
        self.browser_js("/web", "koda.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere(undefined, true);", "koda.isReady === true", login="demo", timeout=120)
