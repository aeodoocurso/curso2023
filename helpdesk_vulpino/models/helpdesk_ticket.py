from odoo import models, api, _, fields, Command


class HelpdeskTicket(models.Model):
    _name="helpdesk.ticket"
    _description="Helpdesk Ticket"

    name = fields.Char(
        required=True)
    user_id = fields.Many2one("res.users")
    stage = fields.Selection([
        ('new', 'New'),
        ('asigned', 'Assigned'),
        ('process', 'In process'),
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('cancel', 'Canceled')
    ],
    default="new")
    description = fields.Text(
        string="Description",
        default="")
    date = fields.Date()
    sequence = fields.Integer(default=10)
    limit_datetime = fields.Datetime(
        string="Date & Time limit",
        help="Limit date")
    
    assign = fields.Boolean(
        string="Is assign",
        readonly=True)
    
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        string='Tags')
    
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')

    
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()
    
    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(
        string='Amount of time')
    
    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],)
    actions_todo = fields.Html(
        string="Actions to realize")
    color = fields.Integer('Color', default=0)

    assigned = fields.Boolean(
        compute='_compute_assigned',
        search='_search_assigned',
        inverse='_inverse_assigned',
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
        self.tag_ids = [Command.create({'name': self.tag_name})]

    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        # self.write({'tag_ids': [
        #     (5,0,0),
        #     (6,0,tag_ids.ids)]})
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)]