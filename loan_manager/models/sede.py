from odoo import fields, models


class Sede(models.Model):
    _name = 'loanmanager.sede'

    name = fields.Char(string='Sedes')
    user_ids = fields.Many2many(
        'res_users',
        'res_users_loanmanager_sede_rel',
        'sede_id', 'user_id',
        String='Usuarios'
    )
