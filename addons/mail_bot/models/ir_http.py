# -*- coding: utf-8 -*-
# Koda

from koda import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user._is_internal():
            res['kodabot_initialized'] = self.env.user.kodabot_state not in [False, 'not_initialized']
        return res
