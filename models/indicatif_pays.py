from odoo import models, fields

class IndicatifPays(models.Model):
    _name = 'indicatif.pays'

    name = fields.Char(string='Nom du pays')
    indicatif = fields.Char(string='Indicatif téléphonique')
    continent = fields.Selection([
        ('afrique', 'Afrique'),
        ('amerique_nord_antilles', 'Amérique du Nord & Antilles'),
        ('amerique_sud', 'Amérique du Sud'),
        ('asie', 'Asie'),
        ('europe', 'Europe'),
        ('oceanie', 'Océanie'),
        ('autre', 'Autre')], string='Continent')
