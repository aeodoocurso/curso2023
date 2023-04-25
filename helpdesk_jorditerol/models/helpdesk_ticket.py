from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(
        required=True,
        help='Nombre de la incidencia'
    )
    sequence = fields.Char(
        string='Sequence',
        copy=False,
    )

    description = fields.Text(
        default="""
            Version a la que afecta:
            Modulo:
            Pasos para replicar:
            Modulos personalizados:
        """,
    )
    date = fields.Date()
    date_limit = fields.Datetime(
        string='Limit Date & Time',
    )
    assigned = fields.Boolean(
        string='Assigned to',
        readonly=True, 
    )
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
    )
    
    actions_todo = fields.Html()

    state = fields.Selection(
        string='state',
        selection=[
            ('new', 'New'), 
            ('assigned', 'Assigned'),
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ], 
        default='new'
    )