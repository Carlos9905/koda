/** @koda-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@koda/o-spreadsheet";
import { IrMenuSelector } from "@spreadsheet_edition/bundle/ir_menu_selector/ir_menu_selector";

const { LineBarPieConfigPanel, ScorecardChartConfigPanel, GaugeChartConfigPanel } =
    spreadsheet.components;

/**
 * Patch the chart configuration panel to add an input to
 * link the chart to an Odoo menu.
 */
function patchChartPanelWithMenu(PanelComponent) {
    patch(PanelComponent.prototype, {
        get kodaMenuId() {
            const menu = this.env.model.getters.getChartOdooMenu(this.props.figureId);
            return menu ? menu.id : undefined;
        },
        /**
         * @param {number | undefined} kodaMenuId
         */
        updateOdooLink(kodaMenuId) {
            if (!kodaMenuId) {
                this.env.model.dispatch("LINK_ODOO_MENU_TO_CHART", {
                    chartId: this.props.figureId,
                    kodaMenuId: undefined,
                });
                return;
            }
            const menu = this.env.model.getters.getIrMenu(kodaMenuId);
            this.env.model.dispatch("LINK_ODOO_MENU_TO_CHART", {
                chartId: this.props.figureId,
                kodaMenuId: menu.xmlid || menu.id,
            });
        },
    });
    PanelComponent.components = {
        ...PanelComponent.components,
        IrMenuSelector,
    };
}
patchChartPanelWithMenu(LineBarPieConfigPanel);
patchChartPanelWithMenu(GaugeChartConfigPanel);
patchChartPanelWithMenu(ScorecardChartConfigPanel);
