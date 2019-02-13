# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Proveedor(models.Model): 
    _name = 'tienda.proveedor'
    cif = fields.Char(string='cif', required=True) 
 
    nombre = fields.Char(string='nombre', required=True) 
 
    direccion = fields.Char(string='direccion', required=True) 
 
    telefono = fields.Char(string='telefono', required=True) 
 
    provincia = fields.Char(string='provincia', required=True) 
 
    poblacion = fields.Char(string='poblacion', required=True) 
 
    codig_ = fields.Char(string='codig_', required=True) 
 
    email = fields.Char(string='email', required=True) 
 
    def get_proveedor(self):
        proveedor = []
        for p in self:
            name = p.cif + ' - ' + p.nombre
            proveedor.append((p.id, name))
        return proveedor