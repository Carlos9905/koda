#-*- coding:utf-8 -*-
# Koda

from koda import fields, models

class HrWorkEntry(models.Model):
    _inherit = 'hr.work.entry'

    attendance_id = fields.Many2one('hr.attendance', 'Attendance')
