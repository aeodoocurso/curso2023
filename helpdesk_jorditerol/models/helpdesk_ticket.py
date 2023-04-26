from odoo import fields, models

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
        string='Assigned to',
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