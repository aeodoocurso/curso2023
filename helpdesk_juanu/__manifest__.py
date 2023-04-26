# -*- coding: utf-8 -*-
{
    'name': "Helpdesk juanu",
    'summary': """Helpdesk model example for curse 2023""",
    'description': """Helpdesk model example for curse 2023""",
    'author': "JuanuSt",
    'website': "https://moval.es",
    'category': 'Helpdesk',
    'version': '16.0.0.1',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/security_helpdesk.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_actions_views.xml',
        'views/helpdesk_ticket_tag_views.xml',
    ],
}
