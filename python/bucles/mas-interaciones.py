# creando las lista
frutas = ["manzana","frutilla","pera","granada","naranja","banana","durazno"]
cadena = "hola dalto"
numero =[2,4,10,50]


# evitando que se coma una naranja con la centencia continue
for fruta in frutas:
    if fruta == "naranja":
     continue
    print(f'me voy ah comer una {fruta}')
print("-------------------------")
# evitar que el bucle continue
for fruta in frutas:
    if fruta == "naranja":                 # con el break termina hay 
        break                         
else:
    print("terminado")    
    
# recorre una cadena de texto
for letra in cadena:
    print(letra)    
    
# for en una sola linia de codigo ( duplicamos los numeros)    
numeros_duplicados=[x*2 for x in numero]
print(numeros_duplicados)
    