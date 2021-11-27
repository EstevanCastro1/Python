cadena = [[1,2,3],
           [4,1,6],
           [7,8,9]]
cadena2 = [[4,1,11],
           [1,2,3],
           [23,5,1]]
lista1=[]
lista2=[]
c=[]
d=[]
e=[]
f=[]
#convertir las matrices en listas simples
for i in cadena:
    for j in i:
        lista1.append(j)

for k in cadena2:
    for l in k:
        lista2.append(l)
#interseccion
for i in lista1:
    if i in lista2: #verdadero
        c.append(i)


#Union 
for i in lista1:
    if i in lista2:
        d.append(i)
    else:
        d.append(i)

for j in lista2:
    if j in d:
        pass
    else:
        d.append(j)

#diferencia

for i in lista1:
    if i in lista2:
        pass
    else:
        e.append(i)

#diferencia simetrica
'''for i in lista1:
    if i in lista2:
        pass
    else:
        f.append(i)

for i in lista2:
    if i in lista1:
        f.append(i)
    else:
        pass'''


#print (lista1)
#print (lista2)

print ("intersección ", c)
print ("unión ", d)
print ("diferencia", e)
print ("diferencia simetrica", f)






















#recorrer no tan fácil
'''for i in range (3):
    print (numeros[i])
    for j in range (3):
        print (numeros[i][j])'''





