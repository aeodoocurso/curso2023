from odoo import models, api, fields

class HelpDeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    # Nombre
    name = fields.Char(
        required=True,
        help="Título incidencia resumida."
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
    date_limit = fields.Datetime(string='Limit Date & Time')

    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean()

    # Acciones a realizar (Html)
    actions_todo = fields.Html()

    