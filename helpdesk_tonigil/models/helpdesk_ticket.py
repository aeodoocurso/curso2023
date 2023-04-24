from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"


    # Nombre
    name = fields.Char(
        required=True,
        help="Resume en pocas palabras, un título para la incidencia"
    )

    # Descripción
    description = fields.Text(
        help="Escribe detalladamente la incidencia. Cuanta más información aportes, más fácil será ayudarte.",
        default="""Versión a la que afecta:
        Módulo:
        Pasos para replicar:
        Módulos personalizados:
        """
    )

    # Fecha
    date = fields.Date()

    # Fecha y hora limite
    date_limit = fields.Datetime(
        string='Limit Date & Time')

    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean()

    # Acciones a realizar (Html)
    actions_todo = fields.Html()