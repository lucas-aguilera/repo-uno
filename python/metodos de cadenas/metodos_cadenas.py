cadena1="hola,maquina,como,esta"
cadena2="bienvenido bro"


#converti en mayuscula
mayusc=cadena1.upper()

#convierten en minuscula 
minuscula=cadena1.lower()

#primera letra en mayuscula
primera_letra_mayusc=cadena1.capitalize()

#me busca un valor que le pida , tambien si no encuentra el valor nos da -1
busqueda_find=cadena1.find("h")

#buscamos una cadena en otra cadena , si no encuentra nada nos tira una exepcion 
busqueda_index=cadena1.index("h")

#si es numerico nos devuelve true,si nos devuelve false
es_numerico=cadena1.isnumeric()

#si es alfanumerico devuelve true,si nos da false
#para el alfanumerico no tengo que dejar espacio elp=lucasaaguilera
es_alfanumerico=cadena1.isalpha()

#buscamos una cadena en otra cadena,devuelve las veces que que se repite
contar_considencia=cadena1.count("a")

#contamos los caracteres que tiene una cadena
#len no es un metodo es una funcion
contar_caracteres=len(cadena1)

#verifivamos si una cadena empieza con otra cadena dada,si es asi devuelve true
empieza_con = cadena1.startswith("a")

#verifivamos si una cadena termina  con otra cadena dada,si es asi devuelve true
termina_con = cadena1.endswith("a")


# remplaza una cadena dada , por otra cadena dada
#si el valor 1,se encuentra en el mismo original,remplaza el valor 1 de la misma,
#por el 2
cadena_nueva = cadena1.replace( ","," " )
cadena_nueva2 =cadena1.capitalize()

#separa cadena con la cadena que le pasamos
# poniendo print (type(cadena_separada))me dice que clase de lista es
#y poniendo asi me dice que es una lista: cadena_separadas=cadena1.split(",")
#poniendo asi me dice que hay en cada posicion: print((cadena_separadas[1]))
cadena_separadas=cadena1.split(",")


print((cadena_separadas[1]))


