# -*- coding: utf-8 -*-
# Koda

from koda import models
from koda.osv.expression import OR


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super(PosSession, self)._loader_params_product_product()
        if self.config_id.module_pos_discount:
            result['search_params']['domain'] = OR([result['search_params']['domain'], [('id', '=', self.config_id.discount_product_id.id)]])
        return result
