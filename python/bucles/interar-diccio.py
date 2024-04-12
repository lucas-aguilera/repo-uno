diccionario={
    "nombre":"lucas",
    "apellido":"aguilera",
    "supcritores":100000
}

# recorriendo un diccionario para tener las claves
for key in diccionario:
    key 
    print(f"la clave es: {key}")

# recorriendo un diccionario con items()para tener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value= datos[1]
    print(f"la clave es: {key} y el valor es : {value}")




