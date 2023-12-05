# -*- coding: utf-8 -*-
# Koda

from koda import models, fields, api, _

class CalendarEventRecruitment(models.Model):
    _inherit = 'calendar.event'

    applicant_id = fields.Many2one(related="appointment_invite_id.applicant_id", readonly=False, store=True)
