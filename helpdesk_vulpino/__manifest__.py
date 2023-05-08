{
    "name": "Helpdesk Vulpino",
    "summary": "Un gestor de tickets to wapo",
    "version": "16.0.0.1",
    "category": "Helpdesk",
    "licence": "AGPL-3",
    "website": "odoo.com",
    "author": "Vulpino",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    'data': [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk.xml",
        "views/helpdesk_menu.xml",
        "views/helpdesk_tags.xml"
    ],
}
