# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models


class TestModel(models.Model):
    """ Add website option in server actions. """

    _name = 'test.model'
    _inherit = [
        'website.seo.metadata',
        'website.published.mixin',
        'website.searchable.mixin',
    ]
    _description = 'Website Model Test'

    name = fields.Char(required=True)

    @api.model
    def _search_get_detail(self, website, order, options):
        return {
            'model': 'test.model',
            'base_domain': [],
            'search_fields': ['name'],
            'fetch_fields': ['name'],
            'mapping': {
                'name': {'name': 'name', 'type': 'text', 'match': True},
                'website_url': {'name': 'name', 'type': 'text', 'truncate': False},
            },
            'icon': 'fa-check-square-o',
            'order': 'name asc, id desc',
        }


class TestModelExposed(models.Model):
    _name = "test.model.exposed"
    _inherit = [
        'website.seo.metadata',
        'website.published.mixin',
    ]
    _description = 'Website Model Test Exposed'
    _rec_name = "name"

    name = fields.Char()
