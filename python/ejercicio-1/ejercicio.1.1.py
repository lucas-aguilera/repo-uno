# promedio de duracion varible
otro_curso_min = 2.5
otro_curso_max = 7
otro_curso_promedio = 4
dalto_curso = 1.5

#duracion del crudo del video
crudo_promedio=5
crudo_dalto=3.5

# diferencia en duracion
diferencia_con_min =100- dalto_curso / otro_curso_min *100
diferencia_con_max =100- dalto_curso *1000 // otro_curso_max /10
diferencia_con_promedio =100- dalto_curso / otro_curso_promedio *100

# calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio= 100- otro_curso_promedio *1000 // crudo_promedio /10
tiempo_vacio_dalto= 100- dalto_curso *1000 // crudo_dalto /10

# mostrando diferencia del ejercicio "A"
print("---------")
print("el curso de dalto dura")
print(f'- un {diferencia_con_min} % menos que el mas rapido')
print(f'- un {diferencia_con_max} % menos que el mas lento')
print(f'- un {diferencia_con_promedio} % menos que el mas promedio')
print("---------------")

# mostrando la calida de espacio vacio que se remueve en el ejercicio"B
print(f'el curso promedio elimino {tiempo_vacio_promedio} % de tiempo vacio')
print(f'el curso dalto elimino {tiempo_vacio_dalto} % de tiempo vacio')
print("-----------------")
# mostrando diferencia si el curso duraran 10 horas 
print(f'ver 10 horas de este curso equivale ver {otro_curso_promedio *100 // dalto_curso /10} horas de otro curso' )
print(f'ver 10 horas de otro curso equivale ver {dalto_curso *100 // otro_curso_promedio /10} horas de este curso' )
