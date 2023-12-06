/** @koda-module */

import { coreTypes, CorePlugin } from "@koda/o-spreadsheet";

/** Plugin that link charts with Odoo menus. It can contain either the Id of the koda menu, or its xml id. */
export class ChartOdooMenuPlugin extends CorePlugin {
    constructor(config) {
        super(config);
        this.kodaMenuReference = {};
    }

    /**
     * Handle a spreadsheet command
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "LINK_ODOO_MENU_TO_CHART":
                this.history.update("kodaMenuReference", cmd.chartId, cmd.kodaMenuId);
                break;
            case "DELETE_FIGURE":
                this.history.update("kodaMenuReference", cmd.id, undefined);
                break;
        }
    }

    /**
     * Get koda menu linked to the chart
     *
     * @param {string} chartId
     * @returns {object | undefined}
     */
    getChartOdooMenu(chartId) {
        const menuId = this.kodaMenuReference[chartId];
        return menuId ? this.getters.getIrMenu(menuId) : undefined;
    }

    import(data) {
        if (data.chartOdooMenusReferences) {
            this.kodaMenuReference = data.chartOdooMenusReferences;
        }
    }

    export(data) {
        data.chartOdooMenusReferences = this.kodaMenuReference;
    }
}
ChartOdooMenuPlugin.getters = ["getChartOdooMenu"];

coreTypes.add("LINK_ODOO_MENU_TO_CHART");
