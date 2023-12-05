# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class HrReferralLevel(models.Model):
    _name = 'hr.referral.level'
    _description = 'Level for referrals'
    _order = 'points'

    name = fields.Char(required=True, string='Level Name')
    points = fields.Integer(required=True)
    image = fields.Binary(required=True)
