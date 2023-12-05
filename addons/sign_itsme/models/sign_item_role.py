# -*- coding: utf-8 -*-
# Koda

from koda import fields, models

class SignItemParty(models.Model):
    _inherit = "sign.item.role"

    auth_method = fields.Selection(selection_add=[
        ('itsme', 'Via itsme®')
    ], ondelete={'itsme': 'cascade'})
