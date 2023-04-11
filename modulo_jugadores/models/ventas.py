from odoo import fields,models



class Ventas(models.Model):
    _inherit = "sale.order"



    is_supervisor = fields.Boolean(string="Es supervisor")