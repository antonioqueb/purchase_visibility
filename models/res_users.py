from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    additional_visible_users = fields.Many2many(
        'res.users',
        string="Usuarios adicionales para visibilidad",
        help="Define qué usuarios adicionales pueden ver los documentos creados por este usuario."
    )
