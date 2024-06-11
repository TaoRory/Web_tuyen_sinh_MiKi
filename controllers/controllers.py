from odoo import http
from odoo.http import request


class Tuyensinh(http.Controller):
    @http.route('/login_page', auth='public')
    def index(self, **kw):
        return http.request.render('Web-tuyen-sinh-MiKi.login_page')

    @http.route('/check-student', auth='public', type='json', methods=['POST'])
    def check(self, **kw):
        print(kw)
        student_id = request.env['miki.student'].sudo().search([
            ('student_code', '=', kw.get('mhs')),
            ('identification_number', '=', kw.get('sbd'))
        ])
        data ={}
        if student_id:
            data['student_name'] = student_id.name
            data['day_of_birth'] = student_id.dob_temp
        else:
            data['error'] = True
        print(data)
        return data

    # @http.route('/form_page', auth='public')
    # def list(self, **kw):
    #     return http.request.render('tuyensinh.listing', {
    #         'root': '/tuyensinh/tuyensinh',
    #         'objects': http.request.env['tuyensinh.tuyensinh'].search([]),
    #     })
