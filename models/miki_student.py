from odoo import fields, models, api


class MikiStudent(models.Model):
    _name = 'miki.student'

    name = fields.Char(
        string='Ho ten'
    )

    last_name = fields.Char(
        string='Ho'
    )

    first_name = fields.Char(
        string='Ten'
    )

    dob_date = fields.Date(
        string='ngay thang nam sinh'
    )

    dob_day = fields.Integer()
    dob_month = fields.Integer()
    dob_year = fields.Integer()

    dob_temp = fields.Char()

    gender = fields.Boolean(
        string='gioi tinh'
    )

    ethnicity = fields.Char(
        string='Dan toc'
    )

    nationality = fields.Char(
        string='Quoc tich'
    )

    religion = fields.Char(
        string='Ton giao'
    )

    permanent_province_id = fields.Many2one(
        comodel_name='miki.province',
        string='Permanent province Id'
    )

    permanent_district_id = fields.Many2one(
        comodel_name='miki.district'
    )

    permanent_ward_id = fields.Many2one(
        comodel_name='miki.ward'
    )

    permanent_hamlet = fields.Char()

    permanent_address = fields.Char()

    home_town_province_id = fields.Many2one(
        comodel_name='miki.province'
    )

    home_town_district_id = fields.Many2one(
        comodel_name='miki.district'
    )

    home_town_ward_id = fields.Many2one(
        comodel_name='miki.ward'
    )

    birth_province_id = fields.Many2one(
        comodel_name='miki.province'
    )

    birth_district_id = fields.Many2one(
        comodel_name='miki.district'
    )

    birth_ward_id = fields.Many2one(
        comodel_name='miki.ward'
    )

    birth_address = fields.Char(
        string='Noi sinh'
    )

    current_province_id = fields.Many2one(
        comodel_name='miki.province'
    )

    current_district_id = fields.Many2one(
        comodel_name='miki.district'
    )

    current_ward_id = fields.Many2one(
        comodel_name='miki.ward'
    )

    current_hamlet = fields.Char()

    current_address = fields.Char()

    contact_phone = fields.Char(
        string='so dien thoai'
    )

    citizen_identification_code = fields.Char(
        string='CCCD'
    )

    issued_by = fields.Char(
        string='Noi cap'
    )

    date_range_date = fields.Date(
        string='Ngay cap'
    )

    date_range_day = fields.Integer()
    date_range_month = fields.Integer()
    date_range_year = fields.Integer()

    personal_identification_number = fields.Char(
    )

    father_full_name = fields.Char()
    father_occupation = fields.Char()
    father_dob_year = fields.Integer()
    father_phone = fields.Char()

    mother_full_name = fields.Char()
    mother_occupation = fields.Char()
    mother_dob_year = fields.Integer()
    mother_phone = fields.Char()

    guardian_full_name = fields.Char()
    guardian_occupation = fields.Char()
    guardian_relation = fields.Char()
    guardian_dob_year = fields.Integer()
    guardian_phone = fields.Char()

    student_code = fields.Char(
        string='Ma hoc sinh'
    )

    identification_number = fields.Char(
        string='So bao danh'
    )

    stt_trung_tuyen = fields.Char(
        string='STT trong danh sach trung tuyen'
    )

    student_type_id = fields.Many2one(
        comodel_name='miki.student.type'
    )

    major_id = fields.Many2one(
        comodel_name='miki.major'
    )

    HSG_achievement = fields.Char()
    TDTT_achievement = fields.Char()
    other_achievement = fields.Char()

    miki_priority_situation_id = fields.Many2one(
        comodel_name='miki.priority.situation'
    )
    miki_other_situation_id = fields.Many2one(
        comodel_name='miki.other.situation'
    )

    ## grade
    literature_grade = fields.Float()
    math_grade = fields.Float()
    foreign_language_grade = fields.Float()
    french_grade = fields.Float()
    integration_grade = fields.Float()
    priority_grade = fields.Float()

    sum_grade = fields.Float()

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = (rec.last_name or '') + ' ' + (rec.first_name or '')






