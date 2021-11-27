import os
Nombre_de_usuario=51732
Contraseña=23715
lista=["1.Cambiar contraseña", "2.Ingresar coordenadas actuales","3.Ubicar zona wifi más cercana","4.Guardar archivo con ubicación cercana",
"5.Actualizar registros de zonas wifi desde archivo","6.Elegir opción de menú favorita","7.Cerrar sesión"]
contador=0
while True:
        for i in lista:
            print(i)
        opc=int(input("Elija una opción"))
####################################################################################################################################
###############*******************************CONTRASEÑA*********************************************************###################        
        if   opc==1:
            validarcontraseña=int (input("Escriba su contraseña anterior:"))
            if validarcontraseña==Contraseña:
                nuevacontraseña=int (input("Escriba la nueva contraseña"))
                if nuevacontraseña==Contraseña:
                    print("Error")
                else: 
                    Contraseña=nuevacontraseña
            else:
                print("Error")
#####################################################################################################################################                
##################*****************************OPCIONES*********************************************************#####################            
        elif opc==2:
            print("Usted ha elegido la opción 2")
            break
        elif opc==3:
            print("Usted ha elegido la opción 3")
            break
        elif opc==4:
            print("Usted ha elegido la opción 4")
            break
        elif opc==5:
            print("Usted ha elegido la opción 5")
            break
##################################################################################################################################################
###############*********************************OPCION FAVORITA******************************************************************###################    
        if opc==6:
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
#########################################################################################################################################################
#########################################################################################################################################################             
        if opc<1 or opc>7:
            print("Error")
            contador=contador+1
            if contador==4:
                break

        if opc==7:
            print("Hasta pronto")
            break
        



