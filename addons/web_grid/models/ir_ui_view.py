# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models


class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('grid', "Grid")])
