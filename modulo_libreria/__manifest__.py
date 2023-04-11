#-*- coding: utf-8 -*-

{
    "name":"Libreria",
    "summary": """
        Carga de libros con sus respectivos datos
    """,
    "author": "Alejo Marinsalda",
    "category":"General",
    "version":"1.0.0",
    "depends":["mail","hr"],
    "data":[
        "views/menu_views.xml",
        "views/libros_view.xml",
        "security/libreria_security.xml",
        "security/ir.model.access.csv",
        "views/hr_employee_view.xml"
    ]
}