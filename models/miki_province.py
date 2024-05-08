from odoo import fields, models, api


class MikiProvince(models.Model):
    _name = 'miki.province'

    name = fields.Char()

    slug = fields.Char()

    type = fields.Char()

    name_with_type = fields.Char()

    code = fields.Char(
    )

    isDeleted = fields.Boolean()