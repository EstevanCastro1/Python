import math
coordenada=[[6.289,-72.473],[6.288,-72.474],[6.287,-72.475]]
modificar=[]
boyaca=[[6.211,-72.481,2],[6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
longitud=[]
latitud=[]
def lat_long(op):
                if op<1 or op>3:
                    print("Error ubicación")
                    exit()
                if op==1:
                    i = 0
                    columna = [fila[i] for fila in coordenada]
                    latitud.append(columna)
                    for m in latitud:  
                        lat1=m[0]
                    i = 1 
                    filas = [fila[i] for fila in coordenada]
                    longitud.append(filas)
                    for m in longitud:  
                        long1=m[0]
                    calcular_distancia(lat1,long1)                    
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
                print("{0:.2f}".format(minimo))
                print("la zona wifi ubicada en las coordenadas:","(",lat,",",long,")", "a", "{0:.2f}".format(minimo) , "metros tiene en promedio de",us, "usuarios")
                print("la zona wifi ubicada en las coordenadas:","(", lat,",",long,")", "a", "{0:.2f}".format(maximo) , "metros tiene en promedio de",us2, "usuarios")
                kil=int(input("elija 1 o 2 para recibir indicaciones de llegada"))
                if kil==1:
                    bus=(minimo/16.7)
                    auto=(minimo/20.83)
                    print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")
                    cero=int(input("Presione 0 para salir"))



print("coordenada [latitud,longitud] 1:", coordenada[0])
print("coordenada [latitud,longitud] 2:", coordenada[1])
print("coordenada [latitud,longitud] 3:", coordenada[2])
op=int(input("Por favor elija su ubicacion actual (1,2 ó 3) para calcular la distancia a los puntos de conexion"))
lat_long(op)