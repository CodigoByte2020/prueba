from odoo import api, fields, models
from odoo.exceptions import UserError

STATE_SELECTION = [
    ('bloc', 'consultar'),
    ('owe', 'deber'),
    ('paid', 'pagar')
]
class Prestamo(models.Model):
    _name = 'mymodule.prestamo'
    description = "Tabla de prestamos"

    name = fields.Char(string='Serie Corelativo', default='/', readonly=True)
    total = fields.Char(string='Monto prestado')
    cliente_id = fields.Many2one('mymodule.cliente', String='Cliente', required=True)
    cobros_ids = fields.One2many('mymodule.cobro', 'prestamo_id', String='Cobros')
    saldo = fields.Float(string="Saldo")
    estado = fields.Selection([], string='estado')

    def action_set_cobro(self):
        self.ensure_one()
        view_id = self.env.ref('my_module.my_module_cobro_view_form_wizard').id
        return { #Retornaremos de manera virtual los siguientes campos, solo para que los visualize el
                 #usuario, pero no se guardan en bases de datos
            'name': 'Registro de un cobro',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mymodule.cliente',
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': {
                'default_prestamo_id': self.id,
            }
        }

    @api.model
    def create(self, values):
        if values.get('name', '/') == '/':
            values['name'] = self.env['ir.sequence'].next_by_code('comprobanteprestamo.cliente', sequence_date=None) or '/'
        values['estado'] = 'owe'
        if values['monto_prestado'] == 0:
            raise UserError('El monto debe ser mayor a cero.')

        return super(Prestamo, self).create(values)

    @api.onchange('total')
    def _onchange_total(self):
        return{
            'value': {
                'saldo': self.total
            }
        }

    @api.onchange('cobros_ids')
    def _onchange_cobros_ids(self):
        suma_pagos = 0
        for cobro in self.cobros_ids:
            suma_pagos += cobro.importe
        return {
            'values': {
                'saldo': self.total - suma_pagos
            }
        }
