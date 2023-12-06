/** @koda-module */

import * as spreadsheet from "@koda/o-spreadsheet";
import { CommonOdooChartConfigPanel } from "./common/config_panel";
import { OdooBarChartConfigPanel } from "./koda_bar/koda_bar_config_panel";
import { OdooLineChartConfigPanel } from "./koda_line/koda_line_config_panel";

const { chartSidePanelComponentRegistry } = spreadsheet.registries;
const { LineBarPieDesignPanel } = spreadsheet.components;

chartSidePanelComponentRegistry
    .add("koda_line", {
        configuration: OdooLineChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("koda_bar", {
        configuration: OdooBarChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("koda_pie", {
        configuration: CommonOdooChartConfigPanel,
        design: LineBarPieDesignPanel,
    });
