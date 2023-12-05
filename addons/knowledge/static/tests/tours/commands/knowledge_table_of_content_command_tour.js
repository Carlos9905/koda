/** @koda-module */

import { registry } from "@web/core/registry";
import { endKnowledgeTour, openCommandBar } from '../knowledge_tour_utils.js';
import { stepUtils } from "@web_tour/tour_service/tour_utils";


registry.category("web_tour.tours").add('knowledge_table_of_content_command_tour', {
    url: '/web',
    test: true,
    steps: () => [stepUtils.showAppsMenuItem(), {
    // open the Knowledge App
    trigger: '.o_app[data-menu-xmlid="knowledge.knowledge_menu_root"]',
}, { // open the command bar
    trigger: '.koda-editor-editable > p',
    run: function () {
        openCommandBar(this.$anchor[0]);
    },
}, { // click on the /toc command
    trigger: '.oe-powerbox-commandName:contains("Table Of Content")',
    run: 'click',
}, { // wait for the block to appear in the editor
    trigger: '.o_knowledge_behavior_type_toc',
}, { // insert a few titles in the editor
    trigger: '.koda-editor-editable > p',
    run: function () {
        const $anchor = $(this.$anchor[0]);
        $anchor.append([
            $('<h1>Title 1</h1>'),
            $('<h2>Title 1.1</h2>'),
            $('<h3>Title 1.1.1</h3>'),
            $('<h2>Title 1.2</h2>'),
        ]);
    },
}, { // click on the h1 anchor link generated by the toc
    trigger: '.o_knowledge_toc_link_depth_0',
    run: 'click',
}, { // open the tools panel
    trigger: '#dropdown_tools_panel',
    run: 'click',
}, { // switch to locked (readonly) mode
    trigger: '.o_knowledge_more_options_panel .btn-lock',
    run: 'click',
}, { // check that we are in readonly mode
    trigger: '.o_field_html .o_readonly',
    run: () => {},
}, { // check that the content of the toc is not duplicated
    trigger: '.o_knowledge_behavior_type_toc',
    run: function () {
        if (this.$anchor[0].querySelectorAll('.o_knowledge_toc_content').length !== 1) {
            throw new Error('The table of content group of links should be present exactly once (not duplicated)');
        }
    },
}, { // click on the h1 anchor link generated by the toc
    trigger: '.o_knowledge_toc_link_depth_0',
    run: 'click',
}, { // open the tools panel
    trigger: '#dropdown_tools_panel',
    run: 'click',
}, { // unlock the article
    trigger: '.o_knowledge_more_options_panel.show .btn-lock',
    run: 'click',
}, { // check that we are in edit mode
    trigger: '.o_field_html .koda-editor-editable',
    run: () => {},
}, ...endKnowledgeTour()
]});
