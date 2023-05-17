from odoo.tests import common

from odoo import fields
from odoo.exceptions import UserError

class TestHelpdesk(common.TransactionCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.ticket = self.env['helpdesk.ticket'].create({
            'name': 'Test ticket',
            'description': 'Test description',
        })
        self.user_admin = self.env.ref('base.user_admin')
    
    def test_ticket_amount_time_no_negative(self):
        self.ticket.amount_time = 3
        self.assertEqual(self.ticket.amount_time, 3.0)
        with self.assertRaises(UserError):
            self.ticket.amount_time = -1
    
    def test_ticket_assigned(self):
        self.assertFalse(self.ticket.assigned)
        self.ticket.user_id = self.user_admin
        self.assertTrue(self.ticket.assigned)
        self.ticket.user_id = False
        self.assertFalse(self.ticket.assigned)
        self.ticket.user_id = self.user_admin
        self.assertTrue(self.ticket.assigned)
    
    def test_ticket_search_assigned(self):
        self.assertIn(self.ticket, self.env['helpdesk.ticket'].search([('assigned', '=', False)]))
        self.assertIn(self.ticket, self.env['helpdesk.ticket'].search([('assigned', '!=', True)]))
        self.ticket.user_id = self.user_admin
        self.assertIn(self.ticket, self.env['helpdesk.ticket'].search([('assigned', '=', True)]))
        self.assertIn(self.ticket, self.env['helpdesk.ticket'].search([('assigned', '!=', False)]))
        with self.assertRaises(UserError):
            self.env['helpdesk.ticket'].search([('assigned', '>', True)])