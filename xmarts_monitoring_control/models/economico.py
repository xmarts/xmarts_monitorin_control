# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Economico(models.Model):
    _name = "economico"

    name = fields.Char(string="Nombre")
