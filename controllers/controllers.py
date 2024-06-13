from odoo import http
from odoo.http import request


class Tuyensinh(http.Controller):
    ## First page/ Login
    @http.route('/login_page', auth='public')
    def LoginPage(self, **kw):
        return http.request.render('Web-tuyen-sinh-MiKi.login_page')

    @http.route('/check-student', auth='public', type='json', methods=['POST'])
    def Check(self, **kw):
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

    @http.route('/district', auth='public', type='json', methods=['POST'])
    def GetDistrict(self, **kw):

        district_ids = request.env['miki.district'].sudo().search([
            ('province_id', '=', int(kw.get('province_id'))),
        ])
        data ={}
        data['districts'] = []
        for district in district_ids:
            data['districts'].append({
                'id': district.id,
                'name': district.name
            })
        return data
    @http.route('/ward', auth='public', type='json', methods=['POST'])
    def GetWard(self, **kw):

        ward_ids = request.env['miki.ward'].sudo().search([
            ('district_id', '=', int(kw.get('district_id'))),
        ])
        data ={}
        data['wards'] = []
        for ward in ward_ids:
            data['wards'].append({
                'id': ward.id,
                'name': ward.name
            })
        return data

    ## Second page/ Information
    @http.route('/information_page', auth='public')
    def InformationPage(self, **kw):
        print('asd')
        print(kw)

        student = request.env['miki.student'].sudo().search([
            ('identification_number', '=', kw.get('sbd')),
            ('student_code', '=', kw.get('mhs'))
        ])
        department_ids = request.env['miki.department'].sudo().search([(1,'=',1)])
        if not student:
            return http.request.redirect('/login_page')
        if student.permanent_province_id:
            province_ids = request.env['miki.province'].sudo().browse(student.permanent_province_id.id)
            district_ids = request.env['miki.district'].sudo().search([
                ('province_id', '=', student.permanent_province_id.id)
            ])
        else:
            province_ids = request.env['miki.province'].sudo().search([(1,'=',1)])

        return http.request.render('Web-tuyen-sinh-MiKi.information_page', {
            'student': student,
            'province_ids': province_ids,
            'department_ids': department_ids
        })

    @http.route('/information_page/submit', auth='public')
    def InformationPageSubmit(self, **kw):
        print(kw)
        student_id = request.env['miki.student'].sudo().search([
            ('student_code', '=', kw.get('student_code')),
            ('identification_number', '=', kw.get('identification_number'))
        ])
        kw.pop('student_code', 'Key not found')
        kw.pop('identification_number', 'Key not found')
        kw['permanent_province_id'] = int(kw.get('permanent_province_id')) if kw.get('permanent_province_id') else 'None'
        kw['permanent_district_id'] = int(kw.get('permanent_district_id')) if kw.get('permanent_district_id') else 'None'
        kw['permanent_ward_id'] = int(kw.get('permanent_ward_id')) if kw.get('permanent_ward_id') else 'None'
        kw['home_town_province_id'] = int(kw.get('home_town_province_id')) if kw.get('home_town_province_id') else 'None'
        kw['home_town_district_id'] = int(kw.get('home_town_district_id')) if kw.get('home_town_district_id') else 'None'
        kw['home_town_ward_id'] = int(kw.get('home_town_ward_id')) if kw.get('home_town_ward_id') else 'None'
        kw['birth_province_id'] = int(kw.get('birth_province_id')) if kw.get('birth_province_id') else 'None'
        kw['birth_district_id'] = int(kw.get('birth_district_id')) if kw.get('birth_district_id') else 'None'
        kw['birth_ward_id'] = int(kw.get('birth_ward_id')) if kw.get('birth_ward_id') else 'None'
        kw['current_province_id'] = int(kw.get('current_province_id')) if kw.get('current_province_id') else 'None'
        kw['current_district_id'] = int(kw.get('current_district_id')) if kw.get('current_district_id') else 'None'
        kw['current_ward_id'] = int(kw.get('current_ward_id')) if kw.get('current_ward_id') else 'None'
        kw['major_id'] = int(kw.get('major_id')) if kw.get('major_id') else 'None'
        student_id.sudo().write(kw)


