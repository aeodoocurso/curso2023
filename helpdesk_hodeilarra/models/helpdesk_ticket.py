from odoo import fields, models

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

    #Asignado
    assigned            = fields.Boolean(readonly=True)

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
    


