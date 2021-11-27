import os
i=0
while i!=5:
    print("Bienvenido a mi juego de magia")
    print("debes ingresar un numero secreto para poder salir del programa")
    i=int(input("Ingrese un numero del 1 al 10: "))
    if i==5:
        print("Felicitaciones el", i, "si era el numero correcto")
    elif i>10 or i<1:
        os.system("cls")
        print("Error el numero", i , "no esta en los numeros permitidos")
    else:
        os.system("cls")
        print("Fallaste el", i, "no era el numero correcto")
        
    

