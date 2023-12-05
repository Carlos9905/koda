import koda.tests
from koda.tools import mute_logger


@koda.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(koda.tests.HttpCase):

    @mute_logger('koda.addons.http_routing.models.ir_http', 'koda.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
