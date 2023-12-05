# -*- coding: utf-8 -*-
# Koda

from odoo import fields, models


class HelpdeskStage(models.Model):
    _inherit = "helpdesk.stage"

    sms_template_id = fields.Many2one('sms.template', string="SMS Template",
        domain=[('model', '=', 'helpdesk.ticket')], help="SMS automatically sent to the customer when the ticket reaches this stage.")
