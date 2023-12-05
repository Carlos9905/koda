# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class DepartureReason(models.Model):
    _inherit = "hr.departure.reason"

    def _get_default_departure_reasons(self):
        return {
            **super()._get_default_departure_reasons(),
            'freelance': 350,
        }
