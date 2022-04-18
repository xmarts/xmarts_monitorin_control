# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ref_proveedor = fields.Char(string='Referencia proveedor')
    ref_cliente = fields.Char(string='Referencia cliente')
