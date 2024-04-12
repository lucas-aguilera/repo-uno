#esto es un array que tiene una lista de contenido  []
#con lista puedo cambiar contenido
lista=["lucas ","aguilera",True,1.85]

#datos compuestos que son las tuple no se puede modificar las variables
tuple=("lucas ","aguilera",True,1.85)

#creando conjunto (set),no hacede elem por indeci,no alamacena datos duplicado
conjuntos={"lucas ","aguilera",True,1.85} #en un conjunto son elem desordenado y puede cambiar
#print(cinjunto[2])>no se puede haceder ah elementos


#creando un dicionario

dicionario={
'nombre':"lucas",
#la estrotura es key ='nombre' y value='lucas' y separamos con coma ,
'apellido':"aguilera",
'estas_emocionado':"true",
'altura':1.85
#cuando termino de poner elemento ya no lleva coma ,
}
print(dicionario['altura']+2)
