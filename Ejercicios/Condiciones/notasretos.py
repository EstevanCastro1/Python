print("Aprobacion de los retos")
nombre= (input("Ingrese su nombre completo: "))
codigo= (input("Ingrese su codigo de estudiante: "))
nota1= float (input("Ingrese la nota del reto 1: "))
total1=nota1*0.10

nota2= float (input("Ingrese la nota del reto 2: "))
total2=nota2*0.10

nota3= float (input("Ingrese la nota del reto 3: "))
total3=nota3*0.20

nota4= float (input("Ingrese la nota del reto 4: "))
total4=nota4*0.20

nota5= float (input("Ingrese la nota del reto 5: "))
total5=nota5*0.40

aprob= total1+total2+total3+total4+total5/5

if aprob >59:
    print(f"Estudiante {nombre} con codigo {codigo}")
    print(f"reto 1 con promedio de : {total1} %")
    print(f"reto 2 con promedio de : {total2} %")
    print(f"reto 3 con promedio de : {total3} %")
    print(f"reto 4 con promedio de : {total4} %")
    print(f"reto 5 con promedio de : {total5} %")
    print(f"usted aprobo con un promedio de  : {aprob} %")
else:
    print(f"Estudiante {nombre} con codigo {codigo}")
    print(f"reto 1 con promedio de : {total1} %")
    print(f"reto 2 con promedio de : {total2} %")
    print(f"reto 3 con promedio de : {total3} %")
    print(f"reto 4 con promedio de : {total4} %")
    print(f"reto 5 con promedio de : {total5} %")
    print(f"usted no aprobo porque saco un promedio de: {aprob} % para aprobar se necesita el 60%")

