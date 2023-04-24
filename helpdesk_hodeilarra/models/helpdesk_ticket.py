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
    assigned            = fields.Boolean()

    #Acciones a realizar
    actions_todo        = fields.Html()


