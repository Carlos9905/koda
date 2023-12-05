# -*- coding: utf-8 -*-
# Koda

from koda import models


class ReportPaperformat(models.Model):
    _name = 'report.paperformat'
    _inherit = ['studio.mixin', 'report.paperformat']
