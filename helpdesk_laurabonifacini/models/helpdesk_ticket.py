from odoo import models, api, fields

class HelpDeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    # Nombre
    name = fields.Char(required=True, help="Título incidencia resumida.")

    # Secuencia
    sequence = fields.Integer(
        default=10,
        help='Secuencia para'
    )

    # Descripción
    description = fields.Text(
        default="""Versión:
            Módulo:
            """
    )

    # Fecha
    date = fields.Date()

    # Fecha y hora limite
    date_limit = fields.Datetime(
        string='Limit Date & Time')

    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean(
        readonly=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users', 
        string='Assigned to')

    # Acciones a realizar (Html)
    actions_todo = fields.Html()

    # Añadir el campo estado
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

    # 

    