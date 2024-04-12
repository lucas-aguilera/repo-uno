diccionario = {
    "nombre" : "lucas",
    "apellido" : "aguilera",
    "sucri": 1000000
}
# nos devuelve un objeto dict_item
clave = diccionario.keys()

# obteniendo un elemento con get()(no me lanza una exepcion 
# si no encuentra nada el programa continua  )
valor_de_kasdks = diccionario.get("hjkiuh")


#eliminando todo  lo del diccionario
#diccionario.clear()

#eliminando un elemento del dicionario
diccionario.pop("apellido")

#obteniendo un elemento dict_itms interable
#con esto recorro el elemento
diccionario_interable = diccionario.items()

print(diccionario_interable)