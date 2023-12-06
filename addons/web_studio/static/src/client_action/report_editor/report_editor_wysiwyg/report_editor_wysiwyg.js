/** @koda-module */
import {
    Component,
    onWillStart,
    onMounted,
    onWillDestroy,
    onWillUnmount,
    reactive,
    useState,
} from "@koda/owl";
import { loadBundle } from "@web/core/assets";
import { _t } from "@web/core/l10n/translation";
import { omit } from "@web/core/utils/objects";
import { usePopover } from "@web/core/popover/popover_hook";
import { useHotkey } from "@web/core/hotkeys/hotkey_hook";
import { sortBy } from "@web/core/utils/arrays";
import { useOwnedDialogs, useService } from "@web/core/utils/hooks";
import { SelectMenu } from '@web/core/select_menu/select_menu';
import { QWebPlugin } from "@web_editor/js/backend/QWebPlugin";
import { setSelection, startPos, endPos } from "@web_editor/js/editor/koda-editor/src/utils/utils";

import { StudioDynamicPlaceholderPopover } from "./studio_dynamic_placeholder_popover";
import { Many2ManyTagsField } from "@web/views/fields/many2many_tags/many2many_tags_field";
import { CharField } from "@web/views/fields/char/char_field";
import { Record as _Record } from "@web/model/record";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { BooleanField } from "@web/views/fields/boolean/boolean_field";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

import { ReportEditorSnackbar } from "@web_studio/client_action/report_editor/report_editor_snackbar";
import { useEditorMenuItem } from "@web_studio/client_action/editor/edition_flow";
import { memoizeOnce } from "@web_studio/client_action/utils";
import { ReportEditorIframe } from "../report_editor_iframe";

class __Record extends _Record.components._Record {
    setup() {
        super.setup();
        const willSaveUrgently = () => this.model.bus.trigger("WILL_SAVE_URGENTLY");
        onMounted(() => {
            this.env.reportEditorModel.bus.addEventListener("WILL_SAVE_URGENTLY", willSaveUrgently);
        });

        onWillDestroy(() =>
            this.env.reportEditorModel.bus.removeEventListener(
                "WILL_SAVE_URGENTLY",
                willSaveUrgently
            )
        );
    }
}

class Record extends _Record {
    static components = { ..._Record.components, _Record: __Record };
}

function getOrderedTAs(node) {
    const results = [];
    while (node) {
        const closest = node.closest("[t-foreach]");
        if (closest) {
            results.push(closest.getAttribute("t-as"));
            node = closest.parentElement;
        } else {
            node = null;
        }
    }
    return results;
}

class FieldDynamicPlaceholder extends Component {
    static components = { StudioDynamicPlaceholderPopover, SelectMenu };
    static template = "web_studio.FieldDynamicPlaceholder";
    static props = {
        resModel: String,
        availableQwebVariables: Object,
        close: Function,
        validate: Function,
        isEditingFooterHeader: Boolean,
        initialQwebVar: { optional: true, type: String },
        showOnlyX2ManyFields: Boolean,
    };

    static defaultProps = {
        initialQwebVar: "",
    };

    setup() {
        this.state = useState({ currentVar: this.getDefaultVariable() });
        useHotkey("escape", () => this.props.close());
    }

    get currentResModel() {
        const currentVar = this.state.currentVar;
        const resModel = currentVar && this.props.availableQwebVariables[currentVar].model;
        return resModel || this.props.resModel;
    }

    get sortedVariables() {
        const entries = Object.entries(this.props.availableQwebVariables).filter(
            ([k, v]) => v.in_foreach && !this.props.isEditingFooterHeader
        );
        const resModel = this.props.resModel;
        const sortFn = ([k, v]) => {
            let score = 0;
            if (k === "doc") {
                score += 2;
            }
            if (k === "docs") {
                score -= 2;
            }
            if (k === "o") {
                score++;
            }
            if (v.model === resModel) {
                score++;
            }
            return score;
        };

        const mapFn = ([k, v]) => {
            return {
                value: k,
                label: `${k} (${v.name})`,
                model: v.model,
            }
        }
        return sortBy(entries, sortFn, "desc").map(e => mapFn(e));
    }

    validate(...args) {
        this.props.validate(this.state.currentVar, ...args);
    }

    getDefaultVariable() {
        const initialQwebVar = this.props.initialQwebVar;
        if (initialQwebVar && initialQwebVar in this.props.availableQwebVariables) {
            return initialQwebVar;
        }
        if (this.props.isEditingFooterHeader) {
            const companyVar = Object.entries(this.props.availableQwebVariables).find(
                ([k, v]) => v.model === "res.company"
            );
            return companyVar && companyVar[0];
        }

        let defaultVar = this.sortedVariables.find((v) => {
            return ["doc", "o"].includes(v.value);
        });
        defaultVar = defaultVar || this.sortedVariables.find((v) => v.model === this.props.resModel);
        return defaultVar && defaultVar.value;
    }
}

class UndoRedo extends Component {
    static template = "web_studio.ReportEditorWysiwyg.UndoRedo";
    static props = {
        state: Object,
    };
}

class ResetConfirmatiopnPopup extends ConfirmationDialog {
    static template = "web_studio.ReportEditorWysiwyg.ResetConfirmatiopnPopup";
    static props = {
        ...omit(ConfirmationDialog.props, "body"),
        state: Object,
    };
}

function getMaxColumns(row) {
    let cols = [];
    const children = Array.from(row.children);

    if (children.every((el) => el.tagName === "T")) {
        for (const child of children) {
            const subCols = getMaxColumns(child);
            if (subCols.length > cols.length) {
                cols = subCols;
            }
        }
    } else {
        cols = children.filter((el) => el.tagName !== "T");
    }

    return cols;
}

function computeTableLayout(table) {
    const allRows = table.querySelectorAll("[oe-origin-tag='tr']");
    let refCols = [];
    for (const row of allRows) {
        const cols = getMaxColumns(row);
        if (cols.length > refCols.length) {
            refCols = cols;
        }
    }

    let numCols = 0;
    for (const col of refCols) {
        const colSpan = parseInt(col.getAttribute("colspan") || "1");
        numCols += colSpan;
    }
    const baseColSize = Math.floor(100 / numCols);
    const gap = 10;
    for (const row of allRows) {
        const cols = row.querySelectorAll("[oe-origin-tag='td'],[oe-origin-tag='th']");
        for (const col of cols) {
            let colSpan = parseInt(col.getAttribute("colspan") || "1");
            if (colSpan > numCols) {
                colSpan = numCols;
            }
            col.setAttribute("style", `width: calc(${baseColSize * colSpan}% - ${gap}px);`);
        }
    }
}

export class ReportEditorWysiwyg extends Component {
    static components = {
        CharField,
        Record,
        Many2ManyTagsField,
        Many2OneField,
        BooleanField,
        UndoRedo,
        ReportEditorIframe,
    };
    static props = {
        paperFormatStyle: String,
    };
    static template = "web_studio.ReportEditorWysiwyg";

    setup() {
        this.rpc = useService("rpc");
        this.action = useService("action");
        this.user = useService("user");
        this.addDialog = useOwnedDialogs();
        this.notification = useService("notification");

        this._getReportQweb = memoizeOnce(() => {
            const tree = new DOMParser().parseFromString(
                this.reportEditorModel.reportQweb,
                "text/html"
            );
            for (const table of tree.querySelectorAll("[oe-origin-tag='table']")) {
                computeTableLayout(table);
            }
            return tree.firstElementChild;
        });

        const reportEditorModel = (this.reportEditorModel = useState(this.env.reportEditorModel));

        this.state = useState({ wysiwygKey: 0 });
        this.fieldPopover = usePopover(FieldDynamicPlaceholder);
        useEditorMenuItem({
            component: ReportEditorSnackbar,
            props: {
                state: reportEditorModel,
                onSave: this.save.bind(this),
                onDiscard: this.discard.bind(this),
            },
        });

        onWillStart(async () => {
            await Promise.all([
                loadBundle("web_editor.backend_assets_wysiwyg"),
                this.reportEditorModel.loadReportQweb(),
            ]);
            this.Wysiwyg = (
                await koda.loader.modules.get("@web_editor/js/wysiwyg/wysiwyg")
            ).Wysiwyg;
        });

        onWillUnmount(() => {
            this.reportEditorModel.bus.trigger("WILL_SAVE_URGENTLY");
            this.save({ urgent: true });
        });

        this.setWysiwygInstance = async (wysiwyg) => {
            await wysiwyg.startEdition();
            if (this.observer) {
                this.observer.disconnect();
                this.observer = null;
            }
            this.wysiwyg = wysiwyg;
            const kodaEditor = this.wysiwyg.kodaEditor;

            const undoRedoState = this.undoRedoState;
            undoRedoState.canUndo = false;
            undoRedoState.canRedo = false;

            kodaEditor.addEventListener("historyStep", () => {
                undoRedoState.canUndo = kodaEditor.historyCanUndo();
                undoRedoState.canRedo = kodaEditor.historyCanRedo();
                this.reportEditorModel.isDirty = this.undoRedoState.canUndo;
            });

            const observe = () => {
                this.observer.observe(wysiwyg.$editable[0], {
                    childList: true,
                    subtree: true,
                    attributes: true,
                    attributeOldValue: true,
                    characterData: true,
                });
            };

            this.observer = new MutationObserver((records) =>
                this.domChangesDirtyMutations(kodaEditor, records)
            );
            kodaEditor.addEventListener("observerUnactive", () => {
                if (this.observer) {
                    this.domChangesDirtyMutations(kodaEditor, this.observer.takeRecords());
                    this.observer.disconnect();
                }
            });

            kodaEditor.addEventListener("observerActive", observe);

            kodaEditor.observerUnactive();
            if (koda.debug) {
                ["t-esc", "t-out", "t-field"].forEach((tAtt) => {
                    kodaEditor.document.querySelectorAll(`*[${tAtt}]`).forEach((e) => {
                        // Save the previous title to set it back before saving the report
                        if (e.hasAttribute("title")) {
                            e.setAttribute("data-oe-title", e.getAttribute("title"));
                        }
                        e.setAttribute("title", e.getAttribute(tAtt));
                    });
                });
            }
            kodaEditor.observerActive();
        };

        this.undoRedoState = reactive({
            canUndo: false,
            canRedo: false,
            undo: () => this.wysiwyg?.kodaEditor.historyUndo(),
            redo: () => this.wysiwyg?.kodaEditor.historyRedo(),
        });
    }

    onIframeLoaded({ iframeRef }) {
        this.iframeRef = iframeRef;
        const doc = iframeRef.el.contentDocument;
        const _jquery = window.$;
        doc.defaultView.$ = (...args) => {
            if (args.length <= 2 && typeof args[0] === "string") {
                return _jquery(args[0], args[1] || doc);
            } else {
                return _jquery(...args);
            }
        };
        doc.body.classList.remove("container");
        this.state.wysiwygKey++;
        this.reportEditorModel.setInEdition(false);
    }

    get reportQweb() {
        const model = this.reportEditorModel;
        return this._getReportQweb(`${model.renderKey}_${model.reportQweb}`).outerHTML;
    }

    get wysiwygProps() {
        const iframe = this.iframeRef.el;
        const options = {
            get editable() {
                return $(iframe.contentDocument.querySelector("#wrapwrap"));
            },
            get document() {
                return iframe.contentDocument;
            },
            powerboxCategories: [{ name: _t("Report Tools"), priority: 100 }], // on Top
            powerboxCommands: this.getPowerboxCommands(),
            allowCommandVideo: false,
            editorPlugins: [QWebPlugin],
            savableSelector: "[data-oe-model='ir.ui.view']",
            autostart: true,
            sideAttach: true,
            getContextFromParentRect: () => {
                return this.iframeRef.el.getBoundingClientRect();
            },
        };

        return { options, startWysiwyg: this.setWysiwygInstance };
    }

    get reportRecordProps() {
        const model = this.reportEditorModel;
        return {
            fields: model.reportFields,
            activeFields: model.reportActiveFields,
            values: model.reportData,
        };
    }

    async save({ urgent = false } = {}) {
        if (!this.wysiwyg) {
            return;
        }
        const htmlParts = {};
        const editableClone = this.wysiwyg.$editable.clone()[0];

        this.wysiwyg._saveElement = async ($el) => {
            const viewId = $el.data("oe-id");
            if (!viewId) {
                return;
            }

            // FIXME: don't escape, otherwise the non-breakable spaces will be escaped too
            //const escaped_html = this.wysiwyg._getEscapedElement($el).prop("outerHTML");
            const escaped_html = $el[0].outerHTML;

            htmlParts[viewId] = htmlParts[viewId] || {};

            const xpath = $el.data("oe-xpath");
            htmlParts[viewId][xpath || "entire_view"] = escaped_html;
        };

        // Clean technical title
        if (koda.debug) {
            editableClone.querySelectorAll("*[t-field],*[t-out],*[t-esc]").forEach((e) => {
                if (e.hasAttribute("data-oe-title")) {
                    e.setAttribute("title", e.getAttribute("data-oe-title"));
                    e.removeAttribute("data-oe-title");
                } else {
                    e.removeAttribute("title");
                }
            });
        }

        await this.wysiwyg.saveContent(false, editableClone);
        await this.reportEditorModel.saveReport({ htmlParts, urgent });
    }

    async discard() {
        this.wysiwyg.kodaEditor.document.getSelection().removeAllRanges();
        await this.wysiwyg.cancel(false);
        await this.reportEditorModel.discardReport();
    }

    domChangesDirtyMutations(kodaEditor, records) {
        records = kodaEditor.filterMutationRecords(records);

        for (const record of records) {
            if (record.type === "attributes") {
                if (record.attributeName === "contenteditable") {
                    continue;
                }
                if (record.attributeName.startsWith("data-oe-t")) {
                    continue;
                }
            }
            let target = record.target;
            if (!target.isConnected) {
                continue;
            }
            if (target.nodeType !== Node.ELEMENT_NODE) {
                target = target.parentElement;
            }
            if (!target) {
                continue;
            }

            target = target.closest(`[data-oe-model='ir.ui.view']`);
            if (!target) {
                continue;
            }

            const viewId = target.getAttribute("data-oe-id");
            if (
                target.parentElement.closest(
                    `.o_dirty[data-oe-model='ir.ui.view'][data-oe-id='${viewId}']`
                )
            ) {
                continue;
            }
            target.classList.add("o_dirty");
            target
                .querySelectorAll(`[data-oe-model='ir.ui.view'][data-oe-id='${viewId}'].o_dirty`)
                .forEach((n) => n.classList.remove("o_dirty"));
        }
    }

    getPowerboxCommands() {
        return [
            {
                category: _t("Report Tools"),
                name: _t("Field"),
                priority: 150,
                description: _t("Insert a field"),
                fontawesome: "fa-magic",
                callback: () => this.insertField(),
            },
            {
                category: _t("Report Tools"),
                name: _t("Dynamic Table"),
                priority: 140,
                description: _t("Insert a table based on a relational field."),
                fontawesome: "fa-magic",
                callback: () => this.insertTableX2Many(),
            },
        ];
    }

    getFieldPopoverParams() {
        const kodaEditor = this.wysiwyg.kodaEditor;
        const doc = kodaEditor.document;

        const resModel = this.reportEditorModel.reportResModel;
        const docSelection = doc.getSelection();
        const { anchorNode } = docSelection;
        const isEditingFooterHeader =
            !!(doc.querySelector(".header") && doc.querySelector(".header").contains(anchorNode)) ||
            !!(doc.querySelector(".footer") && doc.querySelector(".footer").contains(anchorNode));

        const popoverAnchor = anchorNode.nodeType === 1 ? anchorNode : anchorNode.parentElement;

        const nodeOeContext = popoverAnchor.closest("[oe-context]");
        const availableQwebVariables =
            nodeOeContext && JSON.parse(nodeOeContext.getAttribute("oe-context"));

        return {
            popoverAnchor,
            props: {
                availableQwebVariables,
                initialQwebVar: getOrderedTAs(popoverAnchor)[0] || "",
                isEditingFooterHeader,
                resModel,
            },
        };
    }

    async insertTableX2Many() {
        const { popoverAnchor, props } = this.getFieldPopoverParams();
        await this.fieldPopover.open(popoverAnchor, {
            ...props,
            showOnlyX2ManyFields: true,
            validate: (
                qwebVar,
                fieldNameChain,
                defaultValue = "",
                is_image,
                relation,
                relationName
            ) => {
                this.wysiwyg.focus();
                const doc = this.wysiwyg.kodaEditor.document;

                const table = doc.createElement("table");
                table.classList.add("table", "table-sm");

                const tBody = table.createTBody();

                const topRow = tBody.insertRow();
                topRow.classList.add(
                    "border-bottom",
                    "border-top-0",
                    "border-start-0",
                    "border-end-0",
                    "border-2",
                    "border-dark",
                    "fw-bold"
                );
                const topTd = doc.createElement("td");
                topTd.appendChild(doc.createTextNode(defaultValue || "Column name"));
                topRow.appendChild(topTd);

                const tr = doc.createElement("tr");
                tr.setAttribute("t-foreach", `${qwebVar}.${fieldNameChain}`);
                tr.setAttribute("t-as", "x2many_record");
                tr.setAttribute(
                    "oe-context",
                    JSON.stringify({
                        x2many_record: {
                            model: relation,
                            in_foreach: true,
                            name: relationName,
                        },
                        ...props.availableQwebVariables
                    })
                );
                tBody.appendChild(tr);

                const td = doc.createElement("td");
                td.textContent = _t("Insert a field...");
                tr.appendChild(td);

                this.wysiwyg.kodaEditor.execCommand("insert", table);
                this.iframeRef.el.focus();
                setSelection(...startPos(td), ...endPos(td), true);
            },
        });
    }

    async insertField() {
        const { popoverAnchor, props } = this.getFieldPopoverParams();
        await this.fieldPopover.open(popoverAnchor, {
            ...props,
            showOnlyX2ManyFields: false,
            validate: (qwebVar, fieldNameChain, defaultValue = "", is_image) => {
                this.wysiwyg.focus();
                const doc = this.wysiwyg.kodaEditor.document;
                const span = doc.createElement("span");
                span.textContent = defaultValue;
                span.setAttribute("t-field", `${qwebVar}.${fieldNameChain}`);

                if (koda.debug) {
                    span.setAttribute("title", `${qwebVar}.${fieldNameChain}`);
                }

                if (is_image) {
                    span.setAttribute("t-options-widget", "'image'");
                    span.setAttribute("t-options-qweb_img_raw_data", 1);
                }
                this.wysiwyg.kodaEditor.execCommand("insert", span);
            },
        });
    }

    async printPreview() {
        const model = this.reportEditorModel;
        await this.save();
        const recordId = model.reportEnv.currentId || model.reportEnv.ids.find((i) => !!i) || false;
        if (!recordId) {
            this.notification.add(
                _t(
                    "There is no record on which this report can be previewed. Create at least one record to preview the report."
                ),
                {
                    type: "danger",
                    title: _t("Report preview not available"),
                }
            );
            return;
        }

        const action = await this.rpc("/web_studio/print_report", {
            record_id: recordId,
            report_id: model.editedReportId,
        });
        this.reportEditorModel.renderKey++;
        return this.action.doAction(action, { clearBreadcrumbs: true });
    }

    async resetReport() {
        this.wysiwyg.kodaEditor.document.getSelection().removeAllRanges();
        const state = reactive({ includeHeaderFooter: true });
        this.addDialog(ResetConfirmatiopnPopup, {
            title: _t("Reset report"),
            confirmLabel: _t("Reset report"),
            confirmClass: "btn-danger",
            cancelLabel: _t("Go back"),
            state,
            cancel: () => {},
            confirm: async () => {
                await this.reportEditorModel.saveReport();
                this.reportEditorModel.renderKey++;
                return this.reportEditorModel.resetReport(state.includeHeaderFooter);
            },
        });
    }

    async openReportFormView() {
        await this.save();
        return this.action.doAction(
            {
                type: "ir.actions.act_window",
                res_model: "ir.actions.report",
                res_id: this.reportEditorModel.editedReportId,
                views: [[false, "form"]],
                target: "current",
            },
            { clearBreadcrumbs: true }
        );
    }

    async editSources() {
        await this.save();
        this.reportEditorModel.mode = "xml";
    }
}
