# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Gasto_real(models.Model):
    _name = 'gastos_mes.gasto_real'

    mes = fields.Many2one('gastos_mes.mes', string='mes', required=True)

    precio_piso = fields.Float(string='precio_piso', required=True)

    gastos_piso = fields.Float(string='gastos_piso', required=True)

    gastos_salir = fields.Float(string='gastos_salir', required=True)

    total = fields.Float(string='total', required=True, compute='_total')

    def get_gasto_real(self):
        gasto_real = []
        for p in self:
            name = p.mes + ' - gasto_real '
            gasto_real.append((p.id, name))
        return gasto_real

    @api.one
    @api.depends('total')
    def _total(self):
        self.total = self.precio_piso + self.gastos_piso + self.gastos_salir