numeros=[1,2,3,4,5,10,12]

# creando una funcion lambda para multiplicar por dos 
multiplicar_por_dos= lambda x :x*2

# creando una funcion comun que diga si es para o no 
#def es_pàr(num):
 #   if (num%2==1):
  #      return True
    
# usando filter con una funcion comun
#numeros_pares= filter(es_pàr,numeros)

# creando lo mismo que antes pero con lambdas
numeros_pares = filter(lambda numero:numero %2 == 0,numeros)

print(list(numeros_pares))




