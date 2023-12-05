# -*- coding: utf-8 -*-
# Koda

from koda import api, models


class PublisherWarrantyContract(models.AbstractModel):
    _inherit = "publisher_warranty.contract"
    _description = 'Publisher Warranty Contract For IoT Box'

    @api.model
    def _get_message(self):
        msg = super(PublisherWarrantyContract, self)._get_message()
        msg['IoTBox'] = self.env['iot.box'].search_count([])
        return msg
