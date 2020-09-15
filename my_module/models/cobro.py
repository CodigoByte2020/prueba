from odoo import api, fields, models
from odoo.exceptions import UserError


class Cobro(models.Model):

    _name = 'mymodule.cobro'
    _description = 'Tabla de cobros'

    name = fields.Char(string='Serie del cobro', default='/')
    nombre_cliente = fields.Char(string='Nombre del cliente', compute='_compute_nombre_cliente')
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)
    importe = fields.Float(string='Importe', required=True)
    prestamo_id = fields.Many2one('mymodule.prestamo', string='Prestamo ID', required=True)

    @api.depends('prestamo_id')
    def _compute_nombre_cliente(self):
        self.nombre_cliente = '{} {}'.format(self.prestamo_id.cliente_id.name, self.prestamo_id.cliente_id.apellido)

    @api.model
    def create(self, values):
        values['name'] = self.env['ir.sequence'].next_by_code('comprobantecobro.cliente', sequence_date=None) or '/'
        pres_id = self.env['mymodule.prestamo'].browse([values.get('prestamo_id')])
        if values.get('importe') > pres_id.saldo:
            raise UserError('No puede pagar más que el saldo')
        pres_id.saldo = pres_id.saldo - values.get('importe')
        if pres_id.saldo == 0:
            pres_id.estado = 'paid'
        return super(Cobro, self).create(values)

    def action_guardar(self):
        self.ensure_one()
        return True

