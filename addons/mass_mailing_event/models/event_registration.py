# -*- coding: utf-8 -*-
# Koda

from koda import models


class EventRegistration(models.Model):
    _inherit = 'event.registration'
    _mailing_enabled = True

    def _mailing_get_default_domain(self, mailing):
        return [('state', '!=', 'cancel')]
