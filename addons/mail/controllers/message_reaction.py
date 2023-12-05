# Koda

from werkzeug.exceptions import NotFound

from koda import http
from koda.http import request
from koda.addons.mail.models.discuss.mail_guest import add_guest_to_context


class MessageReactionController(http.Controller):
    @http.route("/mail/message/reaction", methods=["POST"], type="json", auth="public")
    @add_guest_to_context
    def mail_message_add_reaction(self, message_id, content, action):
        message = request.env["mail.message"].browse(int(message_id)).exists()
        if not message._validate_access_for_current_persona("write"):
            raise NotFound()
        message.sudo()._message_reaction(content, action)
