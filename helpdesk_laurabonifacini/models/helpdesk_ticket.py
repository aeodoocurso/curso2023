from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta

class HelpDeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    # Nombre
    name = fields.Char(required=True, help="Título incidencia resumida.")

    # Secuencia
    sequence = fields.Integer(default=10, help='Secuencia')

    # Descripción
    description = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla.",
        default="""Version a la que afecta:
        Módulo:
        Pasos:
            """
    )
    
    @api.model
    def _get_default_date(self):
        return fields.Date.today()

    # Fecha
    date = fields.Date(
        default=_get_default_date,
    )

    # Fecha y hora limite
    date_limit = fields.Datetime( string='Limit Date & Time')

    @api.onchange('date')
    def _onchange_date(self):
        if self.date:
            self.date_limit = self.date + timedelta(days=1)
        else:
            self.date_limit = False    

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
    
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')
    
    action_ids = fields.One2many(
        comodel_name = 'helpdesk.ticket.action',
        inverse_name = 'ticket_id',
        string="Actions",
        )
    
    color = fields.Integer('Color Index', default=0)
    
    amount_time = fields.Float(
        string='Amount of time',
    )

    @api.constrains('amount_time')
    def _amount_time(self):
       for task in self:
           if task.amount_time < 0:
               raise UserError(_("The amount of time can't be negative."))
    
    user_name = fields.Char(
        string='User name',
        )
    
    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],
        )
    
    assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='_inverse_assigned',
        #active=True, # permite archivar/desarchivar
        copy=False, # al duplicar no copiará el contentido de este campo/ los valores o2m por defecto no se copian hay que ponerle el copy=True
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
        return [('user_id', operator, False)]
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user
    
    # hacer un campo calculado que indique, dentro de un ticket, la cantidad de tiquets asociados al mismo ususario.
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

    # crear un campo nombre de etiqueta, y hacer un botón que cree la nueva etiqueta con ese nombre y lo asocie al ticket.
    tag_name = fields.Char()

                      

    def create_tag(self):
        self.ensure_one()
        # self.write({'tag_ids': [(0,0,{'name': self.tag_name})]})
        # self.write({'tag_ids': [Command.create({'name': self.tag_name})]})
        # self.tag_ids = [Command.create({'name': self.tag_name})]
        # action = self.env["ir.actions.actions"]._for_xml_id("helpdesk_laurabonifacini.helpdesk_ticket_tag_action")
        
        action = {
            'name': _('Helpdesk Tickets Tags'),
            'type': 'ir.actions.act_window',
            'res_model': 'helpdesk.ticket.tag',
        }
        action['context'] = {
            'default_name': self.tag_name,
            'default_ticket_id': self.id,

        }
        action['view_mode'] = 'form'
        # action['binding_view_types'] = 'form'
        action['target'] = 'new'
        return action


    def clear_tags(self):
        self.ensure_one()

        # PUNTO DE DEBUG -------
        import pdb; pdb.set_trace()
        a = 10/0

        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        # self.write({'tag_ids': [
        #     (5,0,0),
        #     (6,0,tag_ids.ids)]})
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)] 


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

        




    