# -*- coding: utf-8 -*-
# Koda

{
    'name': 'Skills Management',
    'category': 'Human Resources/Employees',
    'sequence': 270,
    'version': '1.0',
    'summary': 'Manage skills, knowledge and resume of your employees',
    'description':
        """
Skills and Resume for HR
========================

This module introduces skills and resume management for employees.
        """,
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_skills_security.xml',
        'views/hr_views.xml',
        'views/hr_employee_skill_log_views.xml',
        'data/hr_resume_data.xml',
        'data/hr_skill_data.xml',
        'data/ir_actions_server_data.xml',
        'data/report_paperformat.xml',
        'report/hr_employee_skill_report_views.xml',
        'report/hr_employee_cv_report.xml',
        'views/hr_department_views.xml',
        'views/hr_employee_cv_templates.xml',
        'wizard/hr_employee_cv_wizard_views.xml',
    ],
    'demo': [
        'data/hr_resume_demo.xml',
        'data/hr.employee.skill.csv',
        'data/hr.resume.line.csv',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'hr_skills/static/src/fields/skills_one2many/*',
            'hr_skills/static/src/fields/**/*',
            'hr_skills/static/src/scss/*.scss',
            'hr_skills/static/src/views/*.js',
            'hr_skills/static/src/xml/**/*',
        ],
        'web.assets_tests': [
            'hr_skills/static/tests/tours/*',
        ],
        'web.report_assets_pdf': [
            '/hr_skills/static/src/scss/report_employee_cv.scss',
        ],
    },
    'license': 'LGPL-3',
}
