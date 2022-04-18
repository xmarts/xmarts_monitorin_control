# -*- coding: utf-8 -*-
{
    'name': "xmarts_monitoring_control",
    'summary': """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """Long description of module's purpose""",
    'author': "Xmarts",
    'contributors': "daviddiaz@xmarts.com, javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'stock',
        'purchase',
        'sale',
        'contacts',
        'sale_management',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/monitoring_control_views.xml',
        'views/inherit_res_partner_views.xml',
    ],
}
