from odoo import fields, models, api


class MikiWard(models.Model):
    _name = 'miki.ward'

    name = fields.Char()

    type = fields.Char()

    slug = fields.Char()
    name_with_type = fields.Char()
    path = fields.Char()
    path_with_type  = fields.Char()
    code  = fields.Char()
    isDeleted = fields.Boolean()
    parent_code  = fields.Char()
    district_id = fields.Many2one(
        comodel_name='miki.district',
        compute='_compute_district_id',
        store=True
    )


    @api.depends('parent_code')
    def _compute_district_id(self):
        for rec in self:
            if rec.parent_code:
                province_id = self.env['miki.district'].sudo().search([('code', '=', rec.parent_code)])
                if province_id:
                    rec.district_id = province_id[0].id
                else:
                    rec.district_id= None
            else:
                rec.district_id = None