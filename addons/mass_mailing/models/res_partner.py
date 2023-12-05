# -*- coding: utf-8 -*-
# Koda

from koda import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
