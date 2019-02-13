# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Carrito(models.Model): 
    _name = 'tienda.carrito'

    referencia = fields.Char(string='referencia', required=True) 
 
    fecha = fields.Datetime(string='fecha', required=True) 
 
    descripcion = fields.Char(string='descripcion', required=True) 
 
    cliente = fields.Many2one('tienda.cliente',string='cliente', required=True)
 
    productos = fields.Many2one('tienda.producto',string='productos', required=True)
 
    base_imponible = fields.Float()
 
    iva = fields.Float(string='iva', required=True)
 
    cantidad = fields.Float(string='cantidad', required=True)
 
    total = fields.Float(string='total', required=True, compute='_total')

    def get_carrito(self):
        carrito = []
        for c in self:
            name = c.referencia + ' - ' + c.fecha
            carrito.append((c.id, name))
        return carrito


    @api.one
    @api.depends('cantidad')
    def _total(self):
        self.base_imponible = self.productos.precio_venta
        self.total = (self.base_imponible * self.cantidad) * self.iva

