# -*- coding: utf-8 -*-
# Koda

from koda import models, fields


class MailActivityType(models.Model):
    _inherit = "mail.activity.type"

    tag_ids = fields.Many2many('documents.tag')
    folder_id = fields.Many2one('documents.folder',
                                help="By defining a folder, the upload activities will generate a document")
