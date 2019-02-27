# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Mes(models.Model):
    _name = 'gastos_mes.mes'

    mes = fields.Char(string='mes', required=True)
 
    anio = fields.Integer(string='anio', required=True)


    def get_mes(self):
        mes = []
        for c in self:
            mes = c.mes + ' - ' + c.anio
            mes.append((c.id, mes))
        return mes



