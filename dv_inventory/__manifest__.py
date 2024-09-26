# -*- coding: utf-8 -*-
{
    'name': "Inventario APP",

    'summary': "Inventario de una tienda de productos",

	'author': 'Develogers',
	'website': 'https://develogers.com',
	'support': 'especialistas@develogers.com',
	'live_test_url': 'https://wa.link/2cc9dn',

	'category': 'Extra Tools',
	'version': '15.0',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_produc_views.xml',
        'views/menu_items_view.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}

