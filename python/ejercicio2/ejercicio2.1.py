# falto el profe y los pibes van arma la clase 

# pedir el nombre y la edad de cada pibe que vino ala clase 

# funcion para tener el asistente y al profesor segun su edad
def obtener_compañeros(cantidad_de_compañeros):
    
    # creando la lista con los compañero
    compañeros = []
    
    # ejecutando un for para pedir la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombres = input("ingrese el nombre de compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombres,edad)
        
        #agregando la informacion de la lista
        compañeros.append(compañero)
        
    # ordenando de menor o mayor segun su edad     
    compañeros.sort(key=lambda x:x[1])
    
    # compañero [x] devuelve una tupla  con (nombre,edad) y despues acedemos  al nombre
    # para definir al asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # retonamos ah una tupla
    return asistente,profesor
# desapaquetamos lo que nos retona ah una funcion
asistente,profesor = obtener_compañeros(5)    

# mostrando el resultado
print(f'el profesor es {profesor} y su asistente es {asistente}')

        







