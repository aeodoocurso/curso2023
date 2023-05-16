# Copyright <2023> <Hodei Larrañaga>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Hodei Larrañaga",
    "summary": "Gestiona incidencias",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/Hodeilarra/curso2023",
    "author": "Hodei Larrañaga",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "mail",
    ],
    "excludes": [
        "module_name",
    ],
    "data": [
       "security/helpdesk_security.xml",
       "security/ir.model.access.csv",
       "views/helpdesk_ticket_views.xml",
       
        "views/helpdesk_cron.xml",
        "views/helpdesk_ticket_tag_views.xml",
        "wizards/helpdesk_create_ticket_views.xml",
        "report/ir_actions_report_templates.xml",
        "report/ir_actions_report.xml",
        
       
    ],
  
}