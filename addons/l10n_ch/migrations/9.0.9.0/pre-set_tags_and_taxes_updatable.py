# -*- coding: utf-8 -*-

import koda

def migrate(cr, version):
    registry = koda.registry(cr.dbname)
    from koda.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_ch')

