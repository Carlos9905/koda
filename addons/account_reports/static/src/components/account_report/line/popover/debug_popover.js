/** @koda-module */

import { Component } from "@koda/owl";

export class AccountReportDebugPopover extends Component {
    static template = "account_reports.AccountReportDebugPopover";
    static props = {
        close: Function,
        expressionsDetail: Array,
        onClose: Function,
    };
}
