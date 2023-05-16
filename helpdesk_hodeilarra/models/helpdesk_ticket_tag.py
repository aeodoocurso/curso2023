from odoo import fields, models

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Helpdesk Ticket Tag'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)

    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')

    
    def remove_unused_tags(self):
        tags = self.search([('ticket_ids', '=', False)])
        tags.unlink()

    