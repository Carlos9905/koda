# -*- coding: utf-8 -*-
# Koda

from koda import models


class Users(models.Model):
    _inherit = 'res.users'

    def get_totp_invite_url(self):
        if not self._is_internal():
            return '/my/security'
        else:
            return super(Users, self).get_totp_invite_url()
