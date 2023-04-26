from odoo import models, api, fields

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = "Desc"

    name = fields.Char(required=True)
    date = fields.Date()
    state = fields.Selection(
        selection=[
        ('done', 'Done'),
        ('assigned', 'Assigned'),
        ],
        default='new',
    )
     