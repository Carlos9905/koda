# -*- coding: utf-8 -*-
# Koda

from koda import models


class Groups(models.Model):
    _name = 'res.groups'
    _inherit = ['studio.mixin', 'res.groups']
