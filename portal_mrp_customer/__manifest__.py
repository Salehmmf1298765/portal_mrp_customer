# -*- coding: utf-8 -*-
{
    'name': 'Portal Manufacturing Orders',
    'summary': 'Adds My Manufacturing Orders to the customer portal with filtered access',
    'version': '18.0.1.0.0',
    'category': 'Manufacturing/Portal',
    'license': 'LGPL-3',
    'author': "Salah Alhjany - Professional Odoo Developer",
    'website': "https://wa.me/967711778764",
    'depends': ['portal', 'stock', 'mrp', 'sale_mrp', 'sale', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'security/mrp_portal_security.xml',
        'views/mrp_portal_templates.xml',
        #'data/portal_mrp_demo.xml',
    ],
    'application': False,
    'installable': True,
}
