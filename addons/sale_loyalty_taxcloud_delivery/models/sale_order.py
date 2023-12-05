# -*- coding: utf-8 -*-
# Koda

from .taxcloud_request import TaxCloudRequest
from koda import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_TaxCloudRequest(self, api_id, api_key):
        return TaxCloudRequest(api_id, api_key)
