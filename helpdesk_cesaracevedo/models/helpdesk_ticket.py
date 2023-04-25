from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'


    # Nombre
    name = fields.Char(
        required=True,
        help="Resume en procas palabras un titulo para la incidencia."
    )

    # Descripción
    descrioption = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla.",
        default="""Version a la que afecta:
    Modulo:
    Pasos para replicar:
    Modulos personalizados:
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