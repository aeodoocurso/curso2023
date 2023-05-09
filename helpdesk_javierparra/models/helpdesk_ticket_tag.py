from odoo import  fields, models, api

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Helpdesk Ticket Tag'


    #nombre
    name = fields.Char(
        required=True,
    )


    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')
    
    @api.model
    def _clean_unused_tags_cron(self):
        all_tags = self.env['helpdesk.ticket.tag'].search([])
        for tag in all_tags:
            if not tag.ticket_ids:
                tag.unlink()