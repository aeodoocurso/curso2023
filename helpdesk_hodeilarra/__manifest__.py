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
        "base",
    ],
    "excludes": [
        "module_name",
    ],
    "data": [
       "security/helpdesk_security.xml",
       "security/ir.model.access.csv",
       "views/helpdesk_ticket_views.xml"
       
    ],
  
}