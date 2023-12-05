# -*- coding: utf-8 -*-
# Koda

from koda import models, api


class ProjectTaskRecurrence(models.Model):
    _inherit = 'project.task.recurrence'

    @api.model
    def _get_recurring_fields_to_postpone(self):
        return super()._get_recurring_fields_to_postpone() + [
            'planned_date_begin',
        ]
