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
#         })
from odoo import api, fields, models

class TargetSeq(models.Model):
    _name ="target.model.name"
    def sales_number_update(self):
        sequence_obj = self.env['ir.sequence']
        seq_id = sequence_obj.search([('code', '=', 'sale.order')], limit=1)         
        if seq_id:
            sequence_obj.browse(seq_id).write({'number_next': 1})
        return True
