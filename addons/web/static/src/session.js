/** @koda-module **/

export const session = koda.__session_info__ || {};
delete koda.__session_info__;
