# Copyright <2023> Laura bonifacini - laura.bonifacini@gmail.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Laura Bonifacini",
    "summary": "Module Nº1",
    "version": "16.0.1.0.0",
    "development_status": "Alpha|Beta|Production/Stable|Mature",
    "category": "Helpdesk",
    "website": "https://Laura-Bonifacini",
    "author": "Laura Bonifacini, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_action_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_tag_views.xml",
    ],
}