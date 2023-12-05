# -*- coding: utf-8 -*-
# Koda

from koda import models

class User(models.Model):
    _inherit = 'res.users'

    # -----------------------------------------
    # Business Methods
    # -----------------------------------------

    def _get_project_task_resource(self):
        return self.employee_id.resource_id
