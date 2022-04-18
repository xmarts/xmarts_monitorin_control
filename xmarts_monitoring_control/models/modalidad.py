# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Modalidad(models.Model):
    _name = "modalidad"

    name = fields.Char(string="Nombre")
