print("Comision del 25%")
tcomisiones=0
for i in range (0, 2, 1):
    nombre=str (input("Ingrese el nombre del vendedor: "))
    venta=float (input("Ingrese la venta del mes del vendedor: "))
    comision=int= venta*0.25
    tcomisiones=tcomisiones+comision
    i=i+1
    print("El valor de la comision es de", comision, "para el vendedor""  ", nombre)
print("La comision del vednendor es de: ", comision)
print("la comisones son de: ", tcomisiones)
print("la cantidad de vendedores contados son: ", i)
