# -*- coding: utf-8 -*-
# Koda

from koda import models


class Digest(models.Model):
    _inherit = 'digest.digest'

    def _compute_kpis_actions(self, company, user):
        res = super(Digest, self)._compute_kpis_actions(company, user)
        res['kpi_website_sale_total'] = 'website_sale_dashboard.sale_dashboard&menu_id=%s' % self.env.ref('website.menu_website_configuration').id
        return res
