from odoo import models, fields, _

class HelpdeskCreateTicket(models.TransientModel):
    _name = 'helpdesk.create.ticket'
    _description = 'Create Ticket'

    state = fields.Selection(
        [('steep_1', 'Steep 1'), ('steep_2', 'Steep 2')],
        string='State',
        default='steep_1',
    )

    tag_id = fields.Many2one(
        'helpdesk.ticket.tag',
        string='Tag',
        required=True,
        default=lambda self: self.env.context.get('active_id')
    )

    name = fields.Char(string='Subject', required=True)
    description = fields.Text(string='Description', required=True)

    ticket_id = fields.Many2one(
        'helpdesk.ticket',
        string='Ticket',)

    def create_ticket(self):
        ticket = self.env['helpdesk.ticket'].create({
            'name': self.name,
            'description': self.description,
            'tag_ids': [(4, self.tag_id.id)],
        })

        self.ticket_id = ticket.id
        self.state = 'steep_2'

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'helpdesk.create.ticket',
            'view_mode': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }

    def view_ticket(self):
        return {
            'name': _('Ticket'),
            'view_mode': 'form',
            'res_model': 'helpdesk.ticket',
            'res_id': self.ticket_id.id,
            'type': 'ir.actions.act_window',
        }    