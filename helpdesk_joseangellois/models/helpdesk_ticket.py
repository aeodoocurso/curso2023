from odoo import fields, models
from datetime import datetime

class HelpdeskTicket(models.Model):
	_name = "helpdesk.ticket"
	_description = "Helpdesk Ticket"

	name = fields.Char(
		required=True,
		help="Breve frase que resume la incidencia"
	)

	sequence = fields.Integer(
		default=10,
		help='Secuencia para el orden de las incidencia'
	)

	description = fields.Html(
		help="Descripción detallada de la incidencia",
		default="""
		Lorem ipsum dolor sit amet
		"""
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
		],
		default='new',
	)

	# def update_field(self, field, value):
	def update_field(self):
		# self.ensure_one()
		# for record in self:
		# 	self.name = '****OK*****'
		# self.write({'name': pytz.timezone("Europe/Madrid").localize()})
		self.write({'name': datetime.now()})
	
	# def update_all_records(self):
	# 	self.ensure_one()
	# 	all_tickets = self.env['helpdesk.ticket'].search([])
	# 	all_tickets.update_field(new_value='')
