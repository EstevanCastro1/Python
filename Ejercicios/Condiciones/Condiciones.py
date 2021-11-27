print("Compra de autos")
print("1 ===>para BMW")
print("2 ===>para AUDI")
print("3 ===>para TOYOTA")
tauto= float (input("Ingrese el tipo de auto que va comprar: "))
if tauto==1:
    bmw= int (input("Digite el valor de BMW: "))
    des= bmw*0.50
    total= int (bmw - des)
    print(f"El BMW tiene un costo de : {bmw}, y con el descuento de {des} queda en  {total} ")
elif tauto==2:
    audi= int (input("Digite el valor de AUDI: "))
    des= audi*0.30
    total= int (audi - des)
    print(f"El AUDI tiene un costo de : {audi}, y con el descuento de {des} queda en  {total} ")
elif tauto==3:
    toyota= int (input("Digite el valor de TOYOTA: "))
    des= toyota*0.15
    total= int (toyota - des)
    print(f"El TOYOTA tiene un costo de : {toyota}, y con el descuento de {des} queda en  {total} ")
#elif tauto!=1 or tauto!=2 or tauto!=3:
#    print("Usted eligio un numero que no esta en la lista")
 #   print("Adios")

else:
    print("Usted no eligio una opcion correcta")
    print("Adios")


