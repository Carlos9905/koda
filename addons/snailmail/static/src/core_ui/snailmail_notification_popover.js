/* @koda-module */

import { Component } from "@koda/owl";

export class SnailmailNotificationPopover extends Component {
    static template = "snailmail.SnailmailNotificationPopover";
    static props = ["message", "close?"];
}
