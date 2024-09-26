# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InventoryProduct(models.Model):

    _name = 'inventory.product'
    _description = 'Productos que figuran en un inventario'
    _rec_name = 'name'

    name = fields.Char(string="Nombre del producto")
    description = fields.Text(string="Decripción")
    quantity = fields.Integer(string="Cantidad")
    price = fields.Float(string="Precio")

