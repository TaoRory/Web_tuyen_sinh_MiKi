# -*- coding: utf-8 -*-
# from odoo import http


# class Tuyensinh(http.Controller):
#     @http.route('/tuyensinh/tuyensinh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tuyensinh/tuyensinh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tuyensinh.listing', {
#             'root': '/tuyensinh/tuyensinh',
#             'objects': http.request.env['tuyensinh.tuyensinh'].search([]),
#         })

#     @http.route('/tuyensinh/tuyensinh/objects/<model("tuyensinh.tuyensinh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tuyensinh.object', {
#             'object': obj
#         })

