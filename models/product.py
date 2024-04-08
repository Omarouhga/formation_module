from odoo import models, fields

class ProductTemplatnn(models.Model):
    _inherit = 'product.template'


    programme = fields.Html(string='Programme de la formation')
    presentation = fields.Html(string='Objectifs de la formation')
    condition = fields.Html(string='Conditions d\'accés')
    tarifs = fields.Html(string='Modalités de réalisation')
    debouche = fields.Html(string='Les débouchés')


    avantages = fields.Html(string='Avantages')
    programme_acompagnement = fields.Html(string='Programme d\'acompagnement ')
    probleme_resout = fields.Html(string='Problème qu\il résout')
    
    FORMATION_SERVICE_SELECTION = [
        ('formation', 'Formation'),
        ('service', 'Service'),
    ]

    formation_or_service = fields.Selection(FORMATION_SERVICE_SELECTION, string='Formation or Service')