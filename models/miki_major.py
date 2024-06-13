from odoo import fields, models, api


class MikiMajor(models.Model):
    _name = 'miki.major'

    name = fields.Char()

    subject_ids = fields.Many2many(
        comodel_name='miki.subject',
        relation='miki_major_subject',
        column1='major',
        column2='subject'
    )
