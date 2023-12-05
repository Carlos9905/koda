# -*- coding: utf-8 -*-
# Koda

from koda import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('optional_product_ids')
        return result
