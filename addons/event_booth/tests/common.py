# -*- coding: utf-8 -*-
# Koda

from koda.addons.event.tests.common import EventCase


class TestEventBoothCommon(EventCase):

    @classmethod
    def setUpClass(cls):
        super(TestEventBoothCommon, cls).setUpClass()

        cls.event_booth_category_1 = cls.env['event.booth.category'].create({
            'name': 'Standard',
            'description': '<p>Standard</p>',
        })
        cls.event_booth_category_2 = cls.env['event.booth.category'].create({
            'name': 'Premium',
            'description': '<p>Premium</p>',
        })
