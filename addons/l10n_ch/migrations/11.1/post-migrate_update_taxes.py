# Koda
from koda import api, SUPERUSER_ID


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for company in env['res.company'].search([('chart_template', '=', 'ch')]):
        env['account.chart.template'].with_context(force_new_tax_active=True).try_loading('ch', company)
