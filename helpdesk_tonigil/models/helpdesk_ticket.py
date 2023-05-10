from odoo import fields, models, Command, api, _
from odoo.exceptions import UserError
from datetime import timedelta

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

    # Si la función sólo va a tener una línea, como este caso, se puede poner la línea abajo y no llamar función
    @api.model
    def _get_default_date(self):
        return fields.Date.today()

    # Fecha
    date = fields.Date(
        default=_get_default_date,
    )

    # Fecha y hora limite
    date_limit = fields.Datetime()

    # Añadir un onchange para que al indicar la fecha, ponga como fecha de vencimiento, un día más
    @api.onchange('date')
    def _onchange_date(self):
        for record in self:
            if record.date:
                record.date_limit = record.date + timedelta(days=1)
            else:
                record.date_limit = False
    
    @api.model
    def _get_default_user(self):
        return self.env.user
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
        default=_get_default_user
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
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')

    # Relación para poder poner muchos actions sobre un ticket
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')
    
   
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()

    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(
        string='Amount of time'
    )

    # Añadir una restricción para hacer que el campo time no sea menor que 0
    @api.constrains('amount_time')
    def _check_amount(self):
        for record in self:
            if record.amount_time < 0:
                raise UserError(_("The amount of time can't be negative"))

    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],
    )

    assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='_inverse_assigned',
    )

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool (record.user_id)
    
    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError( ("Operación no soportada"))
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='
        return [('user_id', operator, False)]
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id =self.env.user

    tickets_count = fields.Integer(
        compute='_compute_tickets_count',
        string='Tickets count',
    )

    @api.depends('user_id')
    def _compute_tickets_count(self):
        ticket_obj = self.env['helpdesk.ticket']
        for record in self:
            tickets = ticket_obj.search([('user_id', '=', record.user_id.id)])
            record.tickets_count = len(tickets)

    tag_name = fields.Char()

    def create_tag(self):
        self.ensure_one()
        #self.tag_ids = [Command.create({'name':self.tag_name})]

        action = {
            'name' : "Helpdesk Ticket Tags",
            'type': 'ir.actions.act_window',
            'res_model' : 'helpdesk.ticket.tag',
        }
        action['context'] = {
            'default_name': self.tag_name,
            'default_ticket_ids': self.ids,
        }
        action['view_mode'] = 'form'
        #action['binding_view_types'] = 'form'
        action['target'] = 'form'
        return action
       
    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)
        ]

    def get_related_actions(self):
        self.ensure_one()
        # action = self.env["ir.actions.actions"]._for_xml_id("helpdesk_angelmoya.helpdesk_ticket_action_related_action")
        # return action
        action = self.env["ir.actions.actions"]._for_xml_id("helpdesk_angelmoya.helpdesk_ticket_action_action")
        # <field name="domain">[('ticket_id','=',active_id)]</field>
        action['domain'] = [('ticket_id','=',self.id)]
        # <field name="context">{'default_ticket_id': active_id}</field>
        action['context'] = {'default_ticket_id': self.id}
        return action
    
    def get_assigned(self):
        self.ensure_one()
        self.state = 'assigned'
        self.user_id = self.env.user