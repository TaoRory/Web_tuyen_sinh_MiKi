from odoo import fields, models, api


class MikiPrioritySituation(models.Model):
    _name = 'miki.priority.situation'

    name = fields.Char()
