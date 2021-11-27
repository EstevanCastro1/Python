import math
contador2=0
coordenada=[]
modificar=[]
boyaca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
validacion1=()
validacion2=()
longitud=[]
latitud=[]
def calcular_distancia(lat1, long1):
    w_cerca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
    dis=[]
    contador3=0
    for v in range(4):
        rad= math.pi/180
        dlat=w_cerca[v][0]-lat1
        dlon=w_cerca[v][1]-long1
        R=6372.795477598
        z=(math.sin(rad*dlat/2))**2+math.cos(rad*lat1)*math.cos(rad*w_cerca[v][0])*(math.sin(rad*dlon/2))**2
        distancia=2*R*math.asin(math.sqrt(z))
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
                print("la zona wifi 1: ubicada en", coordenada[0], "a", "{0:.2f}".format(minimo) , " metros tiene en promedio de",us, "usuarios")
                print("la zona wifi 1: ubicada en", coordenada[0], "a", "{0:.2f}".format(maximo) , " metros tiene en promedio de",us2, "usuarios")
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
def calcular_distancia1(lat1, long1):
    w_cerca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
    dis=[]
    contador3=0
    for v in range(4):
        rad= math.pi/180
        dlat=w_cerca[v][0]-lat1
        dlon=w_cerca[v][1]-long1
        R=6372.795477598
        z=(math.sin(rad*dlat/2))**2+math.cos(rad*lat1)*math.cos(rad*w_cerca[v][0])*(math.sin(rad*dlon/2))**2
        distancia=2*R*math.asin(math.sqrt(z))
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
                print("la zona wifi 1: ubicada en", coordenada[1], "a", "{0:.2f}".format(minimo) , " metros tiene en promedio de",us, "usuarios")
                print("la zona wifi 1: ubicada en", coordenada[1], "a", "{0:.2f}".format(maximo) , " metros tiene en promedio de",us2, "usuarios")
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
def calcular_distancia2(lat1, long1):
    w_cerca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
    dis=[]
    contador3=0
    for v in range(4):
        rad= math.pi/180
        dlat=w_cerca[v][0]-lat1
        dlon=w_cerca[v][1]-long1
        R=6372.795477598
        z=(math.sin(rad*dlat/2))**2+math.cos(rad*lat1)*math.cos(rad*w_cerca[v][0])*(math.sin(rad*dlon/2))**2
        distancia=2*R*math.asin(math.sqrt(z))
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
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
Nombre_de_usuario=51732
Contraseña=23715
Datos_de_salida="Error"
Captcha= (5+2)+(7-1)-(7+2+1)
usuario= int ((input("digite el nombre de usuario:")))
if  usuario!=Nombre_de_usuario:
    print(Datos_de_salida)
    exit()

else:
    clave= int ((input("Digite la contraseña:")))  
    if  clave!=Contraseña:
        print(Datos_de_salida)
        exit()

    else:
        validacion=int((input("Para verificar que no eres un robot, realice la siguiente operacion y digite el resultado 732+3 =")))
        if  validacion!=Captcha+732:
            print(Datos_de_salida) 
            (exit)
        else:
            print("Sesión iniciada")
lista=["1.Cambiar contraseña", "2.Ingresar coordenadas actuales","3.Ubicar zona wifi más cercana","4.Guardar archivo con ubicación cercana",
"5.Actualizar registros de zonas wifi desde archivo","6.Elegir opción de menú favorita","7.Cerrar sesión"]
contador=0
contador2=0
#try:
while True:
        for i in lista:
            print(i)
        opc=int(input("Elija una opción"))
        if  opc==1:
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
        if  opc==2:
            cant1=(len(coordenada))
            if cant1==0:
                for q in range(3):
                    coordenada.append([])
                    validacion1=float(input(f"digite el valor de la latitud {q+1} "))
                    if validacion1>=5.777 and validacion1<=6.307:
                        coordenada[q].append(validacion1)
                        contador2=contador2+1
                        if contador2==6:
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
                    contador2=0
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
        if  opc==3:
            cant1=(len(coordenada))
            if cant1==0:
            
                print("Error sin registro de coordenadas")
                break
            if cant1>0:
                    print("coordenada [latitud,longitud] 1:", coordenada[0])
                    print("coordenada [latitud,longitud] 2:", coordenada[1])
                    print("coordenada [latitud,longitud] 3:", coordenada[2])
                    op=int(input("Por favor elija su ubicacion actual (1,2 ó 3) para calcular la distancia a los puntos de conexion"))
                    if op<1 or op>3:
                        print("Error ubicación")
                        exit()
                    if op==1:
                        i = 0
                        columna = [fila[i] for fila in coordenada]
                        longitud.append(columna)
                        for m in longitud:  
                            long1=m[0]
                        i = 1 
                        filas = [fila[i] for fila in coordenada]
                        latitud.append(filas)
                        for m in latitud:  
                            lat1=m[0]
                        calcular_distancia(long1,lat1)                    
                    if op==2:
                        i = 0
                        columna = [fila[i] for fila in coordenada]
                        longitud.append(columna)
                        for m in longitud:  
                            long2=m[1]
                        i = 1 
                        filas = [fila[i] for fila in coordenada]
                        latitud.append(filas)
                        for m in latitud:  
                            lat2=m[1]                     
                        calcular_distancia1(long2,lat2)
                    if op==3:
                        i = 0
                        columna = [fila[i] for fila in coordenada]
                        longitud.append(columna)
                        for m in longitud:  
                            long3=m[2]
                        i = 1 
                        filas = [fila[i] for fila in coordenada]
                        latitud.append(filas)
                        for m in latitud:  
                            lat3=m[2]                        
                        calcular_distancia2(long3,lat3)
        if  opc==4:
            print("Usted ha elegido la opción 4")
            break
        if  opc==5:
            print("Usted ha elegido la opción 5")
            break
        if  opc==6:
            sel=int (input("Seleccione opción favorita"))
            if sel>0 and sel<2:
                ad=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
                if ad>2 and ad<4:
                    ad1=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                    if ad1>1 and ad1<3:
                        lista[0]=("1.Cambiar contraseña")

            if sel>1 and sel<3:
                ad=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
                if ad>2 and ad<4:
                    ad1=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                    if ad1>1 and ad1<3:
                        lista[0]=("1.Ingresar coordenadas actuales")
                        lista[1]=("2.Cambiar contraseña")    

            if sel>2 and sel<4:
                ad=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
                if ad>2 and ad<4:
                    ad1=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                    if ad1>1 and ad1<3:                        
                        lista[0]=("1.Ubicar zona wifi más cercana")
                        lista[1]=("2.Cambiar contraseña")
                        lista[2]=("3.Ingresar coordenadas actuales") 

            if sel>3 and sel<5:
                ad=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
                if ad>2 and ad<4:
                    ad1=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                    if ad1>1 and ad1<3:                        
                        lista[0]=("1.Guardar archivo con ubicación cercana")
                        lista[1]=("2.Cambiar contraseña")
                        lista[2]=("3.Ingresar coordenadas actuales")
                        lista[3]=("4.Ubicar zona wifi más cercana")

            if sel>4 and sel<6:
                ad=int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un, la respuesta es:"))
                if ad>2 and ad<4:
                    ad1=int(input("Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des, la respuesta es:"))
                    if ad1>1 and ad1<3:                        
                        lista[0]=("1.Actualizar registros de zonas wifi desde archivo")
                        lista[1]=("2.Cambiar contraseña")
                        lista[2]=("3.Ingresar coordenadas actuales")
                        lista[3]=("4.Ubicar zona wifi más cercana")
                        lista[4]=("5.Guardar archivo con ubicación cercana")

            if sel>5 or sel<1 :
                print("Error")
                exit()
            if ad<3 or ad>3:
                print("Error") 
            if ad1<2 or ad1>2:
                print("Error")   
        if  opc==7:
            print("Hasta pronto")
            break
        if  opc<1 or opc>7:
            print("Error")
            contador=contador+1
            if contador==4:
                break




