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
        "mail"
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_menu_views.xml",
        "wizards/helpdesk_create_ticket_views.xml",
        "views/helpdesk_ticket_action_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_tag_views.xml",
        "data/helpdesk_cron.xml",
        "report/ir_actions_report_templates.xml",
        "report/ir_actions_report.xml",
    ],
}