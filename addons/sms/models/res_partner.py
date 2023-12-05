# -*- coding: utf-8 -*-
# Koda

from koda import models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['mail.thread.phone', 'res.partner']
