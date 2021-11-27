numeros=[[45,70,60], # 0 
         [80,75,60], # 1
         [90,100,25]]
estudiante=["Luis", "Pedro", "Maria"]
notas=[]

for i in numeros:
    for j in i:
        notas.append(j)

nota1=round((notas[0]+notas[1]+notas[2])/3)
nota2=round((notas[3]+notas[4]+notas[5])/3)
nota3=round((notas[6]+notas[7]+notas[8])/3)

pro=round((nota1+nota2+nota3)/3)
print(f"La definitiva de {estudiante[0]} es {nota1} ")
print(f"La definitiva de {estudiante[1]} es {nota2} ")
print(f"La definitiva de {estudiante[2]} es {nota3} ")
print(f"el promedio general del curso es {pro}")
print(f"la nota maxima es {notas[7]} y la nota minima es {notas[8]}")
