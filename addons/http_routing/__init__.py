# Koda

from . import controllers
from . import models

from koda.http import request


def _post_init_hook(env):
    if request:
        request.is_frontend = False
        request.is_frontend_multilang = False
