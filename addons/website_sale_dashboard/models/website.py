# -*- coding: utf-8 -*-
# Koda

import logging

from koda import api, models, fields

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def action_dashboard_redirect(self):
        if self.env.user.has_group('sales_team.group_sale_salesman'):
            return self.env["ir.actions.actions"]._for_xml_id("website_sale_dashboard.sale_dashboard")
        return super(Website, self).action_dashboard_redirect()
