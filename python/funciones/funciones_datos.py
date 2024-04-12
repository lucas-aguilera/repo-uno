# creando una funcion de tres parametro

#def frase ( nombre,apellido,adjectivo):
  #  return f'hola {nombre} {apellido} sos muy {adjectivo}'

# utilizando keyword arguments
#resultado_frase=frase(adjectivo="capo",nombre="lucas",apellido="aguilera")
#print(resultado_frase) 


def frase ( nombre,apellido,adjectivo = "tonto"):
    return f'hola {nombre} {apellido} sos muy {adjectivo}'


frase_resultado= frase("lucas","aguilera",)
print(frase_resultado)
