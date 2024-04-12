# creando un conjunto con sep()
conjunto =set(["dato1"])


# metiendo un conjunto dentro de otro conjunto
conjunto1=frozenset(["dato1","dato2"])
conjunto2={conjunto1,"dato3"}

print(conjunto1)


# teoria de conjuntos

conjunto1={1,2,3,7}
conjunto2={8,9,6}

# verificando si es subconjunto
resultado= conjunto2.issubset(conjunto1)
resultado=conjunto1<=conjunto2

# verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >conjunto1

# verificando si  hay algun numero en comun:   "con esto me dice si 
# tengo algun elemento igual"
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)