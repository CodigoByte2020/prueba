from odoo import api, fields, models
from odoo.exceptions import UserError

STATE_SELECTION = [
    ('draft', 'borrador'),
    ('owe', 'debiendo'),
    ('paid', 'pagado')
]

class Prestamo(models.Model):
    _name = 'mymodule.prestamo'
    description = "Tabla de prestamos"

    name = fields.Char(string='Serie Corelativo', default='/', readonly=True)
    monto_prestado = fields.Float(string='Monto prestado', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)
    cliente_id = fields.Many2one('mymodule.cliente', String='Cliente', required=True)
    cobros_ids = fields.One2many('mymodule.cobro', 'prestamo_id', String='Cobros')
    saldo = fields.Float(string="Saldo", readonly=True)
    estado = fields.Selection(STATE_SELECTION, string='estado', default='draft')

    def action_set_cobro(self):
        self.ensure_one()
        view_id = self.env.ref('my_module.mymodule_cobro_view_form_wizard').id
        return { #Retornaremos los valore de los siguientes campos, solo para que los visualize el
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
                'default_importe': self.saldo
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

    @api.onchange('monto_prestado')
    def _onchange_monto_prestado(self):
        return{
            'value': {
                'saldo': self.monto_prestado
            }
        }

    #@api.onchange('cobros_ids')
    # def _onchange_cobros_ids(self):
    #     suma_pagos = 0
    #     for cobro in self.cobros_ids:
    #         suma_pagos += cobro.importe
    #     return {
    #         'values': {
    #             'saldo': self.monto_prestado - suma_pagos
    #         }
    #     }
