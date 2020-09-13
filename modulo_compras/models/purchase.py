from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # _name = 'purchase.order'

    plazo_extra_pedido = fields.Char(string="Plazo extra de pedido")
    sede_pedido = fields.Char(string="Sede de pedido")
    # De un pedidohistorico_ids voy a consultar un pedido_id
    pedidohistorico_ids = fields.One2many('modulocompras.pedidohistorico', 'pedido_id', string='Vendedor')

    # self contiene todos los atributos de la clase
    def action_set_pedidoshistoricos(self):
        # ensure_one se asegura que por le menos llegue algun elemento
        self.ensure_one()
        view_id = self.env.ref('modulo_compras.modulocompras_pedidohistorico_view_form_wizard').id
        return {
            'name': 'Listar pedidos',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'modulocompras.pedidohistorico',
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': {
                'default_pedido_id': self.id,
            }
        }
