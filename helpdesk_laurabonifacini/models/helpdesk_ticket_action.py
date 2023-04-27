from odoo import models, fields

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = "Helpdesk Ticket Action"

    name = fields.Char(required=True)

    state = fields.Selection(
        selection=[
            ('to_do', 'To Do'),
            ('done', 'Done'),
        ],
        default='to_do',
    )

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket')

    def set_done(self):
        self.write({'state': "done"})

    def set_todo(self):
        self.write({'state': "to_do"})     