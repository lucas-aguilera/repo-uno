# creando una funcion que nos de vuelva nos numeros primos 
# entre el 0 y el argumento que pasamos  


# creando una funcion verificando si los numeros son primos
def es_primo(num):

# verificamos que el numero pasado no pueda dividirse  
# por ningun numero entre 2 y el mismo numero -1  
    for i in range(2,num-1):
        # si es divisible por alguno retornamos  false y termina  el bucle
        if num%i==0: return False
        # si termina el bucle , significa que no fue  divisible entoces es primo
        return True
    
# creando una funcion que retorne con  todos los primos 
def primos_hasta(num):
    # creamos la lista 
    primos = []
    for i in range(3,num+1):
        # verificamos que el valor sea primo
        resultado = es_primo(i)
        # en caso que no sea primo agregamos una lista 
        if resultado == True:primos.append(i)
        # devolvemos la lista 
    return primos        
# creamos el resultado y llamando a la funcion y la mostramos
resultado= primos_hasta(13)
print(resultado)
