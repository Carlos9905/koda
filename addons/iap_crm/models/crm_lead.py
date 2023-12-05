# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    reveal_id = fields.Char(string='Reveal ID') # Technical ID of reveal request done by IAP

    def _merge_get_fields(self):
        return super(Lead, self)._merge_get_fields() + ['reveal_id']
