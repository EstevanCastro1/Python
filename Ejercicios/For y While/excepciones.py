
while True:
    try:

        Cat=int(input("ingrese el numero 1"))
        if Cat<1 or Cat>1:
            print("Error, no eligio el numero 1 ")
        if Cat==1:
            print("Corecto eligio el numero 1")
        break
    except Exception as error:
        print("Por favor solo elija un numero")
        exit()
