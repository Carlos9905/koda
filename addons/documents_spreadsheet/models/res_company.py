# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    documents_spreadsheet_folder_id = fields.Many2one('documents.folder', check_company=True,
        default=lambda self: self.env.ref('documents_spreadsheet.documents_spreadsheet_folder', raise_if_not_found=False))
