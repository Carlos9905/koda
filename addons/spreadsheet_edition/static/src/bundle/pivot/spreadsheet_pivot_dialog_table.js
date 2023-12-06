/** @koda-module */
import { Component } from "@koda/owl";

export class PivotDialogTable extends Component {
    _onCellClicked(formula) {
        this.props.onCellSelected({ formula });
    }
}
PivotDialogTable.template = "spreadsheet_edition.PivotDialogTable";
PivotDialogTable.props = {
    colHeaders: Array,
    rowHeaders: Array,
    values: Array,
    onCellSelected: Function,
};
