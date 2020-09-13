from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    #_name = 'purchase.order'

    plazo_extra_pedido = fields.Char(string="Plazo extra de pedido")
    sede_pedido = fields.Char(string="Sede de pedido")
    pedidohistorico_ids = fields.One2many('modulocompras.pedidohistorico', 'pedido_id', string='Vendedor')

    def action_set_infracciones(self):
        # self se asegurara que por le menos llegue algun elemento
        self.ensure_one()
        view_id = self.env.ref('modulo_compras.modulocompras_pedidohistorico_view_form_wizard').id
        return {
            'name': 'Listar pedidos',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            're_model': 'modulocompras.pedidohistorico',
            'view_id': view_id,
            'views': [('view_id', 'form')],
            'target': 'new',
            'context': {
                'default_modulocompras.pedidohistorico_id': self.id
            }
        }

