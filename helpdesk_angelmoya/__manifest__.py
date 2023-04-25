# Copyright <2023> Angel Moya - angel.moya@pesol.es
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Angel Moya",
    "summary": "Gestiona incidencias blablabla",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://aeodoo.org",
    "author": "aeodoo, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base"
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml"
    ],
}