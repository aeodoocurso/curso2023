# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Jordi Terol",
    "summary": "Gestion de incidencias",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/jterolc/curso2023",
    "author": "Jordi Terol, Odoo Community Association (OCA)",
    "maintainers": ["jterolc"],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        # "templates/assets.xml",
        # "views/report_name.xml",
        # "views/res_partner_view.xml",
        # "wizards/wizard_model_view.xml",
    ],
}