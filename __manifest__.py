# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'restrict_mail_for_sale_order',
    'version': '1.0',
    'summary': "Restrict mail for sale order module",
    'sequence': 14,
    'author': "anand",
    'description': """
Restrict Chatter Mail for Sale Order""",
    'category': 'Custom/Sale',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail', 'sale', 'base'],
    'data': [
        'views/partner.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
