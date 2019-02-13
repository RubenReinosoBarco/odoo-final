# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Cliente(models.Model): 
    _name = 'tienda.cliente'
    nombre = fields.Char(string='nombre', required=True) 
 
    apellidos = fields.Char(string='apellidos', required=True) 
 
    dni = fields.Char(string='dni', required=True) 
 
    direccion = fields.Char(string='direccion', required=True) 
 
    telefono = fields.Char(string='telefono', required=True) 
 
    email = fields.Char(string='email', required=True) 
 
    provincia = fields.Char(string='provincia', required=True) 
 
    poblacion = fields.Char(string='poblacion', required=True) 
 
    codigo_postal = fields.Char(string='codigo_postal', required=True)


    def get_cliente(self):
        cliente = []
        for c in self:
            name = c.dni + ' - ' + c.apellidos
            cliente.append((c.id, name))
        return cliente