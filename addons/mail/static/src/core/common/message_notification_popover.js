/* @koda-module */

import { Component } from "@koda/owl";

export class MessageNotificationPopover extends Component {
    static template = "mail.MessageNotificationPopover";
    static props = ["message", "close?"];
}
