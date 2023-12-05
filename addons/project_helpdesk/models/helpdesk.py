# -*- coding: utf-8 -*-
# Koda

from koda import models, _

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    def action_convert_to_task(self):
        return {
            'name': _('Convert to Task'),
            'view_mode': 'form',
            'res_model': 'helpdesk.ticket.convert.wizard',
            'views': [(False, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {**self.env.context, 'to_convert': self.ids, 'dialog_size': 'medium',},
        }
