# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sla_id = fields.Many2one(
        "helpdesk.sla", string="SLA Policy",
        company_dependent=True,
        help="SLA Policy that will automatically apply to the tickets linked to a sales order item containing this service.")
