# -*- coding: utf-8 -*-
# Koda

from koda import api, models


class ProjectTaskRecurrence(models.Model):
    _inherit = 'project.task.recurrence'

    @api.model
    def _get_recurring_fields_to_copy(self):
        return ['partner_phone'] + super()._get_recurring_fields_to_copy()
