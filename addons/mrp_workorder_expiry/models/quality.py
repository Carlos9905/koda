# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class QualityCheck(models.Model):
    _inherit = 'quality.check'

    is_expired = fields.Boolean(related='lot_id.product_expiry_alert')
