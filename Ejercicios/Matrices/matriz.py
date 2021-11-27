
        #1
letras=[["a","t","i"], # 0 
        ["f","o","j"], # 1
        ["u","r","e"]] # 2
print(letras)
        #0 1 2
cons=[]
cv= 0
#i= recorre la primera fila 
for i in letras:
    for j in i:
        print(j)
        if j!="a" or j!="e" or j!="i" or j!="o" or j!="u":
            cv = cv +1
            cons.append(j) 
        else:
            pass
print(f"la cantidad de vocales dentro de la matriz es {cv}")
print(cons)    #matriz ordenada
    #print(i)
    
