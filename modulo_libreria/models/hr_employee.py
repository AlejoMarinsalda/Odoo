from odoo import models,fields

class HrEmployee(models.Model):
     _inherit = "hr.employee" #cuando el modelo ya existe se remplaza la palabra "_name" por "_inherit"


     is_supervisor = fields.Boolean(string="Es supervisor")