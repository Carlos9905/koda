# -*- coding: utf-8 -*-
# Koda

from koda import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_pos_payment_method(self):
        result = super()._loader_params_pos_payment_method()
        result['search_params']['fields'].append('pos_mercury_config_id')
        return result
