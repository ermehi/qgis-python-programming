# -*- coding: utf-8 -*-

# LISTS **********************************************************************
my_list = [22, True, "PyQGIS", [1, 2]]  # definicion y asignacion

# acceso a elementos de la lista
my_var = my_list[0]
my_var  # 22

# acceso a matrices (lista de listas)
my_var = my_list[3][0]
my_var  # 1

# modificacion elementos existentes
my_list[1] = False
my_list  # [22, False, 'PyQGIS', [1, 2]]

# acceso con numeros negativos
my_list[-1]  # [1, 2]

# slicing o particionado
my_var = my_list[0:2]
my_var  # [22, False]

my_var = my_list[0:4:2]
my_var  # [22, 'PyQGIS']

# algunos metodos del objeto lista
my_list.append(3.141592)  # añade un objeto al final de la lista
my_list  # [22, False, 'PyQGIS', [1, 2], 3.141592]

my_list.pop()  # Devuelve el valor en la posición index y lo elimina de la lista ->  3.141592
my_list  # [22, False, 'PyQGIS', [1, 2]]

my_list.insert(3, 3.141592)  # inserta un elemento en la posición index
my_list  # [22, False, 'PyQGIS', 3.141592, [1, 2]]

#TODO: comprobar que sucede con el acceso y modificación de elementos de una tupla
# TUPLES *********************************************************************
# definicion y asignacion
my_tuple = (22, True, "PyQGIS", [1, 2])
my_tuple = 22, True, "PyQGIS", [1, 2]
type(my_tuple)  # <type 'tuple'>

# acceso a elementos
my_var = my_tuple[0]
my_var  # 22
my_var = my_tuple[1:2]
my_var  # (True,)

# modificacion elementos existentes
my_tuple[1] = False # TypeError: 'tuple' object does not support item assignment

# CONVERSION LIST vs. TUPLA **************************************************
a_tuple = tuple(my_list)
a_tuple  # (22, False, 'PyQGIS', 3.141592, [1, 2])

a_list = list(my_tuple)
a_list  # [22, True, 'PyQGIS', [1, 2]]

# DICCIONARIOS ***************************************************************
# definicion y asignacion
my_dict = {"3857": "WGS 84/Pseudo Mercator",
           "4258": "ETRS89",
           "4326": "WGS 84",
           "25828": "ETRS 89/UTM 28N",
           "25830": "ETRS 89/UTM 30N",
           "32628": "WGS 84/UTM 28N",
           "32630": "WGS 84/UTM 30N"}

# acceso a elementos
my_dict["25830"]  # 'ETRS 89/UTM 30N'  # no se accede por su indice, sino por su key

# modificacion elementos existentes
my_dict["25830"] = "Sistema geodesico de referencia ETRS 89 - proyeccion cartografica UTM huso 30 Norte"
my_dict["25830"]  # 'Sistema geodesico de referencia ETRS 89 - proyeccion cartografica UTM huso 30 Norte'
my_dict["25830"] = "ETRS 89/UTM 30N"  # lo volvemos a dejar como estaba

# añadir nuevos elementos
my_dict["25831"] = "ETRS 89/UTM 31N"
my_dict  # {'4258': 'ETRS89', '4326': 'WGS 84', '3857': 'WGS 84/Pseudo Mercator', '25831': 'ETRS 89/UTM 31N', '25830': 'ETRS 89/UTM 30N', '32630': 'WGS 84/UTM 30N', '32628': 'WGS 84/UTM 28N', '25828': 'ETRS 89/UTM 28N'}


# algunos metodos del objeto diccionario
# Busca el valor de la clave k en el diccionario pero con devuelve default si no lo encuentra
my_dict.get("25830","Unknown SRC")  # 'ETRS 89/UTM 30N'
my_dict.get("25832","Unknown SRC")  # 'Unknown SRC'
my_dict["25832"]  # KeyError: '25832'

# comprueba si el diccionario tiene la clave k
my_dict.has_key("25830")  # True
my_dict.has_key("25832")  # False

my_dict.items()  # devuelve una tupla con pares key-value
my_dict.keys()  # devuelve una lista con las values del diccionario
my_dict.values()  # devuelve una lista con las values del diccionario