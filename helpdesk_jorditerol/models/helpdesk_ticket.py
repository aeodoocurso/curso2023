from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(
        required=True,
        help='Nombre de la incidencia'
    )
    description = fields.Text()
    date = fields.Date()
    date_limit = fields.Datetime(
        string='Limit Date & Time'
    )
    assigned = fields.Boolean()
    actions_todo = fields.Html()