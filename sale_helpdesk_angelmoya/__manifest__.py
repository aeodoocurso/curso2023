# Copyright <2023> Angel Moya - angel.moya@pesol.es
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Helpdesk Angel Moya",
    "summary": "Gestiona incidencias en pedidos de venta",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://aeodoo.org",
    "author": "aeodoo, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_management",
        "helpdesk_angelmoya"
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/product_template_views.xml",
    ],
}