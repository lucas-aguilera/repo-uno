#import modulo_saludar y asinamos el nombre  "m_saludar"
#import  modulo_saludar as m_saludar  

#saludo = modulo_saludar.saludar("martin")
#print(saludo)

# de este modulo importamos dos funciones 
from modulo_saludar import saludar,saludar_raro


# creamos variables ded saludos
saludo = saludar("lucas")
saludar_raro = saludar_raro("amira")

# mostramos los resultado
print(saludo)
print(saludar_raro)


# para ver todo las propiedades y metodo del el namespace 
#print(dir(m_saludar))