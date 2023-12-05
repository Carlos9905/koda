# -*- encoding: utf-8 -*-
# Koda

from koda import api, fields, models


class QualityCheck(models.Model):
    _inherit = "quality.check"

    batch_id = fields.Many2one(related='picking_id.batch_id')
