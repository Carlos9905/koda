# -*- coding: utf-8 -*-
# Koda

from koda import fields, models


class Uom(models.Model):
    _inherit = 'uom.uom'

    def _unprotected_uom_xml_ids(self):
        # Override
        # When timesheet App is installed, we also need to protect the hour UoM
        # from deletion (and warn in case of modification)
        return [
            "product_uom_dozen",
        ]

    # widget used in the webclient when this unit is the one used to encode timesheets.
    timesheet_widget = fields.Char("Widget")
