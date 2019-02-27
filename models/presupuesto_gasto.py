# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Presupuesto_gasto(models.Model):
    _name = 'gastos_mes.presupuesto_gasto'

    mes = fields.Many2one('gastos_mes.mes',string='mes', required=True)
 
    precio_piso = fields.Float(string='precio_piso', required=True)
 
    gastos_piso = fields.Float(string='gastos_piso', required=True)

    gastos_salir = fields.Float(string='gastos_salir', required=True)

    total = fields.Float(string='total', required=True, compute='_total')

    def get_presupuesto_gasto(self):
        presupuesto_gasto = []
        for p in self:
            name = p.mes + ' - presupuesto_gasto '
            presupuesto_gasto.append((p.id, name))
        return presupuesto_gasto

    @api.one
    @api.depends('total')
    def _total(self):
        self.total = self.precio_piso + self.gastos_piso + self.gastos_salir
