# -*- coding: utf-8 -*-
# Koda

from . import models
from . import controllers
from . import report

def _set_allow_billable_in_project(env):
    Project = env['project.project']
    Task = env['project.task']
    projects = Project.search(Project._get_projects_to_make_billable_domain())
    non_billable_projects, = Task._read_group(
        Task._get_projects_to_make_billable_domain([('project_id', 'not in', projects.ids)]),
        [],
        ['project_id:recordset'],
    )[0]
    projects += non_billable_projects
    projects.allow_billable = True
