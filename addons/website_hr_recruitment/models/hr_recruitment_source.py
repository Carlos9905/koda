# -*- coding: utf-8 -*-
# Koda

from werkzeug import urls

from koda import api, fields, models


class RecruitmentSource(models.Model):
    _inherit = 'hr.recruitment.source'

    url = fields.Char(compute='_compute_url', string='Url Parameters')

    @api.depends('source_id', 'source_id.name', 'job_id', 'job_id.company_id')
    def _compute_url(self):
        for source in self:
            source.url = urls.url_join(source.job_id.get_base_url(), "%s?%s" % (
                source.job_id.website_url,
                urls.url_encode({
                    'utm_campaign': self.env.ref('hr_recruitment.utm_campaign_job').name,
                    'utm_medium': source.medium_id.name or self.env.ref('utm.utm_medium_website').name,
                    'utm_source': source.source_id.name
                })
            ))
