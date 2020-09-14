from odoo import api, fields, models


class Prestamo(models.Model):
    _name = 'mymodule.prestamo'
    _rec_name_cliente = 'cliente'

    cliente = fields.Char(string='Nombre del cliente')
    total = fields.Char(string='Monto prestado')
    cliente_id = fields.Many2one('mymodule.cliente', String='Cliente', required=True)

    #cobros_ids = fields.One2many('cobro', 'prestamo_id') ???
    saldo = fields.Float(string="Saldo")
    # estado = fields.Selection([('owe', 'deber'), ('paid', 'pagar')], string='estado')

    # self: Con esta palabra podemos usar las variables de esta clase
    def action_set_cobro(self):
        self.ensure_one()
        view_id = self.env.ref('my_module.my_module_cobro_view_form_wizard').id
        return { #Retornaremos de manera virtual los siguientes campos, solo para que los visualize el
                 #usuario, pero no se guardan en bases de datos
            'name': 'Registro de un cobro',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mymodule.cobro',  # Hacemos referencia a este modelo
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': {
                'default_prestamo_id': self.id,
            }
        }

    # ???
    @api.onchange('total')
    def _onchange_total(self):
        return{
            'value': {
                'saldo': self.total
            }
        }

    # ???
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
