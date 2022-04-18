# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CategoriaProblema(models.Model):
    _name = "categoria.probrema"

    name = fields.Char(string="Descripcion")
