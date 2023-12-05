# coding: utf-8
# Koda

from koda import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_social_demo = fields.Boolean('Enable Demo Mode', groups="base.group_system")
