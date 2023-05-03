from odoo import api, fields, models, _, Command
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'

    name = fields.Char(
        required=True,
        help='Nombre de la incidencia'
    )
    sequence = fields.Char(
        string='Sequence',
        copy=False,
    )

    description = fields.Text(
        default="""
            Version a la que afecta:
            Modulo:
            Pasos para replicar:
            Modulos personalizados:
        """,
    )
    date = fields.Date()
    date_limit = fields.Datetime(
        string='Limit Date & Time',
    )
    assigned = fields.Boolean(
        string='Assigned to',
        readonly=True, 
    )
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Usuario',
    )
    
    actions_todo = fields.Html()

    state = fields.Selection(
        string='State',
        selection=[
            ('new',      'New'), 
            ('assigned', 'Assigned'),
            ('pending',  'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ], 
        default='new'
    )

    def get_random_string(self, length):
        import random
        import string
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def update_description(self):
        for record in self:
            record.description = self.get_random_string(12)
        return True

    def update_all_descriptions(self):
        self.ensure_one()
        all_tickets = self.env['helpdesk.ticket'].search([])
        all_tickets.update_description()

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags'
    )

    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions'
    )

    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()

    color = fields.Integer('Color Index', default=0)
    amount_time = fields.Float()

    is_assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='_inverse_assigned',
    )

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.is_assigned = bool(record.user_id)

    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError('Invalid domain')
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='
        return [('user_id', operator, False)]

    def _inverse_assigned(self):
        for record in self:
            if not record.is_assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    # campo calculado que indique la cantidad de tickets asociados al usuario
    @api.depends('user_id')
    def _compute_ticket_count(self):
        ticket_obj = self.env['helpdesk.ticket']
        for record in self:
            tickets = ticket_obj.search([
                ('user_id', '=', record.user_id.id)
            ])
            record.tickets_count = len(tickets)

    tickets_count = fields.Integer(
        compute='_compute_ticket_count',
        string='Tickets count'
    )

    tag_name = fields.Char()

    def create_tag(self):
        self.ensure_one()
        self.tag_ids = [Command.create({'name': self.tag_name})]

    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)
        ]
        
        # self.env['helpdesk.ticket.tag'].search([]).unlink()