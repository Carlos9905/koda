# -*- coding: utf-8 -*-
# Koda

from koda import models


class IrActionsServer(models.Model):
    _name = 'ir.actions.server'
    _inherit = ['studio.mixin', 'ir.actions.server']
