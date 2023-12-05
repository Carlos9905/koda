# Koda

import koda.tests


@koda.tests.tagged('post_install', '-at_install')
class TestUi(koda.tests.HttpCase):

    def test_01_project_tour(self):
        self.start_tour("/web", 'project_tour', login="admin")
