# -*- coding: utf-8 -*-
# Koda

from koda import models


class GamificationBadge(models.Model):
    _name = 'gamification.badge'
    _inherit = ['gamification.badge', 'website.published.mixin']
