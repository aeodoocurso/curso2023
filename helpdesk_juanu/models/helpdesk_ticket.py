# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk ticket'

    name = fields.Char(
        required=True,
        help="Resumen de la incidencia.",
    )

    description = fields.Text(
        help="Describe detalladamente de la incidencia.",
        default=""""Version a la que afecta:Modulo:Version:""",
    )

    date = fields.Date(
    )

    date_limit = fields.Datetime(
        string="Date & Time limit",
    )

    assigned = fields.Boolean(
    )

    actions_todo = fields.Html(
    )
