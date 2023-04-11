from odoo import models,fields,api


#creando un modelo(tabla de la base de datos) a partir de una clase
class Libros(models.Model):
   #nombre de la tabla
   _name = "libros"
   _inherit = ['mail.thread','mail.activity.mixin']
  

   #nombre de las columnas
   supervisor_id=fields.Many2one(comodel_name="hr.employee",string="Supervisor")
   name = fields.Char(string="Nombre del libro",required=True,tracking=True)
   editorial = fields.Char(string="Editorial", required=True)
   isbn= fields.Char(string="ISBN",required=True)
   autor_id=fields.Many2one(comodel_name="autor",string="Autor",required=True) #Many2one. Se representa como un desplegable que trae los registros del módulo al cual se relaciona
   apellido_autor=fields.Char(related="autor_id.apellido", string="Apellido del autor")
   image=fields.Binary(string="image")
   categoria_id= fields.Many2one( comodel_name="categoria.libro")
   state=fields.Selection([("draft","Borrador"),("published","publicado")], default="draft")  
   description=fields.Char(string="Descripcion",compute="_compute_description")
   
   
   
   @api.depends('name')
   def _compute_description(self):
       self.description = self.name + " | " + self.editorial + " | " + self.isbn + " | " + self.autor_id.name + " | " + self.categoria_id.name
   
   def boton_publicar(self):
      self.state ="published"
        
   def boton_borrador(self):
      self.state="draft"

class CategoriaLibro(models.Model):
   _name ="categoria.libro"

   name=fields.Char(string="Nombre de la categoria")


   


