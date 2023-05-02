from odoo import fields, models
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

	color = fields.Integer('Color Index', default=0)

	def set_actions_as_done(self):
		self.ensure_one()
		self.action_ids.set_done()

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
