from odoo import http


class Tuyensinh(http.Controller):
    @http.route('/login_page', auth='public')
    def index(self, **kw):
        return http.request.render('Web-tuyen-sinh-MiKi.login_page')

    # @http.route('/form_page', auth='public')
    # def list(self, **kw):
    #     return http.request.render('tuyensinh.listing', {
    #         'root': '/tuyensinh/tuyensinh',
    #         'objects': http.request.env['tuyensinh.tuyensinh'].search([]),
    #     })
