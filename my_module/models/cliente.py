from odoo import fields, models


class Cliente(models.Model):
    _name = 'mymodule.cliente'
    _description = "Tabla para los clientes"

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Char(string='Dirección')
