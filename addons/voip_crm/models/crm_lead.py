# Part of Odoo. See LICENSE file for full copyright and licensing details.

from koda import models


class CrmLead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead", "voip.queue.mixin"]
