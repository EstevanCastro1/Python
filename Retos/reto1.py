print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
Nombre_de_usuario=51732
Contraseña=23715
Datos_de_salida="Error"
Captcha= (5+2)+(7-1)-(7+2+1)

#Ingreso de usuario
usuario= int ((input("digite el nombre de usuario:")))
if  usuario!=Nombre_de_usuario:
    print(Datos_de_salida)
#Ingreso de contraseña
else:
    clave= int ((input("Digite la contraseña:")))  
    if  clave!=Contraseña:
        print(Datos_de_salida)
#Validacion de Captcha
    else:
        validacion=int((input("Para verificar que no eres un robot, realice la siguiente operacion y digite el resultado 732+3 =")))
        if  validacion!=Captcha+732:
            print(Datos_de_salida) 
        else:
            print("Sesión iniciada")
