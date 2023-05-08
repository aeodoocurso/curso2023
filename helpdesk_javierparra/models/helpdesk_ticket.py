from odoo import  fields, models, api, Command
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    #Nombre
    name = fields.Char(
        required=True,
        help="Resume en pocas palabras un título para la incidencia",
        index=True
    )
    #Descripcion
    description = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla.",
        default="""Version a la que afecta:
    Modulo:
    Pasos para replicar:
    Modulos personalizados:
        """
    )
    #Fecha
    date = fields.Date()    
    #Fecha y hora limite
    date_limit = fields.Datetime(
        string='Limi Date & Time')    
    
    #Acciones a realizar (Html)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assidned to')
    
    # Añadir el campo Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('in_process', 'In Process'),
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ],
        default='new',
    )

    #Añádir campo sequence y hacer el widget handle.
    sequence = fields.Integer(
        default=10,
        help="Secuencia para el orden de las incidencias",
    )


    actions_todo = fields.Html()

    color = fields.Integer('Color Index', default=0)

    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],)

    amount_time = fields.Float(string='Amount of time')

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')


    #funcion que añada una accion
    #def add_action(self):
    #    self.ensure_one()
    #    self.write{
    #        'action_ids':(0 , 0, {'name': 'Nueva acción'})
    #    }


    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        #relation='helpdesk_ticket_action_rel',
        #column1='ticket_id',
        #column2='action_id',
        inverse_name='ticket_id',
        string='Actions')

    
    def update_description(self):
        #self.write({'description': "Nueva descripcion"})
        for ticket in self:
            ticket.description = "Nueva descripcion"
        

    def update_all_descriptions(self):
        all_tickets = self.env['helpdesk.ticket'].search([])
        all_tickets.update_description()    

    def set_all_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()

    
    #Asignado (Verdadero o Falso) solo lectura
    assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='inverse_assigned',
    )

    #Hacer que el campo assigned sea calculado 
    @api.depends('user_id')
    def _compute_assigned(self):
        for ticket in self:
            ticket.assigned = bool(ticket.user_id)

    #hacer que se pueda buscar con el atributo search
    def _search_assigned(self, operator, value):
        if operator == '=' and value == True:
            raise UserError('No se puede buscar por asignado')
        if operator == '==' and value == True:
            operator = '!='
        else:
            operator = '=',
        return [('user_id', operator, False)]



    def inverse_assigned(self):
        for ticket in self:
            if not ticket.assigned:
                ticket.user_id = False
            else:
                ticket.user_id = self.env.user

    tag_name = fields.Char(Readonly = True)


    #hacer un campo calculado que indique, dentro de un ticket, la cantidad de tiquets asociados al mismo ususario.
    ticket_count = fields.Integer(
        compute='_compute_ticket_count',
    )

    def _compute_ticket_count(self):
        tickek_obj = self.env['helpdesk.ticket']
        for ticket in self:
            tickets = ticket.search([('user_id', '=', ticket.user_id.id)])
            ticket.ticket_count = len(tickets)

#    #crear un campo nombre de etiqueta, y hacer un botón que cree la nueva etiqueta con ese nombre y lo asocie al ticket.
    def create_tag(self):
        self.ensure_one()
        self.write({'tag_ids': [(0, 0, {'name': self.tag_name})]})


    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        #import pdb; pdb.set_trace()
        #import wdb; wdb.set_trace()
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)
        ]



