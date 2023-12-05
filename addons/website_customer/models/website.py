# -*- coding: utf-8 -*-
# Koda

from koda import models, _
from koda.addons.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = "website"

    def get_suggested_controllers(self):
        suggested_controllers = super(Website, self).get_suggested_controllers()
        suggested_controllers.append((_('References'), url_for('/customers'), 'website_customer'))
        return suggested_controllers
