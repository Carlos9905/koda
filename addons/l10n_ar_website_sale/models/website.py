# -*- coding: utf-8 -*-
# Koda

from koda import models


class Website(models.Model):
    _inherit = "website"

    def _display_partner_b2b_fields(self):
        """ Argentinean localization must always display b2b fields """
        self.ensure_one()
        return self.company_id.country_id.code == "AR" or super()._display_partner_b2b_fields()
