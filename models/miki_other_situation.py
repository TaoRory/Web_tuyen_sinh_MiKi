from odoo import fields, models, api


class MikiOtherSituation(models.Model):
    _name = 'miki.other.situation'
    _description = 'Description'

    name = fields.Char()
