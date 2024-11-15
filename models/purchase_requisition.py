from odoo import models, fields

class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    additional_visible_users = fields.Many2many(
        'res.users', 
        string="Usuarios Adicionales con Visibilidad"
    )
