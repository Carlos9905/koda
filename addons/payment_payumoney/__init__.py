# Koda

from . import controllers
from . import models

from koda.exceptions import UserError
from koda.tools import config

from koda.addons.payment import setup_provider, reset_payment_provider


def pre_init_hook(env):
    if not any(config.get(key) for key in ('init', 'update')):
        raise UserError(
            "This module is deprecated and cannot be installed. "
            "Consider installing the Payment Provider: Razorpay module instead.")


def post_init_hook(env):
    setup_provider(env, 'payumoney')


def uninstall_hook(env):
    reset_payment_provider(env, 'payumoney')
