# -*- coding: utf-8 -*-
# Koda

from koda import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
