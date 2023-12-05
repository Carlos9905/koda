# -*- coding: utf-8 -*-
# Koda

from . import models
from . import controllers


def _set_tax_on_work_in_out(env):
    env['product.product'].set_tax_on_work_in_out()
