# Koda
from koda import fields, models, api, _


class AccountFiscalPosition(models.Model):

    _inherit = 'account.fiscal.position'

    l10n_ar_afip_responsibility_type_ids = fields.Many2many(
        'l10n_ar.afip.responsibility.type', 'l10n_ar_afip_reponsibility_type_fiscal_pos_rel',
        string='AFIP Responsibility Types', help='List of AFIP responsibilities where this fiscal position '
        'should be auto-detected')

    @api.model
    def _get_fiscal_position(self, partner, delivery=None):
        """ Take into account the partner afip responsibility in order to auto-detect the fiscal position """
        if self.env.company.country_id.code != "AR":
            return super()._get_fiscal_position(partner, delivery=delivery)

        # if no delivery use invoicing
        if not delivery:
            delivery = partner

        # partner manually set fiscal position always win
        manual_fiscal_position = delivery.property_account_position_id or partner.property_account_position_id
        if manual_fiscal_position:
            return manual_fiscal_position

        domain = [
            ('auto_apply', '=', True),
            ('l10n_ar_afip_responsibility_type_ids', '=', partner.l10n_ar_afip_responsibility_type_id.id),
            ('company_id', '=', self.env.company.id),
        ]
        return self.sudo().search(domain, limit=1)

    @api.onchange('l10n_ar_afip_responsibility_type_ids', 'country_group_id', 'country_id', 'zip_from', 'zip_to')
    def _onchange_afip_responsibility(self):
        if self.company_id.account_fiscal_country_id.code == "AR":
            if self.l10n_ar_afip_responsibility_type_ids and any(['country_group_id', 'country_id', 'zip_from', 'zip_to']):
                return {'warning': {
                    'title': _("Warning"),
                    'message': _('If use AFIP Responsibility then the country / zip codes will be not take into account'),
                }}
