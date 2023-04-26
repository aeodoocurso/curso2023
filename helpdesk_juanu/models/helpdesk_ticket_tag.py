# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Helpdesk ticket tags'

    name = fields.Char(
        required=True,
    )

    color = fields.Integer(
    )

    description = fields.Text(
    )
