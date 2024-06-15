from odoo import fields, models, api


class MikiStudentType(models.Model):
    _name = 'miki.student.type'

    name = fields.Char()
    department_ids = fields.Many2many(
        comodel_name='miki.department'
    )
