print("Hola, escribe un numero y te decimos si es par o impar")
i=1
while i!=int:
  i=int (input("Si pulsa 0 el programa terminara su proceso" "... " "o Escriba un numero: "))
  if i==0:
   break
  elif i%2==0:
   print("es par")
  else:
   print("es impar")
print(i)
print("Gracias")
