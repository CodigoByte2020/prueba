from odoo import fields, models


class Usuario(models.Model):
    _inherit = 'res.users'

    sede_ids = fields.Many2many(
        'loanmanager.sede',
        'res_users_loanmanager_sede_rel',
        'user_id', 'sede_id',
        String='Sedes'
    )