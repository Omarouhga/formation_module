# from odoo import api, models,fields , _

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     @api.model
#     def create(self, vals):
#         record = super(SaleOrder, self).create(vals)
#         if 'name' not in vals or vals['name'] == _('New'):
#             sequence_code = 'kinder.sale.order'
#             record['name'] = self.env['ir.sequence'].next_by_code(sequence_code) or _('New')
#         return record


# class IrSequence(models.Model):
#     _inherit = 'ir.sequence'

#     def reset_sequence(self):
#         self.write({'number_next': 1})
#         today = fields.Date.today()
#         self.date_range_ids.create({
#             'name': today,
#             'start_date': today,
#             'end_date': today,
# #         })
# from odoo import api, fields, models

# class TargetSeq(models.Model):
#     _name ="target.model.name"
#     def sales_number_update(self):
#         sequence_obj = self.env['ir.sequence']
#         seq_id = sequence_obj.search([('code', '=', 'new.move.account')], limit=1)         
#         if seq_id:
#             sequence_obj.browse(seq_id).write({'number_next': 1})
#         return True

# class AccountMoveInherited(models.Model):

#     _inherit = 'account.move'
#     @api.model
#     def create(self, vals):
#         record = super(AccountMoveInherited, self).create(vals)
#         record['name'] = self.env['ir.sequence'].next_by_code('new.account.move') or _('New')
#         return record

from odoo import models, fields

class AccountMoveWithCustomSequence(models.Model):
    _inherit = 'account.move'

    def create(self, vals):
        # If the 'name' field is not set or set to '/', use the custom sequence
        if 'name' not in vals or vals['name'] == '/':
            sequence_code = 'fac.daily.sequence'  # Use the custom sequence defined in XML
            new_sequence = self.env['ir.sequence'].next_by_code(sequence_code)  # Get the next number
            vals['name'] = new_sequence  # Assign the custom sequence to the 'name' field

        return super(AccountMoveWithCustomSequence, self).create(vals)
