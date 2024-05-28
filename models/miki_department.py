from odoo import fields, models, api


class MikiDepartment(models.Model):
    _name = 'miki.department'

    name = fields.Char()
    major_ids = fields.Many2many(
        comodel_name='miki.major'
    )