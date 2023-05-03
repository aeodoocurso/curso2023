from odoo import fields, models, api
from odoo.exceptions import UserError

class Helpdesk(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    #nombre
    nombre              = fields.Char(required=True)

    #descripcion
    description         = fields.Text(help="Describe detalladamente la incidencia y cómo replicarla.",default="Esto es un campo por defecto.")

    #fecha
    date                = fields.Date()
    
    #fecha y hora limite
    date_limit          = fields.Datetime(string="Limit Date & Time")

    

    user_id             = fields.Many2one(comodel_name='res.users', string='Assigned to')

    #Acciones a realizar
    actions_todo        = fields.Html()

    #estado
    state = fields.Selection(
        selection=[
            ('new', 'Nuevo'),
            ('assigned', 'Asignado'),
            ('in_process', 'En proceso'),
            ('pending', 'Pendiente'),
            ('resolved', 'Resuelto'),
            ('canceled', 'Cancelado')],
            string='Estado', default='new',
            )

    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(string="Amount of time")
    
    #secuencia
    sequence = fields.Integer(default=10, help="Secuencia para el orden")

    def update_description(self):
        self.write({'description':"Esto es una descripción de prueba"})
       

    def update_other_description(self):
        self.ensure_one()
        all_tickets = self.env['helpdesk.ticket'].search([])
        all_tickets.update_description()

    


    tag_ids = fields.Many2many(comodel_name='helpdesk.ticket.tag',string='Tags')
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')

    
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()

    
    #Asignado
    assigned  = fields.Boolean(compute="_compute_assigned", search='_search_assigned', inverse='_inverse_assigned')

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _search_assigned(self, operator, value):
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
                record.user_id = self.env.user

    user_name = fields.Char(related='user_id.name', string='User name', readonly=True)

    ticket_count = fields.Integer(
        compute='_compute_tickets_count',
        string='Tickets count'
    )

    @api.depends('user_id')
    def _compute_tickets_count(self):
        ticket_obj = self.env['helpdesk.ticket']
        for record in self:
            tickets = ticket_obj.search([('user_id','=', record.user_id.id)])
            record.ticket_count = len(tickets)

    tag_name = fields.Char()

    def create_tag(self):
        self.ensure_one()
        self.write({
                'tag_ids': [(0,0,{'nombre':self.tag_name})]
            })

    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('nombre','=','otra')])
        self.write({'tag_ids':[
            (5,0,0),
            (6,0,tag_ids.ids)
        ]
        })

