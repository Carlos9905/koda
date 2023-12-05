# Koda

from . import models
from . import controllers

from koda.addons.payment import setup_provider, reset_payment_provider


def post_init_hook(env):
    setup_provider(env, 'sips')


def uninstall_hook(env):
    reset_payment_provider(env, 'sips')
