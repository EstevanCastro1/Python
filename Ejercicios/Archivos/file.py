

#open() lesctura y escritura de archivos
# 3 argumentos 1 nombre del archivo y la ruta/ modo de acceso (w,r,a) 3 buffer de archivo
def crearArchivo():
    archivo= open("D:\Estevan Castro\Escritorio\inventario.txt", "w")
    print("El archivo se creo correctamente")
    archivo.close()

def escribirArchivo():
    archivo= open("D:\Estevan Castro\Escritorio\inventario.txt", "a")
    cadena= input("Ingrese su Nombre: ")
    edad=int(input("Ingrese su Edad: "))
    archivo.write(cadena)
    archivo.write(",")
    archivo.write(str(edad))
    print("los datos se guardaron correctamente")
    archivo.close

def lecturaArchivo():
    archivo= open("D:\Estevan Castro\Escritorio\inventario.txt", "r")
    for i in archivo:
        print(i)
    archivo.close
#Cuerpo de codigo
crearArchivo()
escribirArchivo()
lecturaArchivo()