from oddo import fields, models


class Cliente(models.Model):
    _name = 'mymodule.cliente'
    _description = "Tabla para los clientes"

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellidos', required=True)
    celular = fields.Char(string='Celular')
    direccion = fields.Char(string='Direccion')
