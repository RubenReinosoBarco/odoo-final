# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Producto(models.Model):
    _name = 'tienda.producto'
    nombre = fields.Char(string='nombre', required=True) 
 
    descripcion = fields.Char(string='descripccion', required=True)
 
    proveedor = fields.Many2one('tienda.proveedor',string='proveedor', required=True)
 
    precio_coste = fields.Float(string='precio_coste', required=True)
 
    precio_venta = fields.Float(string='precio_venta', required=True)
 
    referecia_proveedor = fields.Char(string='referecia_proveedor', required=True) 
 
    codigo_barras = fields.Char(string='codigo_barras', required=True) 
 
    stock = fields.Integer(string='stock', required=True) 
 
    def get_producto(self):
        producto = []
        for p in self:
            name = p.nombre + ' - ' + p.referecia_proveedor
            producto.append((p.id, name))
        return producto