animales = ["gato","perro","loro","cocodrilo"]
numeros=[25,35,45,55]

#recorriendo la conjuntos animales
for animal in animales:
    print(f'ahora la variable animal es igual a:{animal}')
print("---------------------")
# recorriendo una conjuntos y cada valor multiplicando por 10
for numero in numeros:
    resultado= numero *10
    print(resultado)
print("--------------------")
for numero,animal in zip(animales,numeros):
    print(f"recorriendo conjuntos 1:{numero}")
    print(f"recorriendo conjuntos 2:{animal}")
print("--------------------")
for num in range(15,20):
    print(num)
print("---------------------")
# forma no correcta de reccorre una conjuntos 
for num in range(len(numeros)):
    print(numeros[num])
print("----------------")  
# forma correcta de recorre una conjuntos con su indece (no funciona en conjunto)
for num in enumerate(numeros):
    indece=num[0]
    valor=num[1]
    print(f'el indece es:{indece}y el valor es:{valor}')
else:
    print("el bucle termino")    
print("---------------------")
# recorriendo con for/else 

for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')

# todo lo anterior sirve para tupla y conjunto