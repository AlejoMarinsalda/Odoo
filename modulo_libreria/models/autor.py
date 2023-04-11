from odoo import fields,models


class Autor(models.Model):
    _name= "autor"
    # _rec_name="apellido" Indicamos que columna queremos que nos retorne como "_name"

    name = fields.Char(string="Nombre")
    apellido=fields.Char(string="apellido")