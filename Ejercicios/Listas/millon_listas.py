print("Ganar un millon")
lista=[] 
while True:
        
                         
            num=int(input("Ingrese un numero para agregar a lista: "))
            if num==num:
                lista.append(num)
        
            i=int(input("Pulse ¨1¨ si desea agregar mas numeros o Pulse ¨2¨ si no desea agregar mas numeros: "))
            if i==1:
                    continue
            if i==2:
                    break
for i in lista:
    pass
    if i>0:
     print(f"los numeros positvos en la lista: {i}")
for i in lista:
    pass
    if i<0:
     print(f"los numeros negativos en la lista: {i}")

b=lista.count(0)                        
print(f"la cantidad de numeros en la lista es de {len(lista)}")
print(f"la cantidad de ceros que hay en la lista es de {b}")
print(f"esta es la lista completa, verificando si hay un 100, esta es la lista ===> {lista}")

for i in lista:
    if i>100 or i<100:
     print("No hay numeros 100 en la lista, no has ganado nada, sigue intentando...")
    else:
     print("Felicidades hay un numero 100 en la lista has ganado un millon de pesos")

              



