# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Problema(models.Model):
    _name = "probrema"

    name = fields.Char(string="Name")
    categoria_id = fields.Many2one('categoria.probrema',string="Categoria")
    descripcion = fields.Char(string="Descripcion")
    monitoring_ids = fields.Many2one('monitoring.control')
