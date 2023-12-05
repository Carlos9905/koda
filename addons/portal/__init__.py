# -*- coding: utf-8 -*-
# Koda

# Updating mako environement in order to be able to use slug
try:
    from koda.tools.rendering_tools import template_env_globals
    from koda.addons.http_routing.models.ir_http import slug

    template_env_globals.update({
        'slug': slug
    })
except ImportError:
    pass

from . import controllers
from . import models
from . import wizard
