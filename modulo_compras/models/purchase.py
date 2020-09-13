from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _name = 'purchase.order'

    plazo_extra_pedido = fields.Char(string="Plazo extra de pedido")
    sede_pedido = fields.Char(string="Sede de pedido")
    pedidohistorico_ids = fields.One2many('modulocompras.pedidohistorico', 'id', string='Vendedor')