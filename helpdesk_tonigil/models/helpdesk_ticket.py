from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"

    # Secuencia
    sequence = fields.Integer()
    
    # Nombre
    name = fields.Char(
        string = 'Nombre',
        required=True,
        help="Resume en pocas palabras, un título para la incidencia"
    )

    # Descripción
    description = fields.Text(
        string = 'Descripción',
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
    date_limit = fields.Datetime()

    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean(
        readonly=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to'
    )

    # Acciones a realizar (Html)
    actions_todo = fields.Html()

    # Añadir el campo Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection(
        selection=[
        ('new', 'New'),
        ('assigned', 'Asigned'),
        ('in_process', 'In Process'),
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
        ],
        default='new',
    )