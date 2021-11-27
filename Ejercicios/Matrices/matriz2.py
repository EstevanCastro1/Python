
        #1
numeros=[[-4,-1,0], # 0 
         [78,0,98], # 1
         [0, 0,45]] # 2
        #0 1 2
posi=[]
neg=[]
con=0
con2=0
con3=0


for i in numeros:
    for j in i:
        if j>0:
            con = con +1
            posi.append(j) 
        elif j<0:
            con2 = con2 +1
            neg.append(j)
        elif j!=0:
            con3 = con3 +1
        else:
            pass
print(f"la cantidad de positivos es {con}")
print(posi) 
print(f"la cantidad de negativos es {con2}")
print(neg) 
print(f"la cantidad de ceros {0}")  
    
