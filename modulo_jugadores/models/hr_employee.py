from odoo import fields,models


class HrEmployee(models.Model):
     _inherit = "crm.team"

     campo_nuevo= fields.Char("deporte favorito")