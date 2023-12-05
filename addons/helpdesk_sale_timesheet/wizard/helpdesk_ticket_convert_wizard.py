# -*- coding: utf-8 -*-
# Koda

from koda import models

class HelpdeskTicketConvertWizard(models.TransientModel):
    _inherit = 'helpdesk.ticket.convert.wizard'

    def _get_task_values(self, ticket):
        return {
            **super()._get_task_values(ticket),
            'sale_line_id': ticket.sale_line_id.id,
        }
