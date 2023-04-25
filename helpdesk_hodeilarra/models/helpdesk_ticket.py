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
    
    #secuencia
    sequence = fields.Integer(default=10, help="Secuencia para el orden")


