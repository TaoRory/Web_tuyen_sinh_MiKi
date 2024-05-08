from odoo import fields, models, api


class MikiStudent(models.Model):
    _name = 'miki.student'

    name = fields.Char()

    dob_day = fields.Integer()
    dob_month = fields.Integer()
    dob_year = fields.Integer()

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female')
        ]
    )

    ethnicity = fields.Char()

    nationality = fields.Char()

    religion = fields.Char()

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

    birth_address = fields.Char()

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

    contact_phone = fields.Char()

    citizen_identification_code = fields.Char()

    issued_by = fields.Char()

    date_range_day = fields.Integer()
    date_range_month = fields.Integer()
    date_range_year = fields.Integer()

    personal_identification_number = fields.Char()

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
    guardian_dob_year = fields.Integer()
    guardian_phone = fields.Char()










