from odoo import  fields, models

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Ticket Action'

    #nombre
    name = fields.Char(
        required=True,
    )
    
    #state
    state = fields.Selection(
        selection=[
            ('todo', 'Todo'),
            ('done', 'Done'),
        ],
        default='todo'
        )
    
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket',
    )

        