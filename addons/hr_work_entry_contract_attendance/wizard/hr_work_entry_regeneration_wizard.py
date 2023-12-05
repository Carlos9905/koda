# -*- coding:utf-8 -*-
# Koda

from koda import models

class HrWorkEntryRegenerationWizard(models.TransientModel):
    _inherit = 'hr.work.entry.regeneration.wizard'

    def _work_entry_fields_to_nullify(self):
        return super()._work_entry_fields_to_nullify() + ['attendance_id']
