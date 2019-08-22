# -*- coding: utf-8 -*-
from odoo import http

# class XmartsMonitoringControl(http.Controller):
#     @http.route('/xmarts_monitoring_control/xmarts_monitoring_control/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_monitoring_control/xmarts_monitoring_control/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_monitoring_control.listing', {
#             'root': '/xmarts_monitoring_control/xmarts_monitoring_control',
#             'objects': http.request.env['xmarts_monitoring_control.xmarts_monitoring_control'].search([]),
#         })

#     @http.route('/xmarts_monitoring_control/xmarts_monitoring_control/objects/<model("xmarts_monitoring_control.xmarts_monitoring_control"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_monitoring_control.object', {
#             'object': obj
#         })