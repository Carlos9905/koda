# -*- coding: utf-8 -*-
# Koda

from koda import api, models, _


class Channel(models.Model):
    _inherit = 'discuss.channel'

    def execute_command_help(self, **kwargs):
        super().execute_command_help(**kwargs)
        self.env['mail.bot']._apply_logic(self, kwargs, command="help")  # kwargs are not usefull but...
