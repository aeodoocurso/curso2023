# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk ticket'

    name = fields.Char(
        required=True,
        help="Resumen de la incidencia.",
    )

    sequence = fields.Integer(
        default=10,
        help="Secuencia para el orden de incendencias",
    )

    description = fields.Text(
        help="Describe detalladamente de la incidencia.",
        default=""""Version a la que afecta:Modulo:Version:""",
    )

    date = fields.Date(
        default=lambda self: fields.datetime.now()
    )

    date_limit = fields.Datetime(
        string="Date & Time limit",
    )

    assigned = fields.Boolean(
        readonly=True,
    )

    user_id = fields.Many2one(
        string="Assigned to",
        comodel_name="res.users"
    )

    actions_todo = fields.Html(
    )

    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('in_process', 'In process'),
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ],
        default='new',
    )

    action_ids = fields.One2many(
        string="Actions",
        comodel_name="helpdesk.ticket.action",
        inverse_name="ticket_id",
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
        string='Tags')

    def update_description(self):
        for record in self:
            record.description = "OK"
