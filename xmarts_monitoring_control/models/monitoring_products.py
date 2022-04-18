# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MonitoringProducts(models.Model):
    _name = "monitoring.products"

    monitoring_id = fields.Many2one("monitoring.control")
    product_id = fields.Many2one("product.product", string="Producto", readonly=True)
    fecha = fields.Datetime(string="Fecha prevista", readonly=True)
    product_uom = fields.Many2one("uom.uom", string="Unidad de medida", readonly=True)
    product_qty = fields.Float(string="Cantidad", readonly=True)
