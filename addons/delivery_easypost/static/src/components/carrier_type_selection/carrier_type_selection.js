/** @koda-module **/

import { registry } from "@web/core/registry";
import { SelectionField, selectionField } from "@web/views/fields/selection/selection_field";

export class CarrierTypeSelection extends SelectionField {
    get options() {
        const carrierTypes = this.props.record.context.carrier_types;
        if (carrierTypes) {
            return Object.entries(carrierTypes).map(([carrier, _]) => [carrier, carrier]);
        } else {
            return [];
        }
    }
}

export const carrierTypeSelection = {
    ...selectionField,
    component: CarrierTypeSelection,
};

registry.category("fields").add("carrier_type_selection", carrierTypeSelection);
