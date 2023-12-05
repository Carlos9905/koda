# -*- coding: utf-8 -*-
# Koda

from koda import models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    def _get_sign_request_folder(self):
        self.ensure_one()
        return self.company_id.documents_payroll_folder_id or super()._get_sign_request_folder()
