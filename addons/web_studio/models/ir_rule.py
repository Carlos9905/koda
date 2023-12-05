# -*- coding: utf-8 -*-
# Koda

from koda import models


class IrRule(models.Model):
    _name = 'ir.rule'
    _description = 'Rule'
    _inherit = ['studio.mixin', 'ir.rule']
