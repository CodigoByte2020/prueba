from odoo import fields, models


class PedidoHistorico(models.Model):
    _inherit = 'purchase.order'
    _name = 'modulocompras.pedidohistorico'
    _description = 'Relacion historica de pedidos'


    # pedido_id = fields.Many2one('purchase.order', string='Pedido')
    nombre_pedido = fields.Char(string='Nombre de pedido')
    tipo_pedido = fields.Selection([('emp', 'empresarial'), ('pers', 'personal')], string='Tipo de pedido')
    modo_pedido = fields.Selection([
    ('pres', 'presencial'), ('cel', 'celular'), ('int', 'internet')], string='Modo de pedido')
