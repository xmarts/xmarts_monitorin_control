# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    linea_trasporte_id = fields.Many2one(
        'linea.transporte',
        string='Linea de Transporte')
    modalidad_id = fields.Many2one(
        'modalidad',
        string='Modalidad')
    economico_id = fields.Many2one(
        'economico',
        string='Economico')
    tipo_licencia = fields.Selection([
        ('autom', 'Automovilista'),
        ('chofer', 'Chofer'),
        ('federal', 'Federal')
    ], string="Tipo de licencia")
    licencia = fields.Char(string="N° de licencia")
    is_carrier = fields.Boolean(string='Es transportista')
