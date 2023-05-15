# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk ticket actions'

    name = fields.Char(
        required=True,
    )

    description = fields.Text(
        help="Action description.",
    )

    state = fields.Selection(
        selection=[
            ('todo', 'To do'),
            ('done', 'Done'),
        ],
        default='todo',
    )

    ticket_id = fields.Many2one(
        string="Ticket",
        comodel_name="helpdesk.ticket",
    )

    def set_done(self):
        self.write({'state': "done"})

    def set_todo(self):
        self.write({'state': "todo"})