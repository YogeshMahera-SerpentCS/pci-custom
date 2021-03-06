# -*- coding: utf-8 -*-
# Copyright 2016-2017 Pledra
# Copyright 2017 Willdooit
# Copyright 2017-2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Product Configurator Manufacturing Extended',
    'version': '10.0.1.2.0',
    'category': 'Manufacturing',
    'summary': '',
    'author': 'Pledra, Willdooit, Quartile Limited',
    'license': 'AGPL-3',
    'website': 'https://www.quartile.co',
    'depends': [
        'product_configurator_mrp',
        'mrp_specsheet_py3o',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/product_attribute_value_set_views.xml',
    ],
    'installable': True,
}
