from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HelpDeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    # Nombre
    name = fields.Char(required=True, help="Título incidencia resumida.")

    # Secuencia
    sequence = fields.Integer(default=10, help='Secuencia para')

    # Descripción
    description = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla.",
        default="""Version a la que afecta:
        Módulo:
        Pasos:
            """
    )

    # Fecha
    date = fields.Date()

    # Fecha y hora limite
    date_limit = fields.Datetime( string='Limit Date & Time')

    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='_inverse_assigned',
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

    tag_ids = fields.Many2many(
        comodel_name = 'helpdesk.ticket.tag',
        string = "Tag",
        )

    action_ids = fields.One2many(
        comodel_name = 'helpdesk.ticket.action',
        inverse_name = 'ticket_id',
        string="Actions",
        )
    
    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(
        string='Amount of time',
    )

    user_name = fields.Char(
        related='user_id.name',
        string='User name',
        )

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError(_("Operation not supported"))
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='    
        return [('user_id', operator, value)]    
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user    

    def update_description(self):
        self.write({'name': "OK"})

    def update_all_description(self):
        self.ensure_one()
        all_tickets = self.env['helpdesk.ticket'].search([])
        all_tickets.update_description()

    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()  

    def set_actions_as_todo(self):
        self.ensure_one()
        self.action_ids.set_todo()           


    