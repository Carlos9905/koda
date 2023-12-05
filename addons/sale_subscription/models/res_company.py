# Koda

from koda import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Default subscription parameters
    subscription_default_plan_id = fields.Many2one('sale.subscription.plan', string='Default Recurrence')
