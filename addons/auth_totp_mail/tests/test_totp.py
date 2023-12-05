# -*- coding: utf-8 -*-
# Koda

from koda.tests import tagged
from koda.addons.auth_totp.tests.test_totp import TestTOTP


@tagged('post_install', '-at_install')
class TestTOTPInvite(TestTOTP):

    def test_totp_administration(self):
        self.start_tour('/web', 'totp_admin_invite', login='admin')
        self.start_tour('/web', 'totp_admin_self_invite', login='admin')
