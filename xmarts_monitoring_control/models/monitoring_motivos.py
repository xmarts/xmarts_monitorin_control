# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MonitoringMotivos(models.Model):
    _name = "monitoring.motivos"

    name = fields.Char(string="Motivo")
