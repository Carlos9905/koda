import koda.tests
from koda.tools import mute_logger


@koda.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(koda.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
