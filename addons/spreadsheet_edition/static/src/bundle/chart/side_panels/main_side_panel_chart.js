/** @koda-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@koda/o-spreadsheet";

const { chartRegistry } = spreadsheet.registries;
const { ChartPanel } = spreadsheet.components;

/**
 * This patch is necessary to ensure that the chart type cannot be changed
 * between koda charts and spreadsheet charts.
 */

patch(ChartPanel.prototype, {
    get chartTypes() {
        const definition = this.getChartDefinition();
        const isOdoo = definition.type.startsWith("koda_");
        return this.getChartTypes(isOdoo);
    },

    /**
     * @param {boolean} isOdoo
     */
    getChartTypes(isOdoo) {
        const result = {};
        for (const key of chartRegistry.getKeys()) {
            if ((isOdoo && key.startsWith("koda_")) || (!isOdoo && !key.startsWith("koda_"))) {
                result[key] = chartRegistry.get(key).name;
            }
        }
        return result;
    },

    onTypeChange(type) {
        if (this.getChartDefinition().type.startsWith("koda_")) {
            const definition = {
                stacked: false,
                verticalAxisPosition: "left",
                ...this.env.model.getters.getChartDefinition(this.figureId),
                type,
            };
            this.env.model.dispatch("UPDATE_CHART", {
                definition,
                id: this.figureId,
                sheetId: this.env.model.getters.getActiveSheetId(),
            });
        } else {
            super.onTypeChange(type);
        }
    },
});
