/** @koda-module **/

import { Component } from "@koda/owl";

export class FileUploadProgressContainer extends Component {}
FileUploadProgressContainer.template = "web.FileUploadProgressContainer";
FileUploadProgressContainer.props = {
    Component: { optional: false },
    shouldDisplay: { type: Function, optional: true },
    fileUploads: { type: Object },
};
