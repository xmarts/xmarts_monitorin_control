# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LineaTransporte(models.Model):
    _name = "linea.transporte"

    name = fields.Char(string="Nombre")
