# -*- coding: utf-8 -*-

# manejo de excepciones ******************************************************
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Denominador cero!!!")
    else:
        print("El resultado es", result)
    finally:
        print("Ejecución claúsula finally")

divide(2,1)
divide(2,0)
divide("2","1")  # excepcion no controlada

# The exception argument *****************************************************
def divide(x, y):
    try:
        result = x / y
        print("El resultado es:", result)
    except Exception as detail:
        print(detail, type(detail))

divide(2,0)  #TODO: probar
divide("2","1")

