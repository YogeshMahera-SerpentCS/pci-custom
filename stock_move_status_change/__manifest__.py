# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Move Status Change",
    "summary": "",
    "description": """
Adds functions to change the status of stock move records.
""",
    "version": "10.0.1.0.0",
    "category": "Inventory",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "mrp",
    ],
    "data": [
        "views/stock_move_views.xml",
    ],
}
