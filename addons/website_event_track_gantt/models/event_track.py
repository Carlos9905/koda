# -*- coding: utf-8 -*-
# Koda

from koda import models


class Track(models.Model):
    _inherit = 'event.track'

    def action_unschedule(self):
        self.ensure_one()
        self.date = None
        self.date_end = None
        return {'type': 'ir.actions.act_window_close'}
