# -*- coding: utf-8 -*-
# Koda

from koda import models


class BaseAutomation(models.Model):
    _name = 'base.automation'
    _inherit = ['studio.mixin', 'base.automation']
