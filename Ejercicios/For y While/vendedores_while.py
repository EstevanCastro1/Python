i=0
while i!=999:
    nombre=str (input("Ingrese el nombre del vendedor: "))
    venta=int (input("Ingrese la venta del mes del vendedor: "))
    comision=venta*0.25
    print("El valor de la comision es de", comision, "para el vendedor", nombre)
    i=int(input("pulse el numero 1 para seguir agregando vendedores o pulse 999 para salir: "))
print("Gracias")


