# Copyright <2023> Laura bonifacini - laura.bonifacini@gmail.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Helpdesk María Laura Bonifacini",
    "summary": "Gestiona incidencias en pedidos de venta",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://Laura-Bonifacini",
    "author": "Laura Bonifacini, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_management",
        "helpdesk_laurabonifacini"
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/product_template_views.xml",
    ],
}