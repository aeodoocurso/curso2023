# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk JALP",
    "summary": "Gestión de incidencias",
    "version": "16.0.1.0.0",
    "category": "HelpDesk",
    "author": "José Ángel Lois. Odoo Community Association (OCA)",
    "maintainers": ["joseangellois"],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml"
    ]
}