boyaca=[[6.211,-72.481],[6.212,-72.470],[6.105,-72.342]]
dis=[8.720622451945435, 8.570843075595231, 25.07332445310197, 9.431706391686538]
usuarios = [2, 25, 25, 50]
dic = {dis[p]: usuarios[p] for p in range(len(dis))}
maximo= max(dic)
del dic[maximo]
maximo= max(dic)
del dic[maximo]
minimo=min(dic)
maximo=max(dic)
us=dic.setdefault(minimo)
us2=dic.setdefault(maximo)

print("la zona wifi 1: ubicada en", boyaca[0], "a", "{0:.2f}".format(minimo) , "metros tiene en promedio de",us, "usuarios")
print("la zona wifi 1: ubicada en", boyaca[0], "a", "{0:.2f}".format(maximo) , "metros tiene en promedio de",us2, "usuarios")


bus=(minimo/16.7)
auto=(minimo/20.83)
print("El tiempo promedio para llegar en bus es de", "{0:.2f}".format(bus),"segundos y en auto es de", "{0:.2f}".format(auto),"segundos")