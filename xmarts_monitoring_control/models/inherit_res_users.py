# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = "res.users"

    valida_logistica = fields.Boolean(string="Valida Logistica", default=False)
