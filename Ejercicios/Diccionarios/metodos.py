
#DICT recibe com parametro una reresentacion de un diccionario, si la organizacion 
#de los datos es correta
datos=dict(nombre="Gerardo", apellido="Cardona", edad=35)
print(datos)

#Zip recibe dos datos iterables, deben tener la misma cantida de elementos
diccionario=dict(zip(["12345","12345"], ["uno", "dos","tres", "cuatro", "cinco"])) 
print(diccionario)

#Items devuelve una lista con tupla se compone de dos elementos. el 1 la clave y el segundo el valor
dic2={"a":1,"b":2,"c":3}
items=dic2.items()
print(items)

#keys devuelva  retorna una lista de elementos y eso es la clave de nuestr diccionario
keys=dic2.keys()
print(keys)

#Values devuelve los valores 
values=dic2.values()
print(values)

#clear limpia un diccionario
#dic2.clear()
#print(dic2)

#copy copia el diccionario
dic3=dic2.copy()
print(dic2)
print(dic3)

#get recibe como paremetro la clave, devuelve el varlor de clave si no lo encuentra

valor=dic2.get("a")
print(valor)

#pop recibe como parametro clave y lo elimina

valor3=dic2.pop("c")
print(valor3)
print(dic2)



#setdeaful de dos manera 1: me trae el valor 2: si le envio dos argumentos
#los agrega al diccionario al final de la fila

valor4=dic2.setdefault("a")
print(valor4)

valor5=dic2.setdefault("d",4)
print(dic2)

##clave=input("digite la clave: ")
#valor6=int(input("Digite el valor: "))
#dic2.setdefault(clave, valor6)
#print(dic2)


#update atualiza la clave repetida de dos diccionarios
#si no agraga al diccionarios

dic10={"a":1,"b":2,"c":3}
dic20={"d":4,"b":2,"e":5}

dic10.update(dic20)
print(dic10)






