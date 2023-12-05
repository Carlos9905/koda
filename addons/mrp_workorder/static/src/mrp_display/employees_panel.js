/** @koda-module **/

import { Component } from "@koda/owl";

export class MrpDisplayEmployeesPanel extends Component {
    static template = "mrp_workorder.MrpDisplayEmployeesPanel";
    static props = {
        employees: { type: Object },
        setSessionOwner: { type: Function },
        popupAddEmployee: { type: Function },
        logout: { type: Function },
    };
}
