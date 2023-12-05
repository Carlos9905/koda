# Koda

from . import controllers
from . import models

from koda.addons.payment import setup_provider, reset_payment_provider


def post_init_hook(env):
    setup_provider(env, 'demo')


def uninstall_hook(env):
    reset_payment_provider(env, 'demo')
