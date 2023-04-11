#-*- coding: utf-8 -*-

{
    "name":"Jugadores",
    "summary": """
        Carga de jugadores y sus datos
    """,
    "author": "Alejo Marinsalda",
    "category":"General",
    "version":"1.0.0",
    "depends":["mail","crm","sale_management"],
    "data":[
        "views/menus_views.xml",
        "views/jugadores_view.xml",
        "security/jugadores_security.xml",
        "security/ir.model.access.csv",
        "views/vista_heredada.xml",
        "views/sales_heredada.xml"
    ]
}