print ("****************************************")
print ("* PROGRAMA DE HONORARIOS PARA DOCENTES *")
print ("****************************************")
for i in range (1, 1000, 1):
     Cod=int (input("Digite el codigo del docente: "))
     Nom=str (input("Digite el nombre del docente: "))
     Hor=int(input("Digite las horas laboradas por el docente: "))
     print("elija a la categoria que corresponde")
     print ("*****************************")
     print ("*CATEGORIA 1======> 35.0000 *")
     print ("*CATEGORIA 2======> 40.0000 *")
     print ("*CATEGORIA 3======> 50.0000 *")
     print ("*****************************")
     Cat=int(input(": "))
     if Cat<1 or Cat>3:
        print("Este categoria no existe")
        i=int(input("Digite 1 si desea agregar otro profesor o 999 si desea salir: "))
        if i==1:
           pass
        if i==999:
            break
        if i!=1 or i!=999:
            print("Eligio una opcion incorrecta, ERROR")
            break
     elif Cat==1:
         cant=Hor*35.000
         print(f"Profesor {Nom} Su codigo es {Cod} y su cantidad de honorarios es {cant}")
         i=int(input("Digite 1 si desea agregar otro profesor o 999 si desea salir: "))
         if i==1:
           pass
         if i==999:
            break
         if i!=1 or i!=999:
            print("Eligio una opcion incorrecta, ERROR")
            break
     elif Cat==2:
         cant=Hor*40.000
         print(f"Profesor {Nom} Su codigo es {Cod} y su cantidad de honorarios es {cant}")
         i=int(input("Digite 1 si desea agregar otro profesor o 999 si desea salir: "))
         if i==1:
           pass
         if i==999:
            break
         if i!=1 or i!=999:
            print("ERROR")
            break
     elif Cat==3:
         cant=Hor*50.000
         print(f"Profesor {Nom} Su codigo es {Cod} y su cantidad de honorarios es {cant}")
         i=int(input("Digite 1 si desea agregar otro profesor o 999 si desea salir: "))
         if i==1:
           pass
         if i==999:
            break 
         if i!=1 or i!=999:
            print("Eligio una opcion incorrecta, ERROR")
            break       
print("Muchas gracias, Adios")
     