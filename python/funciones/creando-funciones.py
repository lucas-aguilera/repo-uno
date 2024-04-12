#crenado una funcion simple 
def saludar():
    print("hola lucas,como ¿estas?")
    
# ejecutando la funcion simple    
saludar()
saludar()

# clear una funcion con parametro 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjectivo = "reina"
    elif(sexo == "hombre"):
        adjectivo = "titan"
    else:
        adjectivo = "amor"    
    print(f'hola {nombre}, mi {adjectivo} ¿como estas')
    
saludar("camila","mujer")    
saludar("lucas","hombre")
saludar("fran","no binario")
    
    
# crear funciones que nos retornes multiples valores como una clave
def crear_contraseña_random(num):
    chars = "absdefghij"
    num_entero= str(num)
    num = int(num_entero[0])   
    c1 = num -2
    c2 = num
    c3 = num -5
    
    contraseña =f'{chars[c1]}{chars[c2]}{chars[c3]}{num *2}' 
    return contraseña,num

# desempaquetado la funcion
password,primer_numero =crear_contraseña_random(3)


# mostrando los resultados obteniendo y los datos utulizados para tenerlos
print(f'tu contraseña nueva es: {password}')
print(f'el numero utulizado para crear fue:{primer_numero}')
    
