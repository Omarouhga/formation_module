from odoo import models, fields,api
import re
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    type_lead = fields.Selection(string="type d'opportunité", selection=[('service', 'Service'), ('formation', 'Formation')])
    indicatif_paye = fields.Char(string="Indicatif Payé")
    secteur_activite  = fields.Char(string="secteur d'activité ")
    taille_entreprise = fields.Char(string="taille de l'entreprise")
    nombre_experience = fields.Integer(string="Nombre d'années d'expérience")

    

  
  
    # @api.constrains('indicatif_paye', 'phone')
    # def _check_phone_and_indicatif(self):
    #     phone_regex = re.compile(r'^\+?[0-9\s\-]+$')
    #     indicatif_regex = re.compile(r'^\+?[0-9]+$')
        
    #     for record in self:
    #         if record.indicatif_paye and not indicatif_regex.match(record.indicatif_paye):
    #             raise ValidationError("Indicatif Payé must contain only digits and optional leading '+'.")
    #         if record.phone and not phone_regex.match(record.phone):
    #             raise ValidationError("Phone must contain only digits, spaces, hyphens, and optional leading '+'.")
    # def write(self, vals):
    #     if 'indicatif_paye' in vals:
    #         new_indicatif = vals['indicatif_paye']
    #         for record in self:
    #             if record.phone:
    #                 current_phone = record.phone
    #                 # Remove old indicatif_paye if it exists
    #                 if record.indicatif_paye and current_phone.startswith(record.indicatif_paye):
    #                     current_phone = current_phone[len(record.indicatif_paye):]
    #                 # Concatenate new indicatif_paye with phone
    #                 vals['phone'] = new_indicatif + current_phone
    #     return super(CrmLead, self).write(vals)