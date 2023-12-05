# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class FollowupLine(models.Model):
    _inherit = 'account_followup.followup.line'

    send_letter = fields.Boolean('Send a Letter', default=True)
