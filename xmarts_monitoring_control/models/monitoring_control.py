# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MonitoringControl(models.Model):
    _name = "monitoring.control"
    _inherit = ['mail.thread']

    def _document_id(self):
        if self.id < 10:
            self.name = 'DOC0' + str(self.id)
        else:
            self.name = 'DOC' + str(self.id)
    problema_ids = fields.One2many(
        'probrema',
        'monitoring_ids',
        string='test')
    state = fields.Selection([
        ('ingreso', 'Ingreso'),
        ('aprobado', 'Aprobado'),
        ('salir', 'Por salir'),
        ('egreso', 'Egreso'),
        ('rechazado', 'Rechazado')
    ], default='ingreso', string="Estado")
    name = fields.Char(string="N° de documento", compute=_document_id)
    tipo_reg = fields.Selection([
        ('entrada', 'Entrada'),
        ('salida', 'Salida')
    ], default="salida", string="Tipo de registro", required=True)
    hora_llegada = fields.Datetime(string="Fecha y hora de llegada", default=fields.Datetime.now, required=True)
    hora_ingreso = fields.Datetime(string="Fecha y hora de ingreso", default=fields.Datetime.now, required=True)
    hora_salida = fields.Datetime(string="Fecha y hora de salida", default=fields.Datetime.now)
    nombre_chofer = fields.Char(string="Nombre del chofer")
    tipo_trans = fields.Selection([
        ('1ton', '1 Tonelada'),
        ('3ton', '3 Toneladas'),
        ('5ton', '5 Toneladas'),
        ('10ton', '10 Toneladas'),
        ('torton', 'Torton'),
        ('48pi', '48 Pies'),
        ('53pi', '53 Pies'),
        ('full', 'Full'),
        ('c20', 'Contenedor 20'),
        ('c40', 'Contenedor 40'),
        ('c48', 'Contenedor 48'),
        ('c53', 'Contenedor 53')
    ], string="Tipo de transporte")
    placas_tractor = fields.Char(string="Placas del tractor")
    placas_caja = fields.Char(string="Placas de la caja")
    placas_caja_dos = fields.Char(string="Placas de la caja 2")
    # cambios
    nombre = fields.Char(
        string='Nombre')
    aprobo = fields.Many2one(
        'hr.employee',
        string='Quien Aprobo')
    fecha_aprobacion = fields.Date(
        string='Fecha')
    image = fields.Binary(
        help="Este campo contiene la imagen utilizada como foto para el empleado, limitada a 1024x1024px.")
    identificacion = fields.Char(
        string='Identificacion')
    num_identificacion = fields.Char(
        string='Numero de Identificacion')
    procedencia = fields.Char(
        string='Procedencia')
    visita = fields.Many2one(
        'hr.employee',
        string='A quien visita')
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
    origen = fields.Char(string="Origen")
    destino = fields.Char(string="Destino")
    cedis = fields.Char(string="Cedis")
    purchase_id = fields.Many2one('purchase.order', string="Orden de compra")
    sale_id = fields.Many2one('sale.order', string="Orden de venta")
    provider_id = fields.Many2one('res.partner', string="Proveedor", related="purchase_id.partner_id", readonly=True)
    carrier_id = fields.Many2one('res.partner', string="Transportista")
    purchase_lines = fields.One2many("purchase.order.line", string="Productos", related="purchase_id.order_line")
    sale_lines = fields.One2many("sale.order.line", string="Productos", related="sale_id.order_line", readonly=True)
    motivo_rechazo = fields.Many2one("monitoring.motivos", string="Motivo de rechazo")
    clean_unit = fields.Boolean(string='Unidad limpia', default=False)
    no_leaks = fields.Boolean(string='Sin filtraciones de luz o agua', default=False)
    damage_door_floor = fields.Boolean(string='Daños en pisos o puertas', default=False)
    odor_free = fields.Boolean(string='Libre de olores', default=False)
    no_graffiti = fields.Boolean(string='No graffiti', default=False)
    transport_observations = fields.Text(string='Observaciones del transporte')
    condiciones_trans = fields.Text(string="Condiciones del transporte")
    product_programed = fields.One2many("purchase.order.programing", "monitoring_id", string="Lista programada", delete=False)
    fecha_registro = fields.Date(string="Fecha de creación", default=fields.Date.today())
    # Control de calidad
    humidity = fields.Float(string="Humedad %")
    texture = fields.Float(string="Textura %")
    density = fields.Float(string="Densidad")
    brix = fields.Float(string="BRIX")
    temperature = fields.Float(string="Temperatura")
    carbonates = fields.Float(string="Carbonatos")
    a_u = fields.Float(string="A.U.")
    tannins = fields.Float(string="Taninos %")
    rancidity = fields.Float(string="Rancidez")
    agl = fields.Float(string="AGL")
    plague = fields.Float(string="Plaga")

    @api.onchange('carrier_id')
    def onchange_carrier_id(self):
        self.nombre_chofer = self.carrier_id.name
        self.linea_trasporte_id = self.carrier_id.linea_trasporte_id.id
        self.modalidad_id = self.carrier_id.modalidad_id.id
        self.economico_id = self.carrier_id.economico_id.id
        self.tipo_licencia = self.carrier_id.tipo_licencia
        self.licencia = self.carrier_id.licencia

    @api.onchange('tipo_reg')
    def onchange_tipo_reg(self):
        if self.tipo_reg == 'salida':
            self.purchase_id = ''

        if self.tipo_reg == 'entrada':
            self.sale_id = ''

    def action_salida_control(self):
        self.ensure_one()
        if self.state == 'aprobado':
            self.state = 'salir'

    def action_egreso_control(self):
        self.ensure_one()
        if self.state == 'salir':
            self.state = 'egreso'

    def action_acept_control(self):
        self.ensure_one()
        if self.state == 'ingreso':
            self.state = 'aprobado'

    def action_refuse_control(self):
        self.ensure_one()
        if self.state == 'ingreso':
            self.state = 'rechazado'

    def action_draft_control(self):
        self.ensure_one()
        if self.state == 'aprobado' or self.state == 'salir' or self.state == 'egreso' or self.state == 'rechazado':
            self.state = 'ingreso'
