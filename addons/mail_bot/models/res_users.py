# -*- coding: utf-8 -*-
# Koda

from markupsafe import Markup

from koda import models, fields, _

class Users(models.Model):
    _inherit = 'res.users'

    kodabot_state = fields.Selection(
        [
            ('not_initialized', 'Not initialized'),
            ('onboarding_emoji', 'Onboarding emoji'),
            ('onboarding_attachement', 'Onboarding attachment'),
            ('onboarding_command', 'Onboarding command'),
            ('onboarding_ping', 'Onboarding ping'),
            ('idle', 'Idle'),
            ('disabled', 'Disabled'),
        ], string="OdooBot Status", readonly=True, required=False)  # keep track of the state: correspond to the code of the last message sent
    kodabot_failed = fields.Boolean(readonly=True)

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['kodabot_state']

    def _init_messaging(self):
        kodabot_onboarding = False
        if self.kodabot_state in [False, 'not_initialized'] and self._is_internal():
            kodabot_onboarding = True
            self._init_kodabot()
        res = super()._init_messaging()
        res['kodabotOnboarding'] = kodabot_onboarding
        return res

    def _init_kodabot(self):
        self.ensure_one()
        kodabot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
        channel = self.env['discuss.channel'].channel_get([kodabot_id, self.partner_id.id])
        message = Markup("%s<br/>%s<br/><b>%s</b> <span class=\"o_kodabot_command\">:)</span>") % (
            _("Hello,"),
            _("Odoo's chat helps employees collaborate efficiently. I'm here to help you discover its features."),
            _("Try to send me an emoji")
        )
        channel.sudo().message_post(body=message, author_id=kodabot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
        self.sudo().kodabot_state = 'onboarding_emoji'
        return channel
