"""
Escribe un programa que permita crear una lista de palabras.
Para ello, el programa pedirá un número y luego solicitará el valor de ese número de palabras para crear la lista.
Finalmente, el programa escribirá en pantalla la lista creada.
"""

len_lista = int(input("Indique cuántas palabras tiene la lista: "))

if len_lista < 1:
    print("El número de palabras tiene que ser mayor que 0")
else:
    lista = []
    for i in range(len_lista):
        palabra = input("Introduzca la palabra " + str(i+1) + ":")
        lista.append(palabra)

    print("La lista creada es:", lista)