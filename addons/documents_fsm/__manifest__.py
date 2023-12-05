# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Documents - FSM',
    'version': '1.0',
    'category': 'Productivity/Documents',
    'summary': 'Avoid auto-enabling the documents feature on fsm projects',
    'description': """
Avoid auto-enabling the documents feature on fsm projects.
    """,
    'depends': ['documents_project', 'industry_fsm'],
    'auto_install': True,
    'license': 'OEEL-1',
    'post_init_hook': '_documents_fsm_post_init'
}
