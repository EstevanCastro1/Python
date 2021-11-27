filas_a=int(input("Digite el numero de filas para la matriz A \n"))
columnas_a=int(input("Digite el numero de columnas para la matriz A \n"))
filas_b=int(input("Digite el numero de filas para la matriz B \n"))
columnas_b=int(input("Digite el numero de columnas para la matriz B \n"))
a,b,c,d,e,f=[],[],[],[],[],[]#asignación multiple de variables.
for i in range(filas_a):
    a.append([])
    for j in range(columnas_a):
        a[i].append(input(f"digite el valor de la fila {i+1} columna {j+1} matriz A\n"))
for i in range(filas_b):
    b.append([])
    for j in range(columnas_b):
        b[i].append(input(f"digite el valor de la fila {i+1} columna {j+1} matriz B\n"))
for fila_a in a:
    for columna_a in fila_a:
        e.append(columna_a)#agregamos los elementos de la matriz a en una lista
        for fila_b in b:
            for columna_b in fila_b:
#unimos los conjuntos, con la validacion se evita repetir el elemento mas de una vez en la union
                if d.count(columna_a)<1:d.append(columna_a)
                if d.count(columna_b)<1:d.append(columna_b)
                if columna_a==columna_b and c.count(columna_a)<1:c.append(columna_a)#hallamos la interseccion en una lista  
f.extend(d)#damos el valor de la union a la lista que sera la diferencia simetrica
for i in c:
    f.remove(i)#hallamos la diferencia simetrica eliminando las coincidencias de la union con la interseccion
    e.remove(i)#hallamos la diferencia a-b eliminando las coincidencias de a con la interseccion
#realizamos la impresion
print(f"matriz A\n {a}\nmatriz B\n {b}\nintersección (A n B): {c}\nunion (A u B): {d}\ndiferencia (A-B): {e}\ndiferencia simetrica (a ▲ b): {f}")