
longitud=[]
boyaca=     [[6.211,-72.481,  2], 
            [ 6.212,-72.470, 25],
            [ 6.105,-72.342, 25], 
            [ 6.210,-72.442, 50]] 

i = 1 #columna que queremos obtener
columna = [fila[i] for fila in boyaca]
longitud.append(columna)
for m in longitud:  
    longitud1=m[0]
    longitud2=m[1]
    longitud3=m[2]
print(longitud1)
print(longitud2)
print(longitud3)
