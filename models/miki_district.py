from odoo import fields, models, api


class MikiDistrict(models.Model):
    _name = 'miki.district'

    name = fields.Char()

    type = fields.Char()

    slug = fields.Char()

    name_with_type = fields.Char()

    path = fields.Char()

    path_with_type = fields.Char()

    code = fields.Char()

    parent_code = fields.Char()

    isDeleted = fields.Boolean()

    province_id = fields.Many2one(
        comodel_name='miki.province',
        domain="[('code', '=', 'parent_code')]",
        compute='_compute_province_id',
        store=True
    )

    @api.depends('parent_code')
    def _compute_province_id(self):
        for rec in self:
            if rec.parent_code:
                province_id = self.env['miki.province'].sudo().search([('code', '=', rec.parent_code)])
                if province_id:
                    rec.province_id = province_id[0].id
                else:
                    rec.province_id= None
            else:
                rec.province_id= None