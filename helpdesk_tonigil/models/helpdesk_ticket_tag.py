from odoo import fields, models, api

class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.tag"
    _description = "Helpdesk Ticket Tag"

    # Nombre
    name = fields.Char(
        required=True
    )

    # Relación para poder poner muchos tags sobre muchos ticket
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')
    
    # Función para eliminar las tags que no estén asignadas a ningún ticket - Se utiliza en el cron
    @api.model
    def _clean_tags_cron(self):
        tags = self.search([('ticket_ids', '=', False)])
        tags._clean_tags()

    def _clean_tags(self):
        self.unlink()