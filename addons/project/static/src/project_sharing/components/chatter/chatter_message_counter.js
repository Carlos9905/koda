/** @koda-module */

import { Component } from "@koda/owl";

export class ChatterMessageCounter extends Component { }

ChatterMessageCounter.props = {
    count: Number,
};
ChatterMessageCounter.template = 'project.ChatterMessageCounter';
