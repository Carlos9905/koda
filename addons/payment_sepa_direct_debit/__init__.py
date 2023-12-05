# Koda

from . import controllers
from . import models

from koda.addons.payment import reset_payment_provider


def uninstall_hook(env):
    reset_payment_provider(env, 'sepa_direct_debit')
