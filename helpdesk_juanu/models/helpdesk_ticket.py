# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, Command
from odoo.exceptions import UserError, ValidationError

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk ticket'

    name = fields.Char(
        required=True,
        help="Resumen de la incidencia.",
    )

    sequence = fields.Integer(
        default=10,
        help="Secuencia para el orden de incendencias",
    )

    description = fields.Text(
        help="Describe detalladamente de la incidencia.",
        default=""""Version a la que afecta:Modulo:Version:""",
    )

    date = fields.Date(
        default=lambda self: fields.datetime.now()
    )

    date_limit = fields.Datetime(
        string="Date & Time limit",
    )

    assigned = fields.Boolean(
        compute="_compute_assigned",
        inverse="_inverse_assigned",
        search="_search_assigned",
    )

    user_id = fields.Many2one(
        string="Assigned to",
        comodel_name="res.users"
    )

    actions_todo = fields.Html(
    )

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

    action_ids = fields.One2many(
        string="Actions",
        comodel_name="helpdesk.ticket.action",
        inverse_name="ticket_id",
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
        string='Tags')

    color = fields.Integer(
        string="Color",
        default=0,
    )

    amount_time = fields.Float(
        string="Amount time",
    )

    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],
    )

    tickets_count = fields.Integer(
        compute='_compute_tickets_count',
        string='Tickets count',
    )

    tag_name = fields.Char(
    )

    @api.depends('user_id')
    def _compute_tickets_count(self):
        ticket_obj = self.env['helpdesk.ticket']
        for record in self:
            tickets = ticket_obj.search([('user_id', '=', record.user_id.id)])
            record.tickets_count = len(tickets)

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def update_description(self):
        for record in self:
            record.description = "OK"

    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError(_("Operation not supported"))
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='
        return [('user_id', operator, False)]

    def create_tag(self):
        self.ensure_one()
        # self.write({'tag_ids': [(0,0,{'name': self.tag_name})]})
        # self.write({'tag_ids': [Command.create({'name': self.tag_name})]})
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