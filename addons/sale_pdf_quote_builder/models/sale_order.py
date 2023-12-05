# Koda

from koda import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _filter_product_documents(self, documents):
        return (
            super()._filter_product_documents(documents)
            | documents.filtered(lambda document: document.attached_on == 'inside')
        )
