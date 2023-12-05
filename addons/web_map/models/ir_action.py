# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[
        ('map', "Map")
    ], ondelete={'map': 'cascade'})
