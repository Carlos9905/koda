# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class EventMenu(models.Model):
    _inherit = "website.event.menu"

    menu_type = fields.Selection(
        selection_add=[('social', 'Social Menus')],
        ondelete={'social': 'cascade'})
