############################################################### Inicio #####################################################################################################
import math
Nombre_de_usuario=51732
Contraseña=23715
Datos_de_salida="Error"
Captcha= (5+2)+(7-1)-(7+2+1)
validacion1=()
validacion2=()
contador=0
contador2=0
contador3=0
lista=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
coordenada=[]
modificar=[]
boyaca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
longitud=[]
latitud=[]
############################################################### Declaracion de Funciones Opcion 3 #########################################################################
def lat_long(op):
        i = 0
        columna = [fila[i] for fila in coordenada]
        latitud.append(columna)
        for m in latitud:  
            lat1=m[0]
            lat2=m[1]
            lat3=m[2]
        i = 1 
        filas = [fila[i] for fila in coordenada]
        longitud.append(filas)
        for m in longitud:  
            long1=m[0]
            long2=m[1]
            long3=m[2]
        if op==1:
            calcular_distancia(lat1,long1)                    
        if op==2:
            calcular_distancia(lat2,long2)
        if op==3: 
            calcular_distancia(lat3,long3)
        if op<1 or op>3:
            print("Error ubicación")
            exit()
def calcular_distancia(lat, long):
    dis=[]
    contador3=0
    for v in range(4):
        radianes= math.pi/180
        distancia_lat=boyaca[v][0]-lat
        distancia_lon=boyaca[v][1]-long
        radio=6372.795477598
        z=(math.sin(radianes*distancia_lat/2))**2+math.cos(radianes*lat)*math.cos(radianes*boyaca[v][0])*(math.sin(radianes*distancia_lon/2))**2
        distancia=2*radio*math.asin(math.sqrt(z))
        dis.append(distancia)
        usuarios = [2, 25, 5, 50]
        contador3=contador3+1
        if contador3>=4:
                dic = {dis[p]: usuarios[p] for p in range(len(dis))}
                maximo= max(dic)
                del dic[maximo]
                maximo= max(dic)
                del dic[maximo]
                minimo=min(dic)
                maximo=max(dic)
                us=dic.setdefault(minimo)
                us2=dic.setdefault(maximo)
                print("la zona wifi ubicada en las coordenadas:","(",lat,",",long,")", "a", "{0:.2f}".format(minimo) , "metros tiene en promedio de",us, "usuarios")
                print("la zona wifi ubicada en las coordenadas:","(", lat,",",long,")", "a", "{0:.2f}".format(maximo) , "metros tiene en promedio de",us2, "usuarios")
                kil=int(input("elija 1 o 2 para recibir indicaciones de llegada"))
                if kil==1:
                    bus=(minimo/16.7)
                    auto=(minimo/20.83)
                    print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")
                    cero=int(input("Presione 0 para salir"))
                    if cero==0:
                        break
                if kil==2:
                    bus=(maximo/16.7)
                    auto=(maximo/20.83)
                    print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")
                    cero=int(input("Presione 0 para salir"))
                    if cero==0:
                        break
                if kil<1 or kil>2:
                    print("Error zona wifi”")
                    exit()

    dis=[]
    contador3=0
    for v in range(4):
        radianes= math.pi/180
        distancia_lat=boyaca[v][0]-lat
        distancia_lon=boyaca[v][1]-long
        radio=6372.795477598
        z=(math.sin(radianes*distancia_lat/2))**2+math.cos(radianes*lat)*math.cos(radianes*boyaca[v][0])*(math.sin(radianes*distancia_lon/2))**2
        distancia=2*radio*math.asin(math.sqrt(z))
        dis.append(distancia)
        usuarios = [2, 25, 5, 50]
        contador3=contador3+1
        if contador3>=4:
                
                dic = {dis[p]: usuarios[p] for p in range(len(dis))}
                maximo= max(dic)
                del dic[maximo]
                maximo= max(dic)
                del dic[maximo]
                minimo=min(dic)
                maximo=max(dic)
                us=dic.setdefault(minimo)
                us2=dic.setdefault(maximo)
                print("la zona wifi 1: ubicada en", coordenada[2], "a", "{0:.2f}".format(minimo) , " metros tiene en promedio de",us, "usuarios")
                print("la zona wifi 1: ubicada en", coordenada[2], "a", "{0:.2f}".format(maximo) , " metros tiene en promedio de",us2, "usuarios")
                kil=int(input("elija 1 o 2 para recibir indicaciones de llegada"))
                if kil==1:
                    bus=(minimo/16.7)
                    auto=(minimo/20.83)
                    print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")
                    cero=int(input("Presione 0 para salir"))
                if kil==2:
                    bus=(maximo/16.7)
                    auto=(maximo/20.83)
                    print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")
                    cero=int(input("Presione 0 para salir"))
                if kil<1 or kil>2:
                    print("Error zona wifi”")
                    exit()
############################################################### Primer Paso ###############################################################################################
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
############################################################### Ingreso de usuario ########################################################################################
usuario= int ((input("digite el nombre de usuario:")))
if  usuario!=Nombre_de_usuario:
    print(Datos_de_salida)
    exit()
############################################################### Ingreso de contraseña #####################################################################################
else:
    clave= int ((input("Digite la contraseña:")))  
    if  clave!=Contraseña:
        print(Datos_de_salida)
        exit()
############################################################### Validacion de Captcha #####################################################################################
    else:
        validacion=int((input("Para verificar que no eres un robot, realice la siguiente operacion y digite el resultado 732+3 =")))
        if  validacion!=Captcha+732:
            print(Datos_de_salida) 
            (exit)
        else:
            print("Sesión iniciada")
############################################################### Elegir una Opcion #########################################################################################
while True:
    print(f"\n1. {lista[0]}\n2. {lista[1]}\n3. {lista[2]}\n4. {lista[3]}\n5. {lista[4]}\n6. {lista[5]}\n7. {lista[6]}")
    opc=int(input("Elija una opción"))
############################################################### 1.Opcion Cambiar contraseña ###############################################################################       
    if opc==1:
        validarcontraseña=int (input("Escriba su contraseña anterior:"))
        if validarcontraseña!=Contraseña:
            pass
        if validarcontraseña==Contraseña:
            nuevacontraseña=int (input("Escriba la nueva contraseña"))
            if nuevacontraseña==Contraseña:
                print("Error")
                exit()
            else: 
                Contraseña=nuevacontraseña
        else:
            print("Error")
            exit()
############################################################### 2.Opcion Ingresar Coordenadas Actuales ####################################################################
    if opc==2:
        cant1=(len(coordenada))
        if cant1==0:
            for q in range(3):
                coordenada.append([])
                validacion1=float(input(f"digite el valor de la latitud {q+1} "))
                if validacion1>=5.777 and validacion1<=6.307:
                    coordenada[q].append(validacion1)
                    contador3=contador3+1
                    if contador3==6:
                        break                        
                else:
                    print("Error coordenada")
                    exit()
                for w in range(1):      
                        validacion2=float(input(f"digite el valor de la longitud {q+1} "))
                        if validacion2<=(-72.321) and validacion2>=(-72.552):
                            coordenada[q].append(validacion2)
                            break
                        else:
                            print("Error coordenada")
                            exit()
        if cant1>0:
                contador3=0
                print("coordenada [latitud,longitud] 1:", coordenada[0])
                print("coordenada [latitud,longitud] 2:", coordenada[1])
                print("coordenada [latitud,longitud] 3:", coordenada[2])
                if coordenada[0] > coordenada[1] and coordenada[0] > coordenada[2]:
                    print("Coordenada 1 ubicada más al norte")
                if coordenada[1] > coordenada[0] and coordenada[1] > coordenada[2]:
                    print("Coordenada 2 ubicada más al norte")
                if coordenada[2] > coordenada[0] and coordenada[2] > coordenada[1]:
                    print("Coordenada 2 ubicada más al norte")
                if coordenada[0] < coordenada[1] and coordenada[0] < coordenada[2]:
                    print("Coordenada 1 ubicada más al occidente")
                if coordenada[1] < coordenada[0] and coordenada[1] < coordenada[2]:
                    print("Coordenada 2 ubicada más al occidente")
                if coordenada[2] < coordenada[0] and coordenada[2] < coordenada[1]:
                    print("Coordenada 3 ubicada más al occidente")   
                esc=int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada.\nPresione 0 para regresar al menú"))
                if esc==1:
                    for q in range(1):
                        modificar.append([])
                        validacion1=float(input(f"digite el valor de la latitud {q+1} "))
                        if validacion1>=5.777 and validacion1<=6.307:
                            modificar[q].append(validacion1)
                        else:
                            print("Error coordenada")
                            exit()
                        for w in range(1):      
                                validacion2=float(input(f"digite el valor de la longitud {q+1} "))
                                if validacion2<=(-72.321) and validacion2>=(-72.552):
                                    modificar[q].append(validacion2)
                                    coordenada.pop(0)
                                    coordenada.insert(0, modificar)
                                else:
                                    print("Error coordenada")
                                    exit()                                      
                if esc==2:
                    for q in range(1):
                        modificar.append([])
                        validacion1=float(input(f"digite el valor de la latitud {q+1} "))
                        if validacion1>=5.777 and validacion1<=6.307:
                            modificar[q].append(validacion1)
                        else:
                            print("Error coordenada")
                            exit()
                        for w in range(1):      
                                validacion2=float(input(f"digite el valor de la longitud {q+1} "))
                                if validacion2<=(-72.321) and validacion2>=(-72.552):
                                    modificar[q].append(validacion2)
                                    coordenada.pop(1)
                                    coordenada.insert(1, modificar) 
                                else:
                                    print("Error coordenada")
                                    exit()                          
                if esc==3:
                    for q in range(1):
                        modificar.append([])
                        validacion1=float(input(f"digite el valor de la latitud {q+1} "))
                        if validacion1>=5.777 and validacion1<=6.307:
                            modificar[q].append(validacion1)
                        else:
                            print("Error coordenada")
                            exit()
                        for w in range(1):      
                                validacion2=float(input(f"digite el valor de la longitud {q+1} "))
                                if validacion2<=(-72.321) and validacion2>=(-72.552):
                                    modificar[q].append(validacion2)
                                    coordenada.pop(2)
                                    coordenada.insert(2, modificar) 
                                else:
                                    print("Error coordenada")
                                    exit()                                                                           
                if esc==0:
                    break

                if esc>1 or esc>3:
                    print("Error actualización")
                    exit()        
############################################################### 3.Opcion Ubicar zona wifi mas cercana #####################################################################       
    if opc==3:
        cant1=(len(coordenada))
        if cant1==0:
            print("Error sin registro de coordenadas")
            break
        if cant1>0:
                print("coordenada [latitud,longitud] 1:", coordenada[0])
                print("coordenada [latitud,longitud] 2:", coordenada[1])
                print("coordenada [latitud,longitud] 3:", coordenada[2])
                op=int(input("Por favor elija su ubicacion actual (1,2 ó 3) para calcular la distancia a los puntos de conexion"))
                lat_long(op)
############################################################### 4.Opcion Guardar archivo con Ubicacion Cercana ############################################################
    if opc==4:
        print("Usted ha elegido la opción 4")
        break
############################################################### 5.Opcion Actualizar registros de zonas wifi desde archivo #################################################
    if opc==5:
        print("Usted ha elegido la opción 5")
        break
############################################################### 6.Opcion Elegir Opcion Favorita ###########################################################################
    if opc==6:
        sel=int(input("Seleccione opción favorita:"))
        if sel>0 and sel<6:
            ad1=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
            if ad1==3:
                ad2=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                if ad2==2:
                    contenedor = lista[0]
                    lista[0] = lista[(sel)-1]
                    lista[(sel)-1]= contenedor
                else:
                    print("Error")
            else:
                print("Error")        
        else:
            print("Error")
            break
############################################################### 7.Opcion Cerrar Sesion ####################################################################################
    if opc==7:
        print("Hasta pronto")
        break
############################################################### 7.1 limite ################################################################################################        
    if opc<1 or opc>7:
            print("Error")
            contador=contador+1
            if contador==4:
                break
############################################################### Fin #######################################################################################################