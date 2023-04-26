from odoo import  fields, models

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Helpdesk Ticket Tag'


    #nombre
    name = fields.Char(
        required=True,
    )