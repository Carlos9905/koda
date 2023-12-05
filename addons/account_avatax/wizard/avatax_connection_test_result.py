# -*- coding: utf-8 -*-
# Koda
from koda import models, fields


class AvataxConnectionTestResult(models.TransientModel):
    _name = "avatax.connection.test.result"
    _description = 'Test connection with avatax'

    server_response = fields.Html(string='Server Response')
