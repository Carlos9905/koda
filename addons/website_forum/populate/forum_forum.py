# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.tools import populate

class Forum(models.Model):
    _inherit = 'forum.forum'
    _populate_sizes = {'small': 1, 'medium': 3, 'large': 10}

    def _populate_factories(self):
        return [
            ('name', populate.constant('Forum_{counter}')),
            ('description', populate.constant('This is forum number {counter}'))
        ]
