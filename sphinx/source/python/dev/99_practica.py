# -*- coding: utf-8 -*-


# ejemplo serie de fibonacci
"""
En matemática, la sucesión de Fibonacci es la siguiente sucesión infinita de números naturales:
La sucesión comienza con los números 0 y 1,2​ y a partir de estos, «cada término es la suma de los dos anteriores», es la relación de recurrencia que la define.

"""

def fib(n):  # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n"""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(2000)

# Ejemplo retorno de una funcion
def fib2(n):  # escribe la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        print a,
        a, b = b, a+b
    return result

f100 = fib2(100)
print f100



# -*- coding: UTF-8 -*-

"""
Simple código que devuelve el factorial de un numero dado

Para calcular dicho valor, hay que multiplicar el numero dado, por su
antecesor mientas sea superior a 1

Ejemplo del factorial de 5 seria:
	5 * 4 * 3 * 2 * 1  = 120
"""


def factorial(x, n):
    """
    Función recursiva que calcula el factorial
    Tiene que recibir:
        x=>El ultimo valor calculado
        n=>El numero a multiplicar
    """
    if (n > 0):
        # Se va llamando a ella misma mientras el valor sea superior a 0
        x = factorial(x, n - 1)
        x = x * n
    else:
        x = 1
    return x


try:
    numero = int(raw_input("inserta un numero "))

    # Ejecutamos la función recusiva para el calculo
    calculo = factorial(1, numero)
    print "El factorial de %s es %s" % (numero, calculo)
except:
    print "\nTiene que ser un valor numerico"


# !/usr/bin/python
# -*- coding: utf-8 -*-

def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    for i in range(2, numero):
        if (numero % i) == 0:
            # es divisible
            return False
    return True


while True:
    try:
        numero = int(raw_input("inserta un numero (0) salir >> "))
        if numero == 0:
            break
        if es_primo(numero):
            print "\nEl numero %s es primo" % numero
        else:
            print "\nEl numero %s NO es primo" % numero
    except:
        print "\nEl numero tiene que ser entero"