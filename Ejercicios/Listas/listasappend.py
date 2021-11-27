par=[]
impar=[]
while True:
        try:
                num=int(input("Ingrese un numer impar o impar: "))
                if num%2==0:
                    par.append(num)
                    a="carlos rendon"
                    par.append(a)
                else:
                    impar.append(num)
                i=str(input("Pulse ¨S¨ si desea continuar o pulse otra tecla si no desea continuar"))
                if i=="S":
                    continue
                else:
                    break
        except Exception as error:
            print("Digite un numero par o impar")
print(par)
print(impar)