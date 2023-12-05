# Koda

from koda import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wa_sale_template_id = fields.Many2one(related="website_id.wa_sale_template_id", readonly=False)
