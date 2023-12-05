# Koda

from koda import _

class WhatsAppError(Exception):
    def __init__(self, message='', error_code=False, failure_type=False):
        """Handle errors for whatsapp API, storing error codes.

        :param str message: An error message
        :param int error_code: Whatsapp error code
        :param str failure_type: Member of failure_type selection in <whatsapp.message>
        """
        self.failure_type = failure_type
        self.error_code = error_code
        self.error_message = message

        formated_message = ''
        if error_code:
            formated_message = f'{error_code}: {message}'
        elif failure_type == 'account':
            formated_message = _("Whatsapp account is misconfigured or shared.")
        elif failure_type == 'network':
            formated_message = _("Whatsapp could not be reached or the query was malformed.")
        else:
            formated_message = _("Unknown error when processing whatsapp request.")

        super().__init__(formated_message)
