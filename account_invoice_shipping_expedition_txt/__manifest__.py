# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Account Invoice Shipping Expedition TXT',
    'version': '12.0.1.0.0',
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'account_invoice_shipping_expedition', 'shipping_expedition_txt'],
    'external_dependencies': {
        'python' : ['xlrd'],
    },
    'data': [],
    'installable': True,
    'auto_install': False,
}