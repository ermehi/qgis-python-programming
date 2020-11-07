# -*- coding: utf-8 -*-

# consulta version del interprete de Python
import sys
sys.version
#IDEA: donde se localiza el interprete de Python de QGIS
# C:\Program Files\QGIS 2.18\bin

# variables no se declaran explicitamente -> se definen al asignarles un valor
  # NameError: name 'my_var' is not defined
my_var = 1
my_var  # 1

# tipos basicos de variables
fecha = 2017  # <type 'int'>
type(fecha)
fecha = 2017.0  # <type 'float'>
type(fecha)
fecha = "2017"
type(fecha)  # <type 'str'>

# NUMEROS ********************************************************************

# operadores artimeticos
suma = 2 + 3
suma, type(suma)  # 5 <type 'int'>

suma = 2 + 3.0
suma, type(suma)  # 5.0 <type 'float'>

# conversion entre numeros
int(3.14159265359)  # 3
float(7)  # 7.0

# CADENAS DE TEXTO ***********************************************************
str_geom_wkt = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"  # definicion 1
str_geom_wkt = 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))'  # definicion 2

str_geom_wkt[0]  # acceso a elemento de una cadena por su indice 'P'

# secuencias escape cadenas de texto
levantamiento = "Nº\tX\t\tY\t\tCOD\n1\t728762.67\t4328983.25\t\"bordillo\"\n2\t728785.42\t4328998.43\t\'acera.\b\'"
print(levantamiento)

# texto en varias lineas
texto_varias_lineas = """linea 1
linea 2
linea n"""  # 'linea 1\nlinea 2\nlinea n' no necesaria secuencia escape \n

# algunos metodos objeto cadena texto
str_geom_wkt = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"
lados_poligono = str_geom_wkt.count(",")  # devuelve numero int de veces que se encuentra "," en la cadena str_geom_wkt
lados_poligono  # 4

coor_pto = "728762.67, 4328983.25"
coor_pto_separador_csv = coor_pto.replace(",", ";")
coor_pto_separador_punto_decimal = coor_pto_separador_csv.replace(".",",")
coor_pto_separador_punto_decimal  # '728762,67; 4328983,25'

# concatenacion de cadenas de texto
texto = "con" + "ca" + "te" + "nar" + " "
texto  # 'concatenar '
repite = texto * 2
repite

# comparacion cadenas de texto
str_geom_wkt1 = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"
str_geom_wkt2 = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"
str_geom_wkt3 = "LINESTRING (30 10, 10 30, 40 40)"
str_geom_wkt1 == str_geom_wkt2  # True
str_geom_wkt1 == str_geom_wkt3  # False

# BOOLEANOS ******************************************************************
# operadores lOgicos y condicionales
r = True and False  # False
r = True or False  # True
r = not True   # False

# operadores relacionales
r = 5 == 3  # False
r = 5 != 3  # True
r = 5 < 3  # False
r = 5 > 3  # True
r = 5 <= 3  # False
r = 5 >= 3  # True

# MISCELANEA *****************************************************************
# eliminacion de variables
my_var = "Curso PyQGIS"
my_var  # 'Curso PyQGIS'
del(my_var)
my_var  # NameError: name 'my_var' is not defined

# asignacion aumentada
count = 0
count += 1
count  # 1

# asignación multiple con distintos valores
str_version, count = "v.1.0.2", 1
str_version  # 'v.1.0.2'
count  # 1

# asignación multiple con el mismo valor
x_min_mancanvas = x_min_aoi = 0.0
x_min_mancanvas  # 0.0
x_min_aoi  # 0.0

# obtener ayuda
from qgis.core import *

# obtener ayuda
help(iface.addVectorLayer)
help(QgsGeometry.fromWkt)
dir(QgsGeometry)