# -*- coding: utf-8 -*-
# Koda

from collections import defaultdict

from koda import models


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    def _configure_payroll_account_hk(self, companies):
        account_codes = [
        ]
        default_account = False
        rules_mapping = defaultdict(dict)

        # ================================================ #
        #          HK Employee Payroll Structure          #
        # ================================================ #

        self._configure_payroll_account(
            companies,
            "HK",
            account_codes=account_codes,
            rules_mapping=rules_mapping,
            default_account=default_account)
