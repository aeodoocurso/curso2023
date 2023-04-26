from odoo import fields, models

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Ticket Action'

    name = fields.Char(
        string='Name',
    )

    state = fields.Selection(
        string='state',
        selection=[
            ('todo', 'To do'), 
            ('done', 'Done'),
        ], 
        default='todo'
    )

    ticket_id = fields.Many2one(
        'helpdesk.ticket',
        string='Ticket',
    )

    def set_done(self):
        self.write({'state': "done"})
    
    def set_todo(self):
        self.write({'state': "todo"})