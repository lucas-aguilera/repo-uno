# le pedimos al ususario que nos digas una frace o (varias)
frace=input("decime una frace y calculo cuanto tendrias si tuviera que decirla: ")

# creamos una lista con todas las palabras de la frace (se separa cada ves que alla un espacio en blanco)
palabras_separada=frace.split(" ")

# usamos len() para ver la cantidad de elemento que hay en la lista
cantidad_de_palabras=len(palabras_separada)

# en caso que tarde mas de un minuto en decirlo,le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("para flaco tampoco te pedi un testamento")

# calculamos cuanto tendria en decir las palabras y se lo decimos
print(f'dijiste {cantidad_de_palabras}palabra,y tardaste {cantidad_de_palabras/2} segundo en decir')
print(f'dalto lo diria en {cantidad_de_palabras *100// 2*1.3/100} segu6ndos')


