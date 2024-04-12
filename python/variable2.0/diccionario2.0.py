# crenado un diccionario con dic()
diccionario= dict(nombre="lucas",apellido="aguilera")

# las lista no pueden ser claves usamos frozenset para meter conjuntos
diccionario={frozenset(["dalto","rancio"]):"jajas"}


# creando unb diccionario con fromkeys()valor por defecto:none
diccionario=dict.fromkeys(["nombre","apellido"])

# creando diccionario con fromkeys()cambiando el valor del defecto por "no se"
diccionario=dict.fromkeys(["nombre","apellido"],"no se")



print(diccionario)