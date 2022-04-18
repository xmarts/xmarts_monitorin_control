# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseProgramedOrder(models.Model):
    _name = "purchase.order.programing"

    def _get_domain(self):
        ids = self.purchase_id.order_line.mapped('product_id').ids
        return [('id', 'in', ids)]

    purchase_id = fields.Many2one("purchase.order")
    product_id = fields.Many2one("product.product", string="Producto", domain=_get_domain)
    product_qty = fields.Float(string="Cantidad a recibir")
    product_uom = fields.Many2one("uom.uom", string="Unidad de medida", related="product_id.uom_id", readonly=True)
    date_planned = fields.Date(string="Fecha planeada")
    state = fields.Selection([('to_program','A programar'),('programed','Programada'),('done','Entregado')], string="Estado", default="to_program")
    monitoring_id = fields.Many2one("monitoring.control")

    @api.onchange('purchase_id')
    def _onchange_purchase_id(self):
        if self.purchase_id:
            return {'domain': {
                'product_id': [('id', 'in', self.purchase_id.order_line.mapped('product_id').ids)]}
            }
