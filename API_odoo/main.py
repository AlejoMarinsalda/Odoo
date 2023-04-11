#Protocolo que llama a procedimiento remoto (RPC)
import xmlrpc.client

#datos de conexion
url="http://localhost:8069"
db="odoo"
username="usuario_api"
password="123"

#password="25563b37f311801317875a3beff786799d7196cd"
#inicio de session
common=xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))


uid=common.authenticate(db,username,password,{})


#llamada a metodo a traves de execute_kw

models=xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

# valores a pasar  
# la base de datos a usar, debera ser una cadena
# la contraseña del usuario recuperado del metodo authenticate
# el nombre del modelo, cadena
# el nombre del metodo, cadena
# una matriz/lista de parametros pasados por posicion
# un mapeo/dictado de parametros para pasar por palabra clave
# en la siguiente linea estamos indicando que se conecte al modelo "purchase.order" y ejecutre el metodo "button_draft" en el registro de id[4]
result_button_draft=models.execute_kw(db,uid,password,"purchase.order","button_draft",[[4]])


#lectura de los campos dentro del modelo "res.partner"

result_execute= models.execute_kw(db,uid,password,"res.partner","read",[[10]])



#traer campos especificados
result_execute= models.execute_kw(db,uid,password,"res.partner","read",[[10]],{'fields':['name','country_id','comment']})


# print(result_execute)

result_execute= models.execute_kw(db,uid,password,"res.partner","action_unarchive",[[31]])