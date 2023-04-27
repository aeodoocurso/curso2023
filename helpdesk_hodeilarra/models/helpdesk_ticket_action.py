from odoo import fields, models

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Ticket Action'

    name = fields.Char(required=True)

    #estado
    state = fields.Selection(
        selection=[
            ('todo', 'To do'),
            ('done', 'Done')],
        string='Estado', default='todo',
    )

    ticket_id = fields.Many2one(comodel_name="helpdesk.ticket", string="Ticket")

    def set_done(self):
        self.write({'state': "done"})

    def set_todo(self):
        self.write({'state': "todo"})