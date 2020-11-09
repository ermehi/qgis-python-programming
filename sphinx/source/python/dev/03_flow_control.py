numero = int(input("Dame un número entero: "))
if numero < 0:
    print("Negativo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Cero")

numero = int(input("Dame un número entero: "))
if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Cero")


contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# iterarción en una secuencia
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)

# range(start-value, end-value, difference between the values)
for i in range(0,10,1):
    print(i)
for i in range(0,10,-1):
    print(i)
for i in range(0,10,2):
    print(i)

# continue statement
# example 1
print("Sentencia continue. Primer ejemplo")
for letra in "PyQGIS":
    if letra == "Q":
        continue
    print("Letra actual: ", letra)
print("Adios")

print("\nSentencia continue. Primer ejemplo")
# example 2
var = 10
while var > 0:
   var = var -1
   if var == 5:
      continue
   print("Valor variable actual:", var)
print("Adios")

# break statement
# example 1
print("\nSentencia break. Primer ejemplo")
for letra in "PyQGIS":
    if letra == "Q":
        break
    print("Letra actual: ", letra)
print("Adios")

# example 2
print("\nSentencia break. Segundo ejemplo")
var = 10
while var > 0:
   var = var -1
   if var == 5:
      break
   print("Valor variable actual:", var)
print("Adios")

# pass statement
print("\nSentencia pass")
for letra in "PyQGIS":
    if letra == "Q":
        pass
    print("Letra actual: ", letra)
print("Adios")