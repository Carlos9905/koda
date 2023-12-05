# -*- coding: utf-8 -*-
# Koda
import contextlib
import io

from koda.tools import pycompat, street_split

from koda import api, models, _


class GeneralLedgerCustomHandler(models.AbstractModel):
    _inherit = 'account.general.ledger.report.handler'

    def _custom_options_initializer(self, report, options, previous_options=None):
        super()._custom_options_initializer(report, options, previous_options)
        if self.env.company.account_fiscal_country_id.code == 'DK':
            options.setdefault('buttons', []).append({
                'name': _('SAF-T'),
                'sequence': 50,
                'action': 'export_file',
                'action_param': 'l10n_dk_export_saft_to_xml',
                'file_export_type': _('XML')
            })
            options['buttons'].append({
                'name': _('CSV'),
                'sequence': 55,
                'action': 'export_file',
                'action_param': 'l10n_dk_export_general_ledger_csv',
                'file_export_type': _('CSV')
            })

    @api.model
    def l10n_dk_export_saft_to_xml(self, options):
        report = self.env['account.report'].browse(options['report_id'])
        template_vals = self._l10n_dk_saft_prepare_report_values(report, options)
        file_data = self._saft_generate_file_data_with_error_check(
            report, options, template_vals, 'l10n_dk_reports.saft_template'
        )
        self.env['ir.attachment'].l10n_dk_saft_validate_xml_from_attachment(file_data['file_content'])
        return file_data

    @api.model
    def _l10n_dk_saft_prepare_report_values(self, report, options):
        template_vals = self._saft_prepare_report_values(report, options)
        template_vals.update({
            'xmlns': "urn:StandardAuditFile-Taxation-Financial:DK",
            'file_version': '1.0',
            'street_split': street_split,
        })
        for tax in template_vals['tax_vals_list']:
            # The documentation describes the `EffectiveDate` as "Representing the starting date for this entry."
            # The postgres `create_date` is the date from which the record can be used in the system and thus is the
            # more suitable one in this context.
            tax['effective_date'] = tax['create_date'].strftime('%Y-%m-%d')
        return template_vals

    def _saft_get_account_type(self, account_type):
        # OVERRIDE account_saft/models/account_general_ledger
        if self.env.company.account_fiscal_country_id.code != 'DK':
            return super()._saft_get_account_type(account_type)

        # possible type: Asset/Liability/Sale/Expense/Other
        account_type_dict = {
            "asset_receivable": 'Asset',
            "asset_cash": 'Asset',
            "asset_current": 'Asset',
            "asset_non_current": 'Asset',
            "asset_prepayments": 'Asset',
            "asset_fixed": 'Asset',
            "liability_payable": 'Liability',
            "liability_credit_card": 'Liability',
            "liability_current": 'Liability',
            "liability_non_current": 'Liability',
            "equity": 'Liability',
            "equity_unaffected": 'Liability',
            "income": 'Sale',
            "income_other": 'Sale',
            "expense": 'Expense',
            "expense_depreciation": 'Expense',
            "expense_direct_cost": 'Expense',
            "off_balance": 'Other',
        }
        return account_type_dict[account_type]

    @api.model
    def l10n_dk_export_general_ledger_csv(self, options):
        report = self.env['account.report'].browse(options['report_id'])
        # account number, account name, balance
        csv_lines = [("KONTONUMMER", "KONTONAVN", "VAERDI")]
        # fold all report lines to make sure we only get the account details
        new_options = report.get_options(previous_options={**options, 'unfolded_lines': [], 'unfold_all': False})

        balance_index = [c['expression_label'] for c in options['columns']].index('balance')
        for line in filter(lambda line: self.env['account.report']._get_markup(line['id']) != 'total', report._get_lines(new_options)):
            account_number, account_name = line['name'].split(maxsplit=1)
            account_balance = int(line['columns'][balance_index]['no_format'])  # balance value must be a whole number
            csv_lines.append((account_number, account_name, account_balance))

        with contextlib.closing(io.BytesIO()) as buf:
            writer = pycompat.csv_writer(buf, delimiter=',')
            writer.writerows(csv_lines)
            content = buf.getvalue()

        return {
            'file_name': report.get_default_report_filename(options, 'csv'),
            'file_content': content,
            'file_type': 'csv',
        }
