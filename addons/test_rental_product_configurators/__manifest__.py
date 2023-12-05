# -*- coding: utf-8 -*-
# Koda

{
    'name': "Rental Product Configurators Tests",
    'summary': "Test Suite for Rental Product Configurators",
    'category': "Hidden",
    'depends': [
        'sale_renting',
        'test_sale_product_configurators',
    ],
    'assets': {
        'web.assets_tests': [
            'test_rental_product_configurators/static/tests/tours/**/*',
        ],
    },
    'license': 'OEEL-1',
}
