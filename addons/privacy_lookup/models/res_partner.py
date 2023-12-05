# -*- coding: utf-8 -*-
# Koda

from koda import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_privacy_lookup(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('privacy_lookup.action_privacy_lookup_wizard')
        action['context'] = {
            'default_email': self.email,
            'default_name': self.name,
        }
        return action
