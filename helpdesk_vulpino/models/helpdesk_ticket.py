from odoo import models, api, _, fields


class HelpdeskTicket(models.Model):
    _name="helpdesk.ticket"
    _description="Helpdesk Ticket"

    name = fields.Char(
        required=True)
    description = fields.Text(
        string="Description",
        default="""
        Afecta el salt de linia?

        Aviam si funciona
        """)
    date = fields.Date()
    limit_datetime = fields.Datetime(
        string="Date & Time limit")
    assign = fields.Boolean(
        string="Is assign")
    actions_todo = fields.Html(
        string="Actions to realize")

    
