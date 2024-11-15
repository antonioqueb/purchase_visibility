from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    additional_visible_users = fields.Many2many(
        'res.users', 
        string="Usuarios Adicionales con Visibilidad"
    )
