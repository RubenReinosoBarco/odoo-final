# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Resumen_cuentas(models.Model):
    _name = 'gastos_mes.resumen_cuentas'
    mes = fields.Many2one('gastos_mes.mes', string='mes', required=True)

    presupuesto_gasto = fields.Many2one('gastos_mes.presupuesto_gasto', string='presupuesto_gasto', required=True)

    gasto_real = fields.Many2one('gastos_mes.gasto_real', string='gasto_real', required=True)

    precio_piso = fields.Float(string='precio_piso', required=True, compute='_gastos_salir')

    gastos_piso = fields.Float(string='gastos_piso', required=True, compute='_gastos_piso')

    gastos_salir = fields.Float(string='gastos_salir', required=True, compute='_gastos_salir')

    total = fields.Float(string='total', required=True, compute='_total')


    def get_cliente(self):
        resumen_cuentas = []
        for c in self:
            name = c.mes + ' - resumen_cuentas '
            resumen_cuentas.append((c.id, name))
        return resumen_cuentas

    @api.one
    @api.depends('total')
    def _total(self):
        self.total = (self.presupuesto_gasto.precio_piso + self.presupuesto_gasto.gastos_piso + self.presupuesto_gasto.gastos_salir) - (self.gasto_real.precio_piso + self.gasto_real.gastos_piso + self.gasto_real.gastos_salir)

    @api.depends('precio_piso')
    def _precio_piso(self):
        self.precio_piso = self.presupuesto_gasto.precio_piso - self.gasto_real.precio_piso
    @api.depends('gastos_piso')
    def _gastos_piso(self):
        self.gastos_piso = self.presupuesto_gasto.gastos_piso - self.gasto_real.gastos_piso
    @api.depends('gastos_salir')
    def _gastos_salir(self):
        self.gastos_salir = self.presupuesto_gasto.gastos_salir - self.gasto_real.gastos_salir

