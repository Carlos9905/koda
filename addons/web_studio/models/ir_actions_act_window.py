# -*- coding: utf-8 -*-
# Koda

from koda import models


class IrActionsActWindow(models.Model):
    _name = 'ir.actions.act_window'
    _inherit = ['studio.mixin', 'ir.actions.act_window']


class IrActionsActWindowView(models.Model):
    _name = 'ir.actions.act_window.view'
    _inherit = ['studio.mixin', 'ir.actions.act_window.view']
