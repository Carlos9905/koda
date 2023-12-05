# Koda

from koda import fields, models


class ShiprocketChannel(models.Model):
    _name = 'shiprocket.channel'
    _description = 'Shiprocket Channel'
    _order = 'name'

    name = fields.Char('Channel Name', readonly=True)
    channel_code = fields.Integer('Channel Code', readonly=True)
    shiprocket_email = fields.Char(string='Shiprocket Email')
