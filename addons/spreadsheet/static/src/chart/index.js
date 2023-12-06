/** @koda-module */

import * as spreadsheet from "@koda/o-spreadsheet";

const { chartComponentRegistry } = spreadsheet.registries;
const { ChartJsComponent } = spreadsheet.components;

chartComponentRegistry.add("koda_bar", ChartJsComponent);
chartComponentRegistry.add("koda_line", ChartJsComponent);
chartComponentRegistry.add("koda_pie", ChartJsComponent);

import { OdooChartCorePlugin } from "./plugins/koda_chart_core_plugin";
import { ChartOdooMenuPlugin } from "./plugins/chart_koda_menu_plugin";
import { OdooChartUIPlugin } from "./plugins/koda_chart_ui_plugin";

export { OdooChartCorePlugin, ChartOdooMenuPlugin, OdooChartUIPlugin };
