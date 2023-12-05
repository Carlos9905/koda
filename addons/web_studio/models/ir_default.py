# -*- coding: utf-8 -*-
# Koda

from koda import models


class IrDefault(models.Model):
    _name = 'ir.default'
    _inherit = ['studio.mixin', 'ir.default']
