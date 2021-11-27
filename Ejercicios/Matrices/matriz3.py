numeros = []
a=int(input("Ingrese el numero de filas para la matriz: "))
b=int(input("Ingrese las columnas de la matriz: "))
print(a)
print(b)

for i in range(a):
    numeros.append([])
    print(numeros)
    for j in range (b):
        num=int(input("ingrese un numero para formar los conjuntos: "))
        print(num)
        print(a)
        print(b)
        numeros[i].append(num)
print(numeros)

#procesar la matrix
pos=0
neg=0
cceros=0
for i in numeros:
    for j in i:
        if j==0:
           cceros+=1
        elif j>0:
            pos+=1
        else:
            neg+=1
            
print (f" la cantidad de ceros dentro de la matriz {a}x{b} es de {cceros}")
print (f" la cantidad de positivos dentro de la matriz {a}x{b} es de {pos}")
print (f" la cantidad de negativos dentro de la matriz {a}x{b} es de {neg}")

