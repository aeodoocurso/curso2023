from odoo import fields, models

class HelpdeskTicketAction(models.Model):
    _name = "helpdesk.ticket.action"
    _description = "Helpdesk Ticket Action"


# Nombre
name = fields.Char(
    required=True
)
state = fields.Selection(
    selection=[
        ('todo', 'To Do'),
        ('done', 'Done')
    ]
)