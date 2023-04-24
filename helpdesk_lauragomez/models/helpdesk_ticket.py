from odoo import fields, models


#models.Model es parte del ORM
class HelpdeskTicket(models.Model): 
    _name = "helpdesk.ticket"
    #si no se pone description (warning)
    _description = "Helpdesk ticket"
    
    # Nombre 
    name = fields.Char(
        required = True     
    )
    
    # Descrición
    description = fields.Text(
        help= "Escribe detallamente la incidencia",
        default="""Versión a la que afecta:
    Módulo:
    Pasos para replicar:
    Módulos personalizados:
    """
    )
    
    # Fecha
    date = fields.Date()
    
    # Fecha y hora límite
    date_limit = fields.Datetime(
        string='Limit Date & Time'
    )
    
    # Asignado (Verdadero o falso)
    field_name = fields.Boolean()
    
    # Acciones a realizar (Html)
    actions_todo = fields.Html(
        string='field_name',
    )
    
    
    