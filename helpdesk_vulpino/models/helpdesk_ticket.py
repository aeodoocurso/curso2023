from odoo import models, api, _, fields


class HelpdeskTicket(models.Model):
    _name="helpdesk.ticket"
    _description="Helpdesk Ticket"

    name = fields.Char(
        required=True)
    user_id = fields.Many2one("res.users")
    stage = fields.Selection([
        ('new', 'New'),
        ('asigned', 'Assigned'),
        ('process', 'In process'),
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('cancel', 'Canceled')
    ],
    default="new")
    description = fields.Text(
        string="Description",
        default="")
    date = fields.Date()
    sequence = fields.Integer(default=10)
    limit_datetime = fields.Datetime(
        string="Date & Time limit",
        help="Limit date")
    assign = fields.Boolean(
        string="Is assign",
        readonly=True)
    actions_todo = fields.Html(
        string="Actions to realize")