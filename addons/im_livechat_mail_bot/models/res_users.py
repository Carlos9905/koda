# -*- coding: utf-8 -*-
# Koda

from koda import models, fields


class Users(models.Model):
    _inherit = 'res.users'

    kodabot_state = fields.Selection(selection_add=[
        ('onboarding_canned', 'Onboarding canned'),
    ], ondelete={'onboarding_canned': lambda users: users.write({'kodabot_state': 'disabled'})})
