# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    sms_template_id = fields.Many2one('sms.template', string="SMS Template",
        domain=[('model', '=', 'project.task')],
        help="If set, an SMS Text Message will be automatically sent to the customer when the task reaches this stage.")
