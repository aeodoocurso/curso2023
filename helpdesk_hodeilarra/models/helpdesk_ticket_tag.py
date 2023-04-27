from odoo import fields, models

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Helpdesk Ticket Tag'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)