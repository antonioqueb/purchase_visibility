from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    additional_visible_users = fields.Many2many(
        'res.users',
        'res_users_additional_visibility_rel',  # Nombre de la tabla intermedia
        'user_id',  # Columna que apunta al registro actual (origen)
        'visible_user_id',  # Columna que apunta al usuario adicional (destino)
        string="Usuarios adicionales para visibilidad",
        help="Define qué usuarios adicionales pueden ver los documentos creados por este usuario."
    )
