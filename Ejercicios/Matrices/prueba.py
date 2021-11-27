A=[(0,0),(5,5)]
B=[(0,0),(10,5)]
def interseccion(x,y):
 
 for i in range(0, len(A), 2):
    line1 = A[i:i+2]
    for j in range(0, len(B), 2):
        line1 = A[j:j+2]
        puntos_de_interseccion =interseccion(line1,line2)
        if puntos_de_interseccion:
            print (puntos_de_interseccion)