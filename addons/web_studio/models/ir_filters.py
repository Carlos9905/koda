# -*- coding: utf-8 -*-
# Koda

from koda import models


class IrFilters(models.Model):
    _name = 'ir.filters'
    _inherit = ['studio.mixin', 'ir.filters']
