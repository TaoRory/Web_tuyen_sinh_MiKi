from odoo import fields, models, api


class MikiSubject(models.Model):
    _name = 'miki.subject'

    name = fields.Char()
