# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models, _
from koda.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    sdworx_code = fields.Char("SDWorx code", groups="hr.group_hr_user")

    @api.constrains('sdworx_code')
    def _check_sdworx_code(self):
        if self.sdworx_code and len(self.sdworx_code) != 7:
            raise ValidationError(_('The code should have 7 characters!'))
