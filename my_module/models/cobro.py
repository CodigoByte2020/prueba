from odoo import fields, models

class Cobro(models.Model):

    _name = 'cobro'
    _description = 'Tabla de cobros'

    fecha = fields.Date(string='Fecha')
    importe = fields.Float(string='Importe')
    prestamo_id = fields.Many2one(
        'my_module.cobro',
        string='Prestamo ID',
        required=True)

