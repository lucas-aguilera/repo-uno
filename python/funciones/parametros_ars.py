# forma no correcta para sumar valores
 #def suma(lista):
  #  numero_sumados= 0
   # for numero in lista:
    #    numero_sumados = numero_sumados +numero
   # return numero_sumados
    
#resultado=  suma ([5,3,12,30,20])

# forma optima de sumar valores
def  suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,12,30,50])
print(resultado2)



#lo mismo que arriba pero  utilizando el operador args * como argumento (args*)
def suma (nombre,*numeros):
    return f'{nombre}, la suma de tu numero es:{sum (numeros)}'

resultado = suma ("lucas",5,3,12,30,20)
print(resultado)


print(resultado)







