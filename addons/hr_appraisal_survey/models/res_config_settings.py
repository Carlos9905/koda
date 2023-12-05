# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    appraisal_survey_template_id = fields.Many2one(
        'survey.survey', related='company_id.appraisal_survey_template_id', domain=[('survey_type', '=', 'appraisal')], readonly=False)
