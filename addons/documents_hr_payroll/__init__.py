# -*- coding: utf-8 -*-
# Koda

from . import models


def _generate_payroll_document_folders(env):
    env['res.company'].search([])._generate_payroll_document_folders()
