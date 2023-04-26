from odoo import models, api, fields

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = "Desc"

    name = fields.Char(required=True)
    state = fields.Selection(
        selection=[
        ('done', 'Done'),
        ('to_do', 'To Do'),
        ],
        default='to_do',
    )

    def set_actions_as_done(self):
        self.state = 'done'

    def set_done(self):
        self.write({'name': "OK"})

    def set_todo(self):
        self.write({'name': "OK"})      