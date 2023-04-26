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
        default="""
        Versión a la que afecta:
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

    # Añadir el método que actualiza la descripción del ticket (únicamente el registro 'self')
    def update_description(self):
        self.write({'name': "Un valor X"})


    def update_all_description(self):
        self.ensure_one()
        all_tickets = self.env['helpdesk.ticket'].search([])
        all_tickets.update_description()

    # Relación para poder poner muchos tags sobre muchos ticket
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
        string='Tags')

    # Relación para poder poner muchos actios sobre un ticket
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')
    
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()