# -*- coding: utf-8 -*-
# Koda
from koda import api
from koda.models import AbstractModel
from koda.tools import cloc

class PublisherWarrantyContract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_message(self):
        msg = super()._get_message()

        ICP = self.env["ir.config_parameter"]
        if ICP.get_param('publisher_warranty.maintenance_disable') is not False:
            return msg

        msg['maintenance'] = {
            "version": cloc.VERSION,
        }
        try:
            c = cloc.Cloc()
            c.count_env(self.env)
            if c.code:
                msg["maintenance"]["modules"] = c.code
            if c.errors:
                msg["maintenance"]["errors"] = list(c.errors.keys())
        except Exception:
            msg["maintenance"]["errors"] = ['cloc/error']
        return msg

    @api.model
    def _get_verbose_maintenance(self):
        """ can be called by a SA to debug cloc issue
            Without runing koda-bin cloc which is not always possible
        """
        c = cloc.Cloc()
        c.count_env(self.env)
        return {
            "modules_count": c.modules,
            "modules_excluded": c.excluded,
        }
