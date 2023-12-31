# -*- coding: utf-8 -*-
# Koda

from datetime import datetime

import koda.tests
from koda.tests.common import HttpCase


@koda.tests.tagged('post_install', '-at_install')
class TestFrontDeskURL(HttpCase):
    # -------------------------------------------------------------------------
    # TESTS
    # -------------------------------------------------------------------------
    def test_frontdesk_ui(self):
        '''Testing the UI of the Frontdesk module'''
        station = self.env['frontdesk.frontdesk'].search([('name', '=', 'Office 1')])
        kiosk_values = station.action_open_kiosk()
        access_url = kiosk_values.get('url')
        self.env.ref('frontdesk.frontdesk_visitor_1').check_in = datetime.now()

        self.start_tour(access_url, 'quick_check_in_tour', login='admin')
        station.drink_offer = True
        self.start_tour(access_url, 'frontdesk_basic_tour', login='admin')
        station.write({
            'host_selection': True,
            'ask_email': 'required',
        })
        self.start_tour(access_url, 'required_fields_tour', login='admin')
