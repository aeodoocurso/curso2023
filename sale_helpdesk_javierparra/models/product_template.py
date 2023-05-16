from odoo import  fields, models, api, Command, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    helpdesk_tag_id = fields.Many2one(
        comodel_name='helpdesk.ticket.tag',
        string='Tags');

    