/** @koda-module */

import { SocialPostFormatterMixinBase } from '@social/js/social_post_formatter_mixin';

import { patchWithCleanup } from "@web/../tests/helpers/utils";

QUnit.module('Social Formatter Regex', {}, () => {
    QUnit.test('Facebook Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'facebook' },
            _formatPost() {
                this.originalPost = { account_id: { raw_value: 42 } };
                return super._formatPost(...arguments);
            }
        });

        const testMessage = 'Hello @[542132] Odoo-Social, check this out: https://www.koda.com?utm=mail&param=1 #crazydeals #koda';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='/social_facebook/redirect_to_profile/42/542132?name=Odoo-Social' target='_blank'>Odoo-Social</a>,",
            "check this out:",
            "<a href='https://www.koda.com?utm=mail&amp;param=1' target='_blank' rel='noreferrer noopener'>https://www.koda.com?utm=mail&amp;param=1</a>",
            "<a href='https://www.facebook.com/hashtag/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.facebook.com/hashtag/koda' target='_blank'>#koda</a>",
        ].join(' '));
    });

    QUnit.test('Instagram Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'instagram' },
        });

        const testMessage = 'Hello @Odoo.Social, check this out: https://www.koda.com #crazydeals #koda';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://www.instagram.com/Odoo.Social' target='_blank'>@Odoo.Social</a>,",
            "check this out:",
            "<a href='https://www.koda.com' target='_blank' rel='noreferrer noopener'>https://www.koda.com</a>",
            "<a href='https://www.instagram.com/explore/tags/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.instagram.com/explore/tags/koda' target='_blank'>#koda</a>",
        ].join(' '));
    });

    QUnit.test('LinkedIn Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'linkedin' },
        });

        const testMessage = 'Hello, check this out: https://www.koda.com {hashtag|#|crazydeals} #koda';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='https://www.koda.com' target='_blank' rel='noreferrer noopener'>https://www.koda.com</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/koda' target='_blank'>#koda</a>",
        ].join(' '));
    });

    QUnit.test('Twitter Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'twitter' },
        });

        const testMessage = 'Hello @Odoo-Social, check this out: https://www.koda.com #crazydeals #koda';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://twitter.com/Odoo-Social' target='_blank'>@Odoo-Social</a>,",
            "check this out:",
            "<a href='https://www.koda.com' target='_blank' rel='noreferrer noopener'>https://www.koda.com</a>",
            "<a href='https://twitter.com/hashtag/crazydeals?src=hash' target='_blank'>#crazydeals</a>",
            "<a href='https://twitter.com/hashtag/koda?src=hash' target='_blank'>#koda</a>",
        ].join(' '));
    });

    QUnit.test('YouTube Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'youtube' },
        });

        const testMessage = 'Hello, check this out: https://www.koda.com #crazydeals #koda';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='https://www.koda.com' target='_blank' rel='noreferrer noopener'>https://www.koda.com</a>",
            "<a href='https://www.youtube.com/results?search_query=%23crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.youtube.com/results?search_query=%23koda' target='_blank'>#koda</a>",
        ].join(' '));
    });
});
