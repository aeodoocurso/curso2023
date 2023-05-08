from odoo import api, Command, fields, models
from odoo.exceptions import UserError

# from datetime import datetime

class HelpdeskTicket(models.Model):
	_name = "helpdesk.ticket"
	_description = "Helpdesk Ticket"

	name = fields.Char(
		required=True,
		help="Resume de la incidencia en una frase"
	)

	sequence = fields.Integer(
		# default=0,
		help='Secuencia/sucesión para el orden de las incidencias'
	)

	description = fields.Html(
		help="Descripción detallada de la incidencia",
		# default="""
		# Lorem ipsum dolor sit amet
		# """
	)
	date = fields.Date()

	date_limit = fields.Datetime(string="Limit date & time")
	
	assigned = fields.Boolean(
		readonly = True
	)

	user_id = fields.Many2one(
		comodel_name = 'res.users',
		string = 'Asigned to'
	)

	actions_todo = fields.Html()

	state = fields.Selection(
		selection=[
			('new', 'New'),
			('assigned', 'Assigned'),
			('in_process', 'In process'),
			('pending', 'Pending'),
            ('canceled', 'Canceled'),
            ('resolved', 'Resolved'),
		],
		default='new',
	)

	tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
        string='Tags'
	)
    
	action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions',
	)
		
	def set_actions_as_done(self):
		self.ensure_one()
		self.action_ids.set_done()

	color = fields.Integer('Color Index', default=0)

	amount_time = fields.Float(
		string='Amount of time')
    
	person_id = fields.Many2one(
		comodel_name='res.partner',
		domain=[('is_company', '=', False)],)

    # Hacer que el campo assigned sea calculado,
    # hacer que se pueda buscar con el atributo search y  
    # hacer que se pueda modificar de forma que si lo marco se actualice el usuario con el usuario conectado y
    # si lo desmarco se limpie el campo del usuario.

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
		self.tag_ids = [Command.create({'name': self.tag_name})]

	# import pdb; pdb.set_trace()

	def clear_tags(self):
		self.ensure_one()
		tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'zzz')])
		# self.write({'tag_ids': [
		#     (5,0,0),
		#     (6,0,tag_ids.ids)]})
		self.tag_ids = [
			Command.clear(),
			Command.set(tag_ids.ids)]


	# def update_field(self, field, value):
	def update_field(self):
		...
		# self.write({'name': datetime.now()})

		# self.ensure_one()
		# for record in self:
		# 	self.name = '****OK*****'
		# self.write({'name': pytz.timezone("Europe/Madrid").localize()})
	
	# def update_all_records(self):
	# 	self.ensure_one()
	# 	all_tickets = self.env['helpdesk.ticket'].search([])
	# 	all_tickets.update_field(new_value='')

	# @api.depends('user_id')
	# def _computed_assigned(self):
	# 	for record in self:
	# 		record.assigned = bool(record.user_id)
	
	# def _search_asssigned(self, operator, value):
	# 	...

	# user_name = fields.Char(
	# 	related='user_id.name',
	# 	string = 'User name'
	# )