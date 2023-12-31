# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    calendar_booking_ids = fields.One2many("calendar.booking", "order_line_id", "Bookings")
    calendar_event_id = fields.Many2one("calendar.event", "Meeting")

    @api.depends('calendar_booking_ids')
    def _compute_product_uom_readonly(self):
        booking_so_lines = self.filtered("calendar_booking_ids")
        booking_so_lines.product_uom_readonly = True
        super(SaleOrderLine, self - booking_so_lines)._compute_product_uom_readonly()

    def _is_not_sellable_line(self):
        return super()._is_not_sellable_line() or self.calendar_booking_ids
