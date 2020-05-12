# -*- coding: utf-8 -*-
{
    'name': 'Account Invoice Not Paid Auto Send Mail',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'data/ir_cron.xml',
        'data/ir_configparameter_data.xml'                 
    ],
    'installable': True,
    'auto_install': False,    
}