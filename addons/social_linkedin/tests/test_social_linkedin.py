# -*- coding: utf-8 -*-
# Koda

import requests

from unittest.mock import patch
from koda.addons.social.tests.common import SocialCase
from koda.addons.social.tests.tools import mock_void_external_calls
from koda.addons.social_linkedin.models.social_live_post import SocialLivePostLinkedin
from koda.addons.social_linkedin.models.social_account import SocialAccountLinkedin
from koda.tools.misc import mute_logger


class SocialLinkedinCase(SocialCase):
    @classmethod
    def setUpClass(cls):
        with mock_void_external_calls():
            super(SocialLinkedinCase, cls).setUpClass()
            cls.social_accounts.write({'linkedin_access_token': 'ABCD'})

    def test_post_success(self):
        self._test_post()

    def test_post_failure(self):
        self._test_post(False)

    @mute_logger("koda.addons.social.models.social_account")
    def _test_post(self, success=True):
        self.assertEqual(self.social_post.state, 'draft')

        def _patched_post(*args, **kwargs):
            response = requests.Response()
            if success:
                response._content = b'{"id": "42"}'
                response.status_code = 200
                response.headers = {'x-restli-id': 'fake_created_post_urn'}
            else:
                response._content = b'{"serviceErrorCode": 65600}'
                response.status_code = 404
            return response

        with patch.object(requests, 'post', _patched_post), \
             patch.object(SocialLivePostLinkedin, '_linkedin_upload_image', lambda *a, **kw: 'fake_image_urn'):
            self.social_post._action_post()

        self._checkPostedStatus(success)

        if success:
            linkedin_post_id = self.social_post.live_post_ids.mapped('linkedin_post_id')
            self.assertEqual(linkedin_post_id, ['fake_created_post_urn'] * 2)
            self.assertTrue(
                all([not account.is_media_disconnected for account in self.social_post.account_ids]),
                'Accounts should not be marked disconnected if post is successful')
        else:
            self.assertTrue(
                all([account.is_media_disconnected for account in self.social_post.account_ids]),
                'Accounts should be marked disconnected if post has failed')

    def test_post_image(self):
        """
        Check the priority of the ``post type``
        The first priority is image
        """
        self.social_post.message = 'A message https://koda.com'
        self.assertTrue(self.social_post.image_ids)
        self._test_post_type('multiImage')

    def test_post_urls(self):
        """
        Check the priority of the ``post type``
        The second priority is urls
        """
        self.social_post.message = 'A message https://koda.com'
        self.social_post.image_ids = False
        self._test_post_type('article')

    def test_post_text(self):
        """
        Check the priority of the ``post type``
        The last priority is text
        """
        self.social_post.message = 'A message without URL'
        self.social_post.image_ids = False
        self._test_post_type(None)

    def _test_post_type(self, expected_post_type):
        self.assertEqual(self.social_post.state, 'draft')

        def _patched_post(*args, **kwargs):
            response = requests.Response()
            response._content = b'{"id": "42"}'
            response.status_code = 200

            post_type = next(iter(kwargs.get('json', {}).get('content', {})), None)

            responses.append(post_type)
            return response

        responses = []
        with patch.object(requests, 'post', _patched_post), \
             patch.object(SocialLivePostLinkedin, '_linkedin_upload_image', lambda *a, **kw: 'fake_image_urn'):
            self.social_post._action_post()

        self.assertTrue(responses)
        self.assertTrue(all([response == expected_post_type for response in responses]),
                        'The post type must be [%s]' % expected_post_type)

    @classmethod
    def _get_social_media(cls):
        return cls.env.ref('social_linkedin.social_media_linkedin')

    def _get_commentary_after_post(self):
        commentaries = []

        def _patched_post(*args, **kwargs):
            commentaries.append(kwargs.get('json', {}).get('commentary', None))

        with patch.object(requests, 'post', _patched_post):
            self.social_post._action_post()

        return commentaries

    def test_post_with_special_char(self):
        """
        Check the priority of the ``post type``
        The last priority is text
        """
        self.social_post.message = '(This) <is> {a} [test] string <3'
        self.social_post.image_ids = False
        commentaries = self._get_commentary_after_post()
        expected_output = '\\(This\\) \\<is\\> \\{a\\} \\[test\\] string \\<3'
        self.assertTrue(all([commentary == expected_output for commentary in commentaries]))
