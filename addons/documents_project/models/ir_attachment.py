# -*- coding: utf-8 -*-
# Koda


from koda import fields, models


class IrAttachment(models.Model):
    _inherit = ['ir.attachment']

    document_ids = fields.One2many('documents.document', 'attachment_id')
