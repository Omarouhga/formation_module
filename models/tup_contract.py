from odoo import models, fields

class HRupContact(models.Model):
    _inherit = 'hr.contract'

    EMPLOYMENT_TYPE_SELECTION = [
        ('salaried', 'Salarié'),
        ('freelancer_com', 'Freelancer avec commission'),
        ('freelancer_daily', 'Freelencer avec Taux journalier')
    ]

    employment_type = fields.Selection(selection=EMPLOYMENT_TYPE_SELECTION, string='Type d\'emploi',    default='salaried')
    commission_rate = fields.Float(string='Taux de Commission')
    daily_rate = fields.Float(string='Prix Par jour')
