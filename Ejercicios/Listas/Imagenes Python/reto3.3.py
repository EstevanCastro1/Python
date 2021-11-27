#Declaramos matriz
matriz = []
#importamos el modulo os 
import os
import sys
#Se define usuario y contraseña paraingresar.
usuario = "51601"
contraseña = "10615"
#mensaje de bienvenida.
print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")
entrada1  = input("nombre de usuario: ")
#se verifica si entrada1 es igual a usuario, si es igual pide ingresar contraseña,
# de lo contrario saldra error. 
if entrada1 == usuario:
    entrada2 = input("contraseña: ")
    #se verifica si entrada2 es igual a contraseña, si es igual pide verficar el captcha, 
    #de lo contrario saldra error.
    if entrada2 == contraseña:
        print ("captcha de seguridad:")
    else:print("Error"),exit()
else:print("Error"),exit()
#se realizan las operaciones para crear el captcha.
termino_1 = int(601)
termino_2 =int((6*1)-5-1)
captcha = input("601+0= ")
#si el captcha es correcto se iniciara sesion, de lo contrario saldra error.
if captcha == "601":
    print("Sesión iniciada\n")
else:
    print("Error"), exit()
# #confirmacion de inicio de sesion 
#creamos el menu de opciones 
menu= ["MENÚ", "1.Cambiar contraseña", "2.Ingresar coordenadas actuales", "3.Ubicar zona wifi más cercana",
 "4.Guardar archivo con ubiacion cercana", "5.Actualizar registros de zonas wifi desde archivo",
 "6.Elegir opcion de menú favorito", "7.Cerrar sesión\n"
]
menu2= ["MENÚ", "1.Cambiar contraseña", "2.Ingresar coordenadas actuales", "3.Ubicar zona wifi más cercana",
 "4.Guardar archivo con ubiacion cercana", "5.Actualizar registros de zonas wifi desde archivo",
 "6.Elegir opcion de menú favorito", "7.Cerrar sesión\n"
]
#creamos un variable contadora,el usuario tendra tres posibilidades de ingresar  una opción del menu, 
# de lo ocntrario se finaliza la ejecución del programa 
cont = 1
while menu:
    #se imprime el menú de opciones 
    for ele in menu:
        print(ele)
    #el usuario elije la opcion que desee
    opcion= int (input("Elija una opción: "))
    if opcion == 6:
        #para reordenar el menú, el usuario debe elejir una opción entre 1 y 5 como opción favorita 
        favorito = int(input("Seleccione opción favorita: "))
        if favorito > 0 and favorito <= 5:
            #el usuario debe realizar la siguiente verificación para confirmar el cambio del menù
            print("para confirmar por favor responda:")
            validacion_1 = int(input("Se trata de un caso extraño, pues siendo siempre el mismo vale mucho o vale nada, según el sitio en el que vaya: "))
            if validacion_1 == 0:
                print("para confirmar por favor responda:")    
                validacion_2 = int(input("Cuado te pones a contar, por mi tienes que empezar: "))
             #si la respuesta es incorrecta debe volver al menu principal 
            else:
                print("Error") 
                continue
             #si ambas respuestas son correctas el programa limpia la consola y reordena el nuevo menú
            if validacion_2 == 1:
                #se ejecuta la funcion "os.system" con el comando "cls" para limpiar consola 
                os.system("cls")
                #convertimos la variable "favorito" en str
                fav = str(favorito)
                #se reemplaza la opcion 1 por la opcion ingresada en favorito
                menu[1]=(menu2[favorito]).replace((fav),'1')
                #se rempaza opcion elejida como favorito por la opcion 1
                menu[(favorito)]=menu2[1].replace('1',(fav))
            #si la respuesta es incorrecta debe volver al menú principal 
            else:
                print("Error")
                continue
         # si el usuario elije como opción favorita una opción incorrecta, se finaliza la ejecución del programa  
        else:
            print("Error")
            break
     #al elejir una opción del menú, se confirma ingreso a la opción elejida y finaliza la ejecución del programa               
    elif opcion > 0 and opcion < 6:
        print(f"Usted ha elegido la opción {opcion}")
     #si el usuario elije la opcion 7, se confirma cierre de sesión y se finaliza la ejecución del programa 
    elif opcion == 7:
        print("Hasta pronto")
        break
     #usamos la variable contadora 
    else:
        while cont <=2:
            cont +=1
            print("Error")
            opcion = int(input("Elija una opción: "))
            if opcion > 0 and opcion < 6:
                print(f"Usted ha elegido la opción {opcion}")
            elif opcion == 7:
                print("Hasta pronto")
                break
        print("Error")
        break
    if opcion == 1:
        entrada2 = input("contraseña actual: ")
        if entrada2 == contraseña:
            nueva_contraseña = input("Ingrese nueva contraseña: ") 
            if nueva_contraseña == contraseña:
                continue
        else:
            print("Error")
            break
    if opcion == 2 :
        cont1 = (len(matriz))
        if cont1  == 0:
            for i in range(3):
                matriz.append([])
                latitud = input(f"digite el valor de la latitud {i+1} ")
                if not latitud:
                        print("Error")
                        exit()
                else:
                    if float(latitud) <= -3.002 and float(latitud) >= -4.227:
                        for j in range(1):
                            matriz[i].append(latitud)
                    else:
                        print("Error coordenada")
                        exit()
                for k in range(1):
                    longitud = input(f"digite el valor de la longitud {i+1} ")
                    if  not longitud:
                        print("Error")
                        exit()
                    else:
                        if float(longitud) <= -69.714 and float(longitud) >= -70.365:
                            matriz[k].append(longitud)
                        else:
                            print("Error coordenada")
                            exit()
        if cont1 > 0 :
            coordenada1 = matriz[0]  
            coordenada2 = matriz[1]     
            coordenada3 = matriz[2]    
            print(f"coordenada [latitud,longitud] 1 : {coordenada1}")
            print(f"coordenada [latitud,longitud] 2 : {coordenada2}")
            print(f"coordenada [latitud,longitud] 3 : {coordenada3}")
            print("Coordenada 1 ubicada más al norte")
            print("Coordenada 2 ubicada más al oriente")
            actualizacion = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú \n"))
            if actualizacion == 1:
                matriz2=[]
                latitud = input("ingrese coordenada: ")
                if float(latitud) <= -3.002 and float(latitud) >= -4.227:
                    matriz2.append(latitud)
                    matriz[coordenada1== latitud] = matriz2
                longitud = input("ingrese coordenada: ")     
                if float(longitud) <= -69.714 and float(longitud) >= -70.365:
                    matriz2.append(longitud) 
                    matriz[coordenada1== longitud] = matriz2
                (matriz)
                continue
            elif actualizacion == 2:
                matriz2=[]
                latitud = input("ingrese coordenada: ")
                if float(latitud) <= -3.002 and float(latitud) >= -4.227:
                    matriz2.append(latitud)
                    matriz[coordenada2== latitud] = matriz2
                longitud = input("ingrese coordenada: ")     
                if float(longitud) <= -69.714 and float(longitud) >= -70.365:
                    matriz2.append(longitud) 
                    matriz[coordenada2== longitud] = matriz2
                (matriz)
                continue
            else:
                actualizacion <0 and actualizacion >3
                print("Error actualización")
                break 
