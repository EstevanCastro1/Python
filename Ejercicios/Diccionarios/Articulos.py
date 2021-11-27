nombres = {"001":"Cuaderno","002":"Lapicero",
"003":"Calculadora","004":"Cartilla nacho"}
valores = {"001":2000,"002":1200,"003":25000
,"004":18000,}

can_elementos=int(input("Ingrse la cantidad de elementos: "))
vcompra=0
cantotal=0
for i in range(can_elementos):
    cod=str(input("Ingrese el codigo: "))
    cant=int(input("Ingrese la cantidad de elementos a comprar: "))
    varticulo=cant*valores[cod]
    cantotal=cantotal+cant
    vcompra=vcompra+varticulo
    print(f"Nombre: {nombres[cod]} precio: {valores[cod]} camtidad {cant} valor total {varticulo} ")
    print(f"Estos articulos valen: {varticulo}")
print(f"el total de articulos comprados es: {cantotal}")
print(f"El valor de la compra es: {vcompra}")
