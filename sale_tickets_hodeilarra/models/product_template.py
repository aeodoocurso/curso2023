from odoo import models, api, fields, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    helpdesk_tag_id = fields.Many2one('helpdesk.ticket.tag', string='Helpdesk Tag')