# -*- coding: utf-8 -*-
# Koda


from unittest.mock import patch

from koda.addons.social_facebook.models.social_account import SocialAccountFacebook
from koda.addons.social.tests.common import SocialCase


class SocialFacebookCommon(SocialCase):
    @classmethod
    def setUpClass(cls):
        with patch.object(SocialAccountFacebook, '_compute_statistics', lambda x: None), \
             patch.object(SocialAccountFacebook, '_create_default_stream_facebook', lambda *args, **kwargs: None):
            super(SocialFacebookCommon, cls).setUpClass()
