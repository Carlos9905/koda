# -*- coding: utf-8 -*-
# Koda

from koda import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_pos_printer(self):
        result = super()._loader_params_pos_printer()
        result['search_params']['fields'].append('epson_printer_ip')
        return result
