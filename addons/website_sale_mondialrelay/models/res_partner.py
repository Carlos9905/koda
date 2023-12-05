# -*- coding: utf-8 -*-
# Koda

from koda import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _can_be_edited_by_current_customer(self, sale_order, mode):
        return super()._can_be_edited_by_current_customer(sale_order, mode) and not self.is_mondialrelay
