/** @koda-module **/

import { _t } from "@web/core/l10n/translation";
import { Component, onWillUnmount, useEffect, useRef } from "@odoo/owl";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { FormViewDialog } from "@web/views/view_dialogs/form_view_dialog";
import { Layout } from "@web/search/layout";
import { standardViewProps } from "@web/views/standard_view_props";
import { useModelWithSampleData } from "@web/model/model";
import { usePager } from "@web/search/pager_hook";
import { useService } from "@web/core/utils/hooks";
import { SearchBar } from "@web/search/search_bar/search_bar";
import { useSearchBarToggler } from "@web/search/search_bar/search_bar_toggler";
import { CogMenu } from "@web/search/cog_menu/cog_menu";

import { useSetupView } from "@web/views/view_hook";

export class GanttController extends Component {
    static components = {
        CogMenu,
        Dropdown,
        DropdownItem,
        Layout,
        SearchBar,
    };
    static props = {
        ...standardViewProps,
        Model: Function,
        Renderer: Function,
        buttonTemplate: String,
        modelParams: Object,
        scrollPosition: { type: Object, optional: true },
    };
    static template = "web_gantt.GanttController";

    setup() {
        this.actionService = useService("action");
        this.dialogService = useService("dialog");
        this.orm = useService("orm");

        this.model = useModelWithSampleData(this.props.Model, this.props.modelParams);
        useSetupView({
            rootRef: useRef("root"),
            getLocalState: () => {
                return { metaData: this.model.metaData };
            },
        });

        onWillUnmount(() => this.closeDialog?.());

        usePager(() => {
            const { groupedBy, pagerLimit, pagerOffset } = this.model.metaData;
            const { count } = this.model.data;
            if (pagerLimit !== null && groupedBy.length) {
                return {
                    offset: pagerOffset,
                    limit: pagerLimit,
                    total: count,
                    onUpdate: async ({ offset, limit }) => {
                        await this.model.updatePagerParams({ offset, limit });
                    },
                };
            }
        });

        const rootRef = useRef("root");
        useEffect(
            (showNoContentHelp) => {
                if (showNoContentHelp) {
                    const realRows = [
                        ...rootRef.el.querySelectorAll(
                            ".o_gantt_row_header:not(.o_sample_data_disabled)"
                        ),
                    ];
                    // interactive rows created in extensions (fromServer undefined)
                    const headerContainerWidth =
                        rootRef.el.querySelector(".o_gantt_header").clientHeight;

                    const offset = realRows.reduce(
                        (current, el) => current + el.clientHeight,
                        headerContainerWidth
                    );

                    const noContentHelperEl = rootRef.el.querySelector(".o_view_nocontent");
                    noContentHelperEl.style.top = `${offset}px`;
                }
            },
            () => [this.showNoContentHelp]
        );
        this.searchBarToggler = useSearchBarToggler();
    }

    get className() {
        if (this.env.isSmall) {
            const classList = (this.props.className || "").split(" ");
            classList.push("o_action_delegate_scroll");
            return classList.join(" ");
        }
        return this.props.className;
    }

    get showNoContentHelp() {
        return this.model.useSampleModel;
    }

    /**
     * @param {Record<string, any>} [context]
     */
    create(context) {
        const { createAction } = this.model.metaData;
        if (createAction) {
            this.actionService.doAction(createAction, {
                additionalContext: context,
                onClose: () => {
                    this.model.fetchData();
                },
            });
        } else {
            this.openDialog({ context });
        }
    }

    /**
     * Opens dialog to add/edit/view a record
     *
     * @param {Record<string, any>} props FormViewDialog props
     * @param {Record<string, any>} [options={}]
     */
    openDialog(props, options = {}) {
        const { canDelete, canEdit, resModel, formViewId: viewId } = this.model.metaData;

        const title = props.title || (props.resId ? _t("Open") : _t("Create"));

        let removeRecord;
        if (canDelete && props.resId) {
            removeRecord = () => {
                return new Promise((resolve) => {
                    this.dialogService.add(ConfirmationDialog, {
                        body: _t("Are you sure to delete this record?"),
                        confirm: async () => {
                            await this.orm.unlink(resModel, [props.resId]);
                            resolve();
                        },
                        cancel: () => {},
                    });
                });
            };
        }

        this.closeDialog = this.dialogService.add(
            FormViewDialog,
            {
                title,
                resModel,
                viewId,
                resId: props.resId,
                mode: canEdit ? "edit" : "readonly",
                context: props.context,
                removeRecord,
            },
            {
                ...options,
                onClose: () => {
                    this.closeDialog = null;
                    this.model.fetchData();
                },
            }
        );
    }

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    onAddClicked() {
        const { focusDate, scale } = this.model.metaData;
        const start = focusDate.startOf(scale.id);
        const stop = focusDate.endOf(scale.id);
        const context = this.model.getDialogContext({ start, stop, withDefault: true });
        this.create(context);
    }
}
