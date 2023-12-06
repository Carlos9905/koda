/** @koda-module **/

import { PivotController } from "@web/views/pivot/pivot_controller";
import { useService } from "@web/core/utils/hooks";
import { onWillStart } from "@odoo/owl";

export class TimesheetValidationPivotController extends PivotController {
    setup() {
        super.setup();
        this.notificationService = useService("notification");
        onWillStart(async () => {
	        await this._checkValidateButtonColor();
        });
    }

    async _checkValidateButtonColor() {
        const timesheetCount = await this.model.orm.call(
            this.model.metaData.resModel,
            'search_count',
            [[['validated', '=', false]], ],
            { limit: 1 },
        );
        this.displayValidateButtonPrimary = timesheetCount === 1;
    }

    //----------------------------------------------------------------------
    // Handlers
    //----------------------------------------------------------------------

    /**
     * @param {MouseEvent} ev
     */
    async onValidateButtonClicked(ev) {
        const timesheetIDs = await this.model.orm.search(this.props.resModel, this.model.searchParams.domain);
        const result = await this.model.orm.call(this.props.resModel, 'action_validate_timesheet', [timesheetIDs]);
        this.displayValidateButtonPrimary = false;
        await this.notificationService.add(result.params.title, { type: result.params.type });
        //reload the table content
        await this.model.load(this.model.searchParams);
        this.model.notify();
    }
};
