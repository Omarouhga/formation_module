from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    programme = fields.Html(string='Programme')
    presentation = fields.Html(string='Présentation')
    condition = fields.Html(string='Conditions d\'admission')
    tarifs = fields.Html(string='Tarifs de formation')
    is_formation=fields.Boolean(string='Formation ?')

