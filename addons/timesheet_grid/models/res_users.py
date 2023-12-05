# -*- coding: utf-8 -*-
# Koda

from koda import fields, models, _
from koda.exceptions import UserError


class User(models.Model):
    _inherit = ['res.users']

    timesheet_manager_id = fields.Many2one(related='employee_id.timesheet_manager_id')

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['timesheet_manager_id']

    def get_last_validated_timesheet_date(self):
        if self.user_has_groups('hr_timesheet.group_timesheet_manager'):
            return False

        if not self.user_has_groups('hr_timesheet.group_hr_timesheet_user'):
            raise UserError(_('You are not allowed to see timesheets.'))

        return self.sudo().employee_id.last_validated_timesheet_date
